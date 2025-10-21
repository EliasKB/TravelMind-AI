import os
from dotenv import load_dotenv


# Simple test to confirm your GOOGLE_MAPS_API_KEY is loaded
load_dotenv()
print(os.getenv("GOOGLE_MAPS_API_KEY"))

# If nothing prints, your .env file or environment variable is misconfigured.