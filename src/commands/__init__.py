import commands.help
import commands.ping
import commands.chat
import commands.ask


# loads all commands
def load(tree):
    commands.help.load(tree)
    commands.ping.load(tree)
    commands.ask.load(tree)


# chat with the model
def ai_chat(message):
    return commands.chat.ai_chat(message)


# setup ai chat api
def setup_ai_chat():
    commands.chat.setup_ai_chat()
