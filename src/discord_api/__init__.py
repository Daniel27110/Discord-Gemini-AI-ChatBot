import discord
from discord import app_commands
from dotenv import load_dotenv
from threading import Thread
import os

# loads the .env file and token
load_dotenv()

# creates the client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def connect():
    # loads the token from the .env file
    token = os.getenv("DISCORD_TOKEN")

    # runs the client
    client.run(token)


@client.event
async def on_ready():
    # prints a message to the console
    print("Discord bot is running!")

    # changes the bot's status
    await change_status(client)

    # loads the bot's application commands
    await load_commands()


async def change_status(client):
    # loads the bot's status from the .env file
    status = os.getenv("DISCORD_STATUS")

    activity = discord.Activity(type=discord.ActivityType.listening, name=status)
    await client.change_presence(activity=activity)


async def load_commands():
    import discord_api.commands
