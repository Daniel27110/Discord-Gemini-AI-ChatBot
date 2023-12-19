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

    # setup ai chat api
    await setup_ai_chat()


# changes the bot's status
async def change_status(client: discord.Client):
    # loads the bot's status from the .env file
    status: str | None = os.getenv("DISCORD_STATUS")

    # changes the bot's status
    if status is not None:
        activity = discord.Activity(type=discord.ActivityType.watching, name=status)
        await client.change_presence(activity=activity)
    else:
        print("No Discord status found in .env file.")


# loads the bot's application commands
async def load_commands(tree):
    commands.load(tree)


# syncs the bot's application commands
async def sync_commands(tree):
    await tree.sync()
    print("Synced application commands.")


# setup ai chat api
async def setup_ai_chat():
    commands.setup_ai_chat()
