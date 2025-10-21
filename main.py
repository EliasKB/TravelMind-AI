from gmail_sender import send_analysis_email, test_gmail
from prompt import get_places_prompt
from maps_handler import MapsHandlerTest
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import re

# Load environment variables (API keys, etc.)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Initialize LLM model (use GPT-4 if available since gpt-4o-mini have low precision)
model = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key=openai_api_key
)

prompt = get_places_prompt()
chain = prompt | model

# Initialize the Google Maps handler
maps_handler = MapsHandlerTest()


def extract_limit_from_question(question):
    """Extract numeric limit (e.g. 'top 5', 'best 10') from the user’s query."""
    match = re.search(r'\b(?:top|best|about|around|recommended|high ranked)?\s*(\d{1,2})\b', question.lower())
    if match:
        return min(int(match.group(1)), 25)  # safety max as 25
    return 10  # default value if user dont specify a number

def handle_conversation( ):
    """Main interactive loop for the AI Places ChatBot."""
    context = ""
    print("=" * 50)
    print("🌍 Welcome to Places AI ChatBot!")
    print("=" * 50)
    print("You can ask about attractions, restaurants, hotels, museums, temples, etc.")
    print("Example: 'What are the top 5 best swimming pools in Gothenburg?'")

    # depending what user types, different actions are taken
    while True:
        print("Type 'exit' to quit.\n")
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Thank you for using ChatBot! Goodbye! 👋")
            break
        
        if user_input.lower() == "locations":
            maps_handler.show_available_locations()
            print()
            continue
        
        if user_input.lower() == "map":
            if maps_handler.locations:
                maps_handler.save_and_open_map()
            else:
                print("ℹ️  No locations on map yet. Ask a question first!\n")
            continue
        
        if user_input.lower() == "export":
            if maps_handler.locations:
                maps_handler.export_to_kml()
            else:
                print("ℹ️ No locations to export. Ask about a place first!\n")
            continue

        if user_input.lower() == "email":
            if test_gmail():
                send_analysis_email(context)
            else:
                print("⚠️ Email sending skipped due to connection issues\n")
            continue

        if not user_input:
            print("Please ask a question to continue.\n")
            continue
        
        print("\n⏳ Fetching recommendations...")

        limit = extract_limit_from_question(user_input)
        response = chain.invoke({"context": context, "question": user_input, "limit": limit})
        result = response.content  

        print("\n🤖 Bot:\n", result)
        print("\n" + "-" * 50 + "\n")
        
        # Update chat context
        context += f"\nUser: {user_input}\nBot: {result}"
        
        # Extract and plot map locations
        print("🗺️  Processing locations for map (TEST MODE)...")
        if maps_handler.add_locations_from_response(result ):
            print("💡 Tip: Type 'map' to view all locations")
            print("💡 Tip: Type 'locations' to see available test locations")
            print("💡 Tip: Type 'export' to export the locations to a file")
            print("💡 Tip: Type 'email' to email the conversation log\n")
        else:
            print("ℹ️  Could not extract locations from response\n")

if __name__ == "__main__":
    handle_conversation( )
