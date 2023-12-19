import commands.help
import commands.ping
import commands.ask


# loads all commands
def load(tree):
    commands.help.load(tree)
    commands.ping.load(tree)
    commands.ask.load(tree)


# chat with the model
def chat(message):
    return commands.ask.chat(message)


# setup ai chat api
def setup_ai_chat():
    commands.ask.setup_ai_chat()
