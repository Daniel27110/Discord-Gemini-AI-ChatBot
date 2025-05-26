import google.generativeai as gemini
from dotenv import load_dotenv
import os


# Load the API key from the .env file.
load_dotenv()


# Configure the API.
key = os.getenv("GOOGLE_API_KEY")

# checks if the key is None
if key is None:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

# Initialize the model and chat log
model = None
chat_log = None


# ask a question to the model.
def ask(question):

    # check if the model is None
    if model is None:
        raise ValueError("AI model is not initialized")

    # generate a response from the model
    response = model.generate_content(question)
    return response.text


# send a new question to the chat log.
def chat(question):

    # check if the model is None
    if model is None:
        raise ValueError("AI model is not initialized")

    # check if the chat log is None
    if chat_log is None:
        raise ValueError("Chat log is not initialized")

    # generate a response from the chat log
    response = chat_log.send_message(question)
    return response.text


# setup ai chat api
def setup_ai_chat(personality_prompt):

    global model
    global chat_log

    # configure the gemini API with the key
    gemini.configure(api_key=key)
    model = gemini.GenerativeModel("gemini-2.0-flash")
    print("AI model loaded successfully.")

    # check if the model is loaded
    if model is None:
        raise ValueError("AI model could not be loaded")

    # start a chat with the model using the personality prompt
    chat_log = model.start_chat(history=[])
    setup_history(personality_prompt)
    print("Bot is ready to chat.")


# starts the chat history using the personality prompt
def setup_history(personality_prompt):

    # sends the personality prompt as the first message in the chat log
    chat(personality_prompt)
