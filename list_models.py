from google import genai

API_KEY = ""

client = genai.Client(api_key=API_KEY)

print("--- STARTING MODEL SCAN ---")
try:
    # We loop through whatever the server sends back
    for m in client.models.list():
        # We print the 'name' attribute directly
        print(f"Model: {m.name}")
except Exception as e:
    print(f"Error: {e}")
print("--- SCAN COMPLETE ---")