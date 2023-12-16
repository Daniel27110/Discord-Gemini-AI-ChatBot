from . import (
    help,
    ping,
)


# loads all commands
def load(tree):
    help.load(tree)
    ping.load(tree)
