import os
from dotenv import load_dotenv, find_dotenv

# Loads environment variables from .env file at the project root
load_dotenv(find_dotenv())

print("Available environment variables:")
for key, value in os.environ.items():
    if "API" in key or "BASE" in key:
        print(f"{key}: {value}")

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")

print(f"API Key loaded: {'Yes' if api_key else 'No'}")
print(f"Base URL loaded: {base_url}")

