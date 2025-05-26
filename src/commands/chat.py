import commands.command_utils as command_utils
from dotenv import load_dotenv
import ai_chat_api as ai_api
import errors
import os


# loads the .env file and token
load_dotenv()


# import the personality prompt
personality_prompt = os.getenv("PERSONALITY_PROMPT")

# checks if the personality prompt is None
if personality_prompt is None:
    raise ValueError("PERSONALITY_PROMPT not found in .env file.")


# loads the ai chat command
def ai_chat(message):

    try:
        # generate a response.
        user_message = command_utils.format_user_message(message)
        response = ai_api.chat(user_message)

        return command_utils.clean_response(response)

    except Exception as e:

        # print the error to the console and return an error message
        print(e)
        return errors.getErrorMessage()


# setup ai chat api
def setup_ai_chat():

    ai_api.setup_ai_chat(personality_prompt)
