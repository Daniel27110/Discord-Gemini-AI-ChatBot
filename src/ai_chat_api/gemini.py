import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the API key from the .env file.
load_dotenv()

# Configure the API.
key: str | None = os.getenv("GOOGLE_API_KEY")
model = None
chat_log = None


# Ask a single question to the model.
def ask(question):
    # checks if the model is not None
    if model is not None:
        response = model.generate_content(question)
        return response.text
    else:
        return "No AI model found, please try again later."


# chat with the model
def chat(question):
    # checks if the model and chat are not None
    if model is not None and chat_log is not None:
        response = chat_log.send_message(question)
        return response.text
    else:
        return "No AI model found, please try again later."


# setup ai chat api
def setup_ai_chat(personality_prompt: str):
    global model
    global chat_log
    # Create the model.
    if key is not None:
        genai.configure(api_key=key)
        model = genai.GenerativeModel("gemini-pro")
        print("AI model loaded successfully.")
    else:
        print("No Google API key found in .env file.")

    # generate the long term chat
    if model is not None:
        chat_log = model.start_chat(history=[])
        setup_history(personality_prompt)
        print("Bot is ready to chat.")
    else:
        print("No AI model was found.")


# starts the chat history using the personality prompt
def setup_history(personality_prompt: str):
    # uses the chat function to start the chat history
    chat(personality_prompt)
