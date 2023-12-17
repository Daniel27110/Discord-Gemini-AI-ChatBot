import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from the .env file.
load_dotenv()

# Configure the API.
key = os.getenv("GOOGLE_API_KEY")

# Create the model.
if key is not None:
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-pro")
else:
    print("No Google API key found in .env file.")


# Ask a question to the model.
def ask(question):
    # checks if the model is not None
    if model is not None:
        response = model.generate_content(question)
        return response.text
    else:
        return "No AI model found, please try again later."
