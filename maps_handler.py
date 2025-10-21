import requests
import folium
import re
import os
import webbrowser

class MapsHandlerTest:
    """Handles map logic, geocoding, and exporting location data using Google Maps APIs."""

    def __init__(self):
        """Initialize handler and load Google API key from .env"""
        self.locations = []
        self.api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    def find_coordinates_with_geocode_api(self, address):
        """Use Google Geocoding API to get coordinates. 
        Falls back to Places API if the result is too vague."""

        if not self.api_key:
            print("⚠️ GOOGLE_MAPS_API_KEY missing in .env")
            return None

        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": address, 
            "key": self.api_key
            }
        resp = requests.get(url, params=params)
        data = resp.json()

        if data["status"] == "OK":
            result = data["results"][0]
            loc = result["geometry"]["location"]
            loc_type = result["geometry"].get("location_type", "")

            # Fallback if precision is low
            if loc_type in ("GEOMETRIC_CENTER", "APPROXIMATE"):
                print(f"⚠️ Low precision for '{address}', trying Places API instead...")
                precise = self.find_coordinates_with_places_api(address)
                if precise:
                    return precise
            return loc["lat"], loc["lng"]
        else:
            print(f"⚠️ Could not geocode '{address}': {data['status']}")
            # direct fallback
            precise = self.find_coordinates_with_places_api(address)
            if precise:
                return precise
            return None

        
    def find_coordinates_with_places_api(self, query):
        """Find exact coordinates using Google Places API with optional city bias."""

        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        params = {
            "input": query,
            "inputtype": "textquery",
            "fields": "place_id,name",
            "key": self.api_key
        }

        resp = requests.get(url, params=params).json()

        if resp["status"] == "OK" and resp["candidates"]:
            place_id = resp["candidates"][0]["place_id"]

            # Get place details (higher precision)
            details_url = "https://maps.googleapis.com/maps/api/place/details/json"
            details_params = {
                "place_id": place_id,
                "fields": "geometry/location",
                "key": self.api_key
            }
            details = requests.get(details_url, params=details_params).json()
            if details["status"] == "OK":
                loc = details["result"]["geometry"]["location"]
                print(f"📍 Using Places Details precision for '{query}'")
                return loc["lat"], loc["lng"]
        return None



    def add_locations_from_response(self, response_text ):
        """Parse the AI’s text output and extract names + addresses, 
        then fetch precise coordinates from Google APIs."""

        pattern = r"(\d+\.\s+)?([^\n-]+)\s*-\s*[^\n]+\n.*?(?:Address|Address/Area).*?:\s*([^\n]+)"
        matches = re.findall(pattern, response_text, re.DOTALL)

        if not matches:
            print("⚠️ No valid address patterns found.\n")
            return False

        added = set()  # track unique names
        for _, name, address in matches:
            name, address = name.strip(), address.strip()
            if name in added:
                continue  # skip duplicates

            query = f"{name}, {address}, tourist attraction, famouse place, verified Google Maps location"
            coords = self.find_coordinates_with_geocode_api(query)

            if coords:
                lat, lon = coords
                self.locations.append((name, lat, lon))
                added.add(name)
                print(f"✅ Added: {name} → ({lat:.5f}, {lon:.5f})")
            else:
                print(f"⚠️ Skipped {name} (no coords found)\n")

        print()
        return len(self.locations) > 0

    def save_and_open_map(self):
        """Generate folium map with all locations and open in browser"""
        if not self.locations:
            print("ℹ️ No locations available to map.")
            return

        first_lat, first_lon = self.locations[0][1], self.locations[0][2]
        fmap = folium.Map(location=[first_lat, first_lon], zoom_start=13)

        for name, lat, lon in self.locations:
            folium.Marker([lat, lon], popup=name).add_to(fmap)

        map_file = "ai_places_map.html"
        fmap.save(map_file)
        webbrowser.open("file://" + os.path.realpath(map_file))
        print(f"🗺️ Map generated and opened: {map_file}\n")

    def show_available_locations(self):
        """Print all collected locations"""
        if not self.locations:
            print("No locations added yet.")
        else:
            for i, (name, lat, lon) in enumerate(self.locations):
                print(f"{i+1}. {name}: ({lat:.5f}, {lon:.5f})")


    def export_to_kml(self, filename="pigeon_places.kml"):
        """Export current locations to a KML file for Google My Maps"""
        kml = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>']

        for name, lat, lon in self.locations:
            kml.append(f"""
                <Placemark>
                    <name>{name}</name>
                    <Point><coordinates>{lon},{lat},0</coordinates></Point>
                </Placemark>
            """)

        kml.append("</Document></kml>")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(kml))
        print(f"📁 KML file created: {filename}")
        print("👉 Open https://www.google.com/mymaps and import the file to see your markers.")

