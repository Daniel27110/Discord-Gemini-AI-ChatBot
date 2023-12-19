import discord_api.bot_utils as bot_utils
from discord import app_commands
from dotenv import load_dotenv
import commands
import discord
import os

# loads the .env file and token
load_dotenv()

# loads the desired chat channel name from the .env file
chat_channel_name: str | None = os.getenv("CHAT_CHANNEL_NAME")
if chat_channel_name is None:
    print("No chat channel name found in .env file.")

# creates the client, intents, and command tree
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# creates the discord bot using the token from the .env file
def connect():
    # loads the token from the .env file
    token: str | None = os.getenv("DISCORD_TOKEN")
    # runs the client if the token is not None
    if token is not None:
        client.run(token)
    else:
        print("No Discord token found in .env file.")


# runs when the bot is ready
@client.event
async def on_ready():
    # prints a message to the console
    print("Discord bot is running! Starting setup...")

    # runs the on_ready setup function from bot_utils.py
    await bot_utils.on_ready(client, tree)


# continiously checks for new messages to respond to
@client.event
async def on_message(message):
    # if the message was not send in the chat channel, ignore it
    if chat_channel_name != message.channel.name:
        return

    # if the message was send by a bot, ignore it
    if message.author.bot:
        return

    # show the bot is typing
    async with message.channel.typing():
        # get the response from the AI
        response: str = commands.ai_chat(message)
    # send the response to the chat
    await message.channel.send(response)
