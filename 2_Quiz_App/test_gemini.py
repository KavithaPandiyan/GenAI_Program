# Quick test: can Python talk to Gemini?
from dotenv import load_dotenv   # reads the .env file
from google import genai         # Google's Gemini library

load_dotenv()                    # loads GEMINI_API_KEY from .env
client = genai.Client()          # uses the key automatically

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Write 1 multiple-choice quiz question about AI data engineer market trends, with 4 options and the correct answer",
)
print(response.text)