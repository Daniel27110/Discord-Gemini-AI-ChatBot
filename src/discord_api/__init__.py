import discord
from discord import app_commands
from dotenv import load_dotenv
import discord_api.commands
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
    # runs the client if the token is not None
    if token is not None:
        client.run(token)
    else:
        print("No Discord token found in .env file.")


@client.event
async def on_ready():
    # prints a message to the console
    print("Discord bot is running!")

    # changes the bot's status
    await change_status(client)

    # loads the bot's application commands
    load_commands()

    # syncs the bot's application commands
    await sync_commands()


async def change_status(client: discord.Client):
    # loads the bot's status from the .env file
    status = os.getenv("DISCORD_STATUS")

    activity = discord.Activity(type=discord.ActivityType.watching, name=status)
    await client.change_presence(activity=activity)


def load_commands():
    discord_api.commands.load(tree)


async def sync_commands():
    await tree.sync()
    print("Synced application commands.")
