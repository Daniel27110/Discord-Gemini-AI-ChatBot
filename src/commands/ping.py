def load(tree):

    @tree.command(name="ping", description="Checks the bot's latency.")
    async def ping(interaction):

        latency = round(tree.client.latency * 1000)
        await interaction.response.send_message(f"Hi! My latency is {latency}ms.")

    print("Loaded app command: ping")
