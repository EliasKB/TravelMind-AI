# 🌍📌 Travel Mind AI Agent

**An AI-powered travel and discovery assistant that recommends top-rated places, retrieves precise Google Maps coordinates, and exports them to KML for visualization.**

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Google Maps Integration](#google-maps-integration)
- [Project Structure](#-Project-Structure)
- [Google Cloud Setup](#google-cloud-setup)
- [Gmail Setup](#-Gmail-Setup)
- [Testing the APIs](#-Testing-the-APIs)
- [Customization](#-Customization)
- [Contributing](#-Contributing)
 
## ✨ Features

- 🤖 **AI-Powered Recommendations** — Uses OpenAI GPT-4o-mini (or GPT-5) to find top attractions restaurants, and hotels worldwide.
- 🗺️ **Google Maps Precision** — Combines Geocoding API and Places API for highly accurate latitude/longitude.
- 📁 **KML Export Support** — Export discovered places directly to .kml for use in Google My Maps.
- 🌍 **Interactive Folium Map** — Instantly generates an HTML map with markers for all found locations.
- 💌 **Email Integration (Optional)** — Send your travel recommendations or session summary by email.
- ⚙️ **Dynamic Query Understanding** — Handles “top 5,” “best 10,” “show around X city” with automatic result limits.
- 🔐 **Environment-Based Configuration** — All keys and credentials stored securely via .env.


## 🔧 Prerequisites

- Python 3.10 or higher
- A Google Cloud Console project with billing enabled
- A valid Google Maps API key (Geocoding + Places)
- OpenAI API key for GPT model access
- (Optional) Gmail App Password for email sending


## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/EliasKB/TravelMind-AI.git
cd TravelMind-AI
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
# or
source venv/bin/activate    # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Configuration
Create a .env file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password_here
```

### 🧠 How It Works

```mermaid
graph TD;
    A[User Question] --> B[OpenAI Model LangChain];
    B --> C[AI Generates List of Places];
    C --> D[Regex Extracts Names & Addresses];
    D --> E[Google Geocoding API];
    E --> F[Google Places API fallback];
    F --> G[Folium Map Visualization];
    F --> H[KML File Export];
```

## 🗺️ Google Cloud Setup <a name="google-cloud-setup"></a>

Step 1: Create a Project
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one

Step 2: Enable APIs
Go to APIs & Services → Library and enable:
- Geocoding API
- Places API

Step 3: Configure Credentials
1. Navigate to APIs & Services → Credentials
2. Click Create Credentials → API Key
3. Copy your key into .env under GOOGLE_MAPS_API_KEY

Step 4: Enable Billing

Each Google Maps API key must be attached to a billing account —
this ensures requests to the APIs are authorized. At the fist time, you will recieve 300$ dollar for free for the first 90 days.


## 📧 Gmail Setup

1. Enable 2-Factor Authentication on your Google Account
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Create an App Password for “Mail.”
4. Use this password in your `.env` file (not your regular Gmail password)


## 🧪 Testing the APIs
Run the test scripts to confirm API setup:

**Test Google Maps Key**
```bash
python test_googleMapsAPIKey.py
```
If your key prints correctly, it’s valid.

**Test Geocoding & Places**
```bash
python test_geocode_Gplace_API.py
```
✅ You should see valid JSON with "status": "OK".

**Test Gmail Integration**
```bash
python test_gmail_sender.py
```


## 🧩 Usage
Start the Chatbot
```bash
python main.py
```
Then simply type your question:
```vbnet
You: Give me the top 5 temples in Bangkok
```
The bot will:
- Use OpenAI to generate top-rated recommendations
- Fetch accurate coordinates via Google APIs
- Offer commands like:
```pgsql
💡 Type 'map'      → View results on an interactive HTML map  
💡 Type 'export'   → Save locations to pigeon_places.kml  
💡 Type 'email'    → Email the session summary  
💡 Type 'exit'     → Quit the program
```

--------------------


## 🗺️ Google Maps Integration <a name="google-maps-integration"></a>

**🔹 Step 1 — Create Your Custom Map**
1. Go to Google My Maps(https://www.google.com/maps/d/)
2. Click “+ Create a New Map”
3. Rename it (e.g. my_travel_map)
4. Optionally, click “Add layer” to organize your points (e.g. Temples, Beaches, Restaurants)

**🔹 Step 2 — Import Your KML File**

After exporting your .kml file from TravelMind AI:

1. In your My Maps project, click on the layer you want to import into
2. Click “Import”
3. Either:
   - Drag & Drop your exported file (e.g. pigeon_places.kml), or
   - Choose “Select a file from Google Drive” if you’ve uploaded it there
4. Wait a few seconds — your markers will appear on the map
5. You can create multiple layers and import multiple kml files

**🔹 Step 3 — View Your Map in the Google Maps App**

1. Open the Google Maps app on your phone
2. Tap Saved → Maps (or Your places → Maps)
3. You’ll see your custom map (e.g. my_travel_map) under “Maps you’ve created in My Maps”
4. Tap it to open — your custom map loads inside standard Google Maps
5. If location services are enabled, you’ll see your live position relative to your markers

**🔹 Step 4 — Switch Between Custom and Regular Maps**

- To return to the standard Google Map, tap the back arrow or close the custom map tab
- To reopen it, go again to Saved → Maps → my_travel_map

**🔹 Step 5 — Removing or Cleaning Up Your Custom Map**

If you want to remove it later:

1. Visit Google My Maps(https://www.google.com/maps/d/) on desktop
2. Open your map (my_travel_map)
3. You can:
   - Delete individual markers or layers, or
   - Click Menu → Delete map to remove it completely
4. Once deleted, it disappears from your Google Maps app as well

**🔹 Step 6 — Offline Use During Travel**

Before traveling:

1. Open the Google Maps app
2. Go to Offline maps → Select your area (e.g. Thailand) → Download
3. You can now use your custom map offline with all markers visible


## 📁 Project Structure
```
AI-Places-Explorer/
│
├── main.py                     # Chat loop + LangChain/OpenAI integration
├── maps_handler.py              # Google Maps API logic + map generation
├── prompt.py                    # Custom prompt template for location queries
├── gmail_sender.py              # Optional Gmail integration
├── test_geocode_Gplace_API.py   # Test Google Geocoding & Places API responses
├── test_googleMapsAPIKey.py     # Verify .env key loading
├── test_gmail_sender.py         # Test email sending
├── requirements.txt             # Dependencies
├── .env                         # Environment variables (not shared)
└── README.md                    # Project documentation
```

## 🧰 Customization
1. Change OpenAI Model

In main.py, update:
```python
model = ChatOpenAI(
    model="gpt-5",  # or "gpt-4o"
    temperature=0.7,
    api_key=openai_api_key
)
```
3. Change Export Filename
```python
def export_to_kml(self, filename="custom_places.kml"):
```

## 🤝 Contributing

1. Fork this repository
2. Create a new branch (feature-name)
3. Commit your changes
4. Push and submit a Pull Request
Contributions and suggestions are welcome!


<div align="center">
Developed with ❤️ by Elias Kamyab
</div>
