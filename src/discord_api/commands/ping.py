from discord import app_commands

from discord_api import tree


@tree.command(name="ping", description="Pings the bot.")
async def ping(interaction):
    latency = round(tree.client.latency * 1000)
    await interaction.response.send_message(f"Hi! My latency is {latency}ms.")


print("Loaded app command: ping")
