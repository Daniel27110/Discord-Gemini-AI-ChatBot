import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from the .env file.
load_dotenv()

# Configure the API.
key = os.environ["GOOGLE_API_KEY"]

# Create the model.
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-pro")


# Ask a question to the model.
def ask(question):
    response = model.generate_content(question)
    return response.text
