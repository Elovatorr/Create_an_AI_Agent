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
if result.usage_metadata is None:
    raise RuntimeError("Usage metadata None.")

print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
print(f"response tokens: {result.usage_metadata.candidates_token_count}")
print(f"response: {result.text}")
