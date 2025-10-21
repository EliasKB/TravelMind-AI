# 🎥 Travel Mind AI Agent

**An AI-powered travel and discovery assistant that recommends top-rated places, retrieves precise Google Maps coordinates, and exports them to KML for visualization.**

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Google Cloud Setup](#-Google Cloud Setup)
- [Email Setup](#-Email Setup)
- [Testing the APIs](#-usaTesting the APIsge)
- [Customization](#-Customization)
- [Troubleshooting](#-Troubleshooting)
- [Contributing](#-Contributing)
- [License](#-License)
- [Support](#-Support)


## ✨ Features

- 🤖 **AI-Powered Recommendations** — Uses OpenAI GPT-4o-mini (or GPT-5) to find top attractions restaurants, and hotels worldwide.
- 🗺️ Google Maps Precision — Combines Geocoding API and Places API for highly accurate latitude/longitude.
- 📁 KML Export Support — Export discovered places directly to .kml for use in Google My Maps.
- 🌍 Interactive Folium Map — Instantly generates an HTML map with markers for all found locations.
- 💌 Email Integration (Optional) — Send your travel recommendations or session summary by email.
- ⚙️ Dynamic Query Understanding — Handles “top 5,” “best 10,” “show around X city” with automatic result limits.
- 🔐 Environment-Based Configuration — All keys and credentials stored securely via .env.


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

## ⚙️ Configuration
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password_here
```

### 🧠 How It Works
```mermaid
graph TD
    A[User Question] --> B[OpenAI Model (LangChain)]
    B --> C[AI Generates List of Places]
    C --> D[Regex Extracts Names & Addresses]
    D --> E[Google Geocoding API]
    E --> F[Google Places API (fallback)]
    F --> G[Folium Map Visualization]
    F --> H[KML File Export]
```

## 🗺️ Google Cloud Setup
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
- Query OpenAI for the best recommendations
- Fetch accurate coordinates via Google APIs
- Offer commands like:
```pgsql
💡 Type 'map'      → View results on an interactive HTML map  
💡 Type 'export'   → Save locations to pigeon_places.kml  
💡 Type 'email'    → Email the session summary  
💡 Type 'exit'     → Quit the program
```

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

## 🧪 Testing the APIs
Run the test scripts to confirm API setup:

**Test Google Maps Key*
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





















# 🗺️ AI Places ChatBot with Google Maps Integration

An interactive **AI-powered location recommender** built with **LangChain**, **OpenAI**, and **Google Maps APIs**.  
It suggests attractions, hotels, and landmarks worldwide — then geocodes them using **real Google Maps data** and plots them on a map.

---

## 🧰 Features

- Conversational AI using **LangChain + OpenAI GPT-4o-mini**
- Automatic **address geocoding** and **Places API lookup**
- Generates interactive **Folium maps**
- Exports markers to **KML** for Google My Maps
- Optional **email reporting** of chat logs
- Includes **test scripts** to validate API keys and Google Cloud setup

---

## 🧱 Project Structure

.
├── main.py
├── maps_handler.py
├── prompt.py
├── gmail_sender.py
├── requirements.txt
├── .env
├── test_geocode_Gplace_API.py
├── test_googleMapsAPIKey.py
└── test_gmail_sender.py


---

## ⚙️ Setup Guide

### 1️⃣ Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Click **"Create Project"** → give it a name (e.g. `AI-Places-Bot`).
3. Enable **Billing** (required for Maps API requests).
   - Go to **Billing → Link Billing Account**.
4. Enable the following APIs:
   - **Maps JavaScript API**
   - **Geocoding API**
   - **Places API**
   - **Maps Static API** *(optional)*
5. Generate an **API key**:
   - Navigate to **APIs & Services → Credentials → Create Credentials → API Key**.
   - Restrict usage (optional but recommended) to your project’s APIs.
6. Copy your key and create a `.env` file:

```bash
GOOGLE_MAPS_API_KEY=your_real_api_key_here
OPENAI_API_KEY=your_openai_api_key_here


2️⃣ Create a Python Virtual Environment

python -m venv venv
source venv/bin/activate        # on Linux/macOS
venv\Scripts\activate           # on Windows

pip install -r requirements.txt

3️⃣ Validate Your Setup

Run the following to confirm your environment works:
# 1. Verify Google API key
python test_googleMapsAPIKey.py

# 2. Check Geocoding + Places API
python test_geocode_Gplace_API.py

# 3. Verify Gmail integration (optional)
python test_gmail_sender.py

✅ If you see "status": "OK" from both APIs → your Google Cloud setup is correct.
❌ If you see "REQUEST_DENIED" → check that Billing is enabled and API keys are linked to your project.

4️⃣ Run the ChatBot
python main.py

Example interaction:
🌍 Welcome to Places AI ChatBot (TEST MODE)!
You: give me the top 5 temples in Bangkok
...
💡 Tip: Type 'map' to view all locations
💡 Tip: Type 'export' to export as KML
💡 Tip: Type 'email' to email the conversation log


5️⃣ Optional: Export and View on Google Maps

1. Type export in the chatbot → generates pigeon_places.kml.
2. Visit Google My Maps: https://www.google.com/maps/d/
3. Create a new map → click Import → select the KML file.
4. Your AI-recommended locations will appear as markers.

🧪 Test Scripts Included
| File                         | Purpose                                            |
| ---------------------------- | -------------------------------------------------- |
| `test_googleMapsAPIKey.py`   | Checks if your API key is loaded correctly         |
| `test_geocode_Gplace_API.py` | Confirms Geocoding + Places APIs return valid data |
| `test_gmail_sender.py`       | Tests Gmail connection & email sending             |
| `.env`                       | Stores private API keys                            |
