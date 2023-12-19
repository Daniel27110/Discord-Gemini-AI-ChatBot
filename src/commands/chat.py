import commands.command_utils as command_utils
from dotenv import load_dotenv
import ai_chat_api as AI
import errors
import os

# loads the .env file and token
load_dotenv()


# import the personality prompt
personality_prompt: str | None = os.getenv("PERSONALITY_PROMPT")
if personality_prompt is None:
    print("No personality prompt found in .env file.")


# chatting with the model
def ai_chat(message):
    # tries to get a response from the AI
    try:
        # Generate a response.
        username: str = message.author.display_name or message.author.name
        chat_messaege: str = f"{username}: {message.content}"
        response: str = AI.chat(chat_messaege)

        return command_utils.clean_response(response)

    except Exception as e:
        print(e)
        # print a random error message from the errors list
        return errors.getRandError()


# setup ai chat api
def setup_ai_chat():
    if personality_prompt is not None:
        AI.setup_ai_chat(personality_prompt)
    else:
        print("Could not setup AI chat, no personality prompt found in .env file.")
