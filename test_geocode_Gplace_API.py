import requests, os
from dotenv import load_dotenv

# Load API key
load_dotenv()
key = os.getenv("GOOGLE_MAPS_API_KEY")

address_test = "Wat Phra Yai, Koh Samui"

# --- GEOCODE API ---
url_geocode = "https://maps.googleapis.com/maps/api/geocode/json"
params_geocode = {
    "address": address_test, 
    "key": key
    }
r = requests.get(url_geocode, params=params_geocode)
print("🌍 Geocode API:")
print(r.json())
print("*" * 60)

# --- PLACES FINDPLACEFROMTEXT API ---
url_gplace = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
params_gplace = {
    "input": address_test,
    "inputtype": "textquery",
    "fields": "name,geometry/location,place_id,formatted_address",
    "key": key
}
r = requests.get(url_gplace, params=params_gplace)
print("🏛️ Places FindPlaceFromText API:")
print(r.json())
print("*" * 60)


# om du får {"results": [], "status": "REQUEST_DENIED"} betyder det att API-nyckeln felaktig eller billing är inte aktiverad.
#om du får en liknande output som nedan betyder att API-anropet lyckades och du fick tillbaka geokodningsdata för den angivna adressen.:
