import os
from dotenv import load_dotenv

load_dotenv()
api_key: str | None = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("failed to load API key")

from google import genai

client = genai.Client(api_key=api_key)
result = client.models.generate_content(
model = "gemini-2.5-flash",
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
# print(f"Prompt tokens: {ptkens}")
print(result.text)
