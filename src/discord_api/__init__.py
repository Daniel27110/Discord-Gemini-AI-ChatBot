import discord
from discord import app_commands
from dotenv import load_dotenv
import commands
import os

# loads the .env file and token
load_dotenv()

# loads the desired chat channel name from the .env file
chat_channel_name = os.getenv("CHAT_CHANNEL_NAME")
if chat_channel_name is None:
    print("No chat channel name found in .env file.")

# creates the client, intents, and command tree
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# creates the discord bot using the token from the .env file
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
    await load_commands()

    # syncs the bot's application commands
    await sync_commands()

    # setup ai chat api
    await setup_ai_chat()


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
        response = commands.chat(message)
        # send the response to the chat
    await message.channel.send(response)


async def change_status(client: discord.Client):
    # loads the bot's status from the .env file
    status = os.getenv("DISCORD_STATUS")

    # changes the bot's status
    if status is not None:
        activity = discord.Activity(type=discord.ActivityType.watching, name=status)
        await client.change_presence(activity=activity)
    else:
        print("No Discord status found in .env file.")


async def load_commands():
    commands.load(tree)


async def sync_commands():
    await tree.sync()
    print("Synced application commands.")


async def setup_ai_chat():
    commands.setup_ai_chat()
