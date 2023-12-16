from discord import app_commands
from dotenv import load_dotenv
import os

# loads the .env file and token
load_dotenv()

# gets the help message from the .env file
helpMessage = os.getenv("HELP_MESSAGE")


# loads the help command
def load(tree):
    @tree.command(name="help", description="Shows all available commands.")
    async def help(interaction):
        await interaction.response.send_message(helpMessage)

    print("Loaded app command: help")
