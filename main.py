import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI-Agent")
        print('\nUsage: python main.py "your prompt here"')
        sys.exit(1)
    
    if args[-1] == "--verbose":
        verbose = True
        args = args[:-1]
    else:
        verbose = False
    
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
        )
    
    print(response.text + "\n")
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
