from discord import app_commands
from dotenv import load_dotenv
from errors import getErrorMessages
import ai_chat_api.palm as palm
import random
import os


# loads the .env file and token
load_dotenv()

# import the personality prompt
personality_prompt: str | None = os.getenv("PERSONALITY_PROMPT")

# import error messages
errors: list[str] = getErrorMessages()


# creates the chat message in the apropiate format
def format_message(interaction, message: str):
    # format = "Hi I'm {username}, {personality_prompt} \n {message}"
    username: str = interaction.user.nick or interaction.user.name
    introduction: str = f"Hi I'm {username}, {personality_prompt}"
    formated_message: str = f"{introduction} \n {message}"

    return formated_message


# cleans the message from the bot's response
def clean_response(response: str) -> str:
    # if the message has over 2000 characters, it will be cut
    # and the last 3 characters will be replaced with "..."
    if len(response) > 2000:
        response = response[:1997] + "..."

    return response


# loads the chat command
def load(tree):
    @tree.command(name="chat", description="Single message chat command.")
    @app_commands.describe(message="Your message.")
    async def chat(interaction, message: str):
        # defer the response
        await interaction.response.defer()

        # tries to get the message
        try:
            # Generate a response.
            formated_message: str = format_message(interaction, message)
            response: str = palm.ask(formated_message)

            await interaction.followup.send(clean_response(response))

        except Exception as e:
            print(e)
            # print a random error message from the errors list
            await interaction.followup.send(random.choice(errors))

    print("Loaded app command: chat")
