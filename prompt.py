from langchain_core.prompts import ChatPromptTemplate

# Template guiding the AI to produce structured, map-friendly results.
PLACES_PROMPT_TEMPLATE = """
You are an expert at recommending attractions, restaurants, hotels, beaches, museums, landmarks worldwide, and etc.

Conversation history: {context}
User question: {question}

INSTRUCTIONS:
- If the question is about a location, respond with up to {limit} of the most relevant and popular places.
- Each item must include:
  1. The **exact Google Maps name** of the place (as it appears on maps.google.com)
  2. Category (e.g., Temple, Museum, Beach, Restaurant)
  3. A brief 1–2 sentence description
  4. The **full, searchable address** (street number, area, city, country)
  5. Do **not** include latitude/longitude coordinates in your response.

Formatting (strict):
  1. [NAME] - [CATEGORY]
     Description: [text]
     Address/Area: [Full address]

Extra guidance:
- Use Google Maps naming conventions and include any special identifiers (e.g. “Wat Saket (The Golden Mount)”).
- Always include country and postal code when known.
- Do not use generic areas (like “Phra Nakhon”), use exact street-level addresses.
- Do not invent coordinates — use real or realistic coordinates close to the true Google Maps location.
- Prefer **landmarks or businesses that have a verified Google Maps listing**.
- If uncertain, specify both the local name and English name (e.g., “Wat Saket (วัดสระเกศราชวรมหาวิหาร)”).

Answer:
"""

def get_places_prompt():
    """Returns a ChatPromptTemplate for location-based searches"""
    return ChatPromptTemplate.from_template(PLACES_PROMPT_TEMPLATE)

