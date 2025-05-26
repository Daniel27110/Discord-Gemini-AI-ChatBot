from dotenv import load_dotenv
import os


# loads the .env file and token
load_dotenv()


# gets the help message from the .env file
helpMessage = os.getenv("HELP_MESSAGE")

# checks if the help message is None
if helpMessage is None:
    raise ValueError("HELP_MESSAGE not found in .env file.")


# loads the help command
def load(tree):

    @tree.command(name="help", description="Get help with the bot's commands")
    async def help(interaction):

        await interaction.response.send_message(helpMessage)

    print("Loaded app command: help")
