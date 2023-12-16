from discord import app_commands
from dotenv import load_dotenv
import os

import ai_chat_api.palm as palm

# loads the .env file and token
load_dotenv()

# TODO: import personality prompt from .env file


# loads the chat command
def load(tree):
    @tree.command(name="chat", description="Single message chat command.")
    @app_commands.describe(message="Your message.")
    async def chat(interaction, message: str):
        await interaction.response.defer()
        # Generate a response.
        response = palm.ask(message)

        print(response)

        await interaction.followup.send(response)

    print("Loaded app command: chat")
