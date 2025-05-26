import discord
import commands
import os


# setup bot status and commands
async def on_ready(client, tree):

    # changes the bot's status
    await change_status(client)

    # loads the bot's application commands
    await load_commands(tree)

    # syncs the bot's application commands
    await sync_commands(tree)

    # prints a message to the console
    print("Loaded all commands and changed status!")
    print("------")

    # setup ai chat api
    await setup_ai_chat()


# changes the bot's status
async def change_status(client: discord.Client):

    # loads the bot's status from the .env file
    status = os.getenv("DISCORD_STATUS")

    # checks if the status is None
    if status is None:
        raise ValueError("DISCORD_STATUS not found in .env file.")

    # sets the bot's status
    activity = discord.Activity(type=discord.ActivityType.watching, name=status)
    await client.change_presence(activity=activity)


# loads the bot's application commands
async def load_commands(tree):
    commands.load(tree)


# syncs the bot's application commands
async def sync_commands(tree):
    await tree.sync()


# setup ai chat api
async def setup_ai_chat():
    commands.setup_ai_chat()
