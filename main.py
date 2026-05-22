import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import *
from call_function import available_functions, call_function
import sys

def main():
    load_dotenv()
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("failed to load API key")

    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt",type=str,help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    client = genai.Client(api_key=api_key)
    messages: list[types.Content] = [
        types.Content(role="user",parts=[types.Part(text=args.user_prompt)])
                                     ]
    for i in range(20):
        result = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))
        if result.candidates:
            for candidate in result.candidates:
                messages.append(candidate.content)

        if result.usage_metadata is None:
            raise RuntimeError("Usage metadata doesn't exist.")

        function_results = []

        if result.function_calls:
            for function in result.function_calls:
                function_call_result = call_function(function,args.verbose)
                if not function_call_result.parts:
                    raise Exception("function call result parts empty.")
                if not function_call_result.parts[0].function_response:
                    raise Exception("response is not a FunctionResponse instance.")
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("no response from function.")
                if args.verbose is True:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                function_results.append(function_call_result.parts[0])
            messages.append(types.Content(role="user",parts=function_results))

        else:
            print(f"{result.text}")
            return
    print("maximum iterations reached without a result")
    sys.exit(1)
main()


