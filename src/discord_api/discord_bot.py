import discord_api.bot_utils as bot_utils
from discord import app_commands
from dotenv import load_dotenv
import commands
import discord
import os


# loads the .env file and token
load_dotenv()


# loads the chat channel name from the .env file
chat_channel = os.getenv("CHAT_CHANNEL_NAME")

# if the chat channel name is not found, print an error message
if chat_channel is None:
    raise ValueError("CHAT_CHANNEL_NAME not found in .env file.")


# creates the client, intents, and command tree
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# connects the bot to Discord using the token from the .env file
def connect():

    # loads the token from the .env file
    token = os.getenv("DISCORD_TOKEN")

    # checks if the token is None
    if token is None:
        raise ValueError("DISCORD_TOKEN not found in .env file.")

    # runs the bot with the token
    client.run(token, log_handler=None)


# runs when the bot is ready
@client.event
async def on_ready():

    # prints a message to the console
    print("Discord bot is running!")
    print("------")

    # sets the bot's status and loads the commands
    await bot_utils.on_ready(client, tree)


# continuously checks for new messages to respond to
@client.event
async def on_message(message):

    # if the message was not send in the chat channel, ignore it
    if message.channel.name != chat_channel:
        return

    # if the message was send by a bot, ignore it
    if message.author.bot:
        return

    # show the bot is typing
    async with message.channel.typing():

        # get the response from the AI
        response = commands.ai_chat(message)

    # send the response to the chat
    await message.channel.send(response)
