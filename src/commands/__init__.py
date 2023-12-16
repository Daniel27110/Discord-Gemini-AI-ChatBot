import commands.help
import commands.ping


# loads all commands
def load(tree):
    commands.help.load(tree)
    commands.ping.load(tree)
