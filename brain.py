import os
import sys
from google import genai

API_KEY = ""

def main():

    if len(sys.argv) < 2:
        print("Usage: python# brain.py 'Your question here'")
        sys.exit()

    user_query = " ".join(sys.argv[1:]) 

    print(f"\nThinking about: {user_query}...\n")

    try:
        client = genai.Client(api_key = API_KEY)
        response = client.models.generate_content(
            model = 'gemini-flash-latest',
            contents = user_query
        )

        print("-------------------------")
        print(response.text)
        print("-------------------------")

    except Exception as e:
        print("An error occurred while generating the response:")
        print(e)

if __name__ == "__main__":
    main()
