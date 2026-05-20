import os
from dotenv import load_dotenv
from google import genai
import argparse



def main():
    load_dotenv()
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("failed to load API key")

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt",type=str,help="User prompt")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)
    result = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = args.user_prompt)
    if result.usage_metadata is None:
        raise RuntimeError("Usage metadata None.")

    print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {result.usage_metadata.candidates_token_count}")
    print(f"response: {result.text}")

main()