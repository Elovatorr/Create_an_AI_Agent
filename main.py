import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import *
from call_function import available_functions

def main():
    load_dotenv()
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    if api_key == "":
        raise RuntimeError("failed to load API key")

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt",type=str,help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)
    user_messages: list[types.Content] = [
        types.Content(role="user",parts=[types.Part(text=args.user_prompt)])
                                     ]

    result = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = user_messages,
        config=types.GenerateContentConfig(Tools=available_functions,system_instruction=system_prompt))

    if result.usage_metadata is None:
        raise RuntimeError("Usage metadata doesn't exist idiot.")

    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {result.usage_metadata.candidates_token_count}")
    if result.function_calls != None:
        for function in result.function_calls:
            print(f"Calling function: {function.name}({function.args})")
    else:
        print(f"result: {result.text}")
main()


