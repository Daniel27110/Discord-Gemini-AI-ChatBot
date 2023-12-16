import commands.help
import commands.ping
import commands.chat


# loads all commands
def load(tree):
    commands.help.load(tree)
    commands.ping.load(tree)
    commands.chat.load(tree)
