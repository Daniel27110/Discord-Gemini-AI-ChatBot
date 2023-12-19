import commands.command_utils as command_utils
from discord import app_commands
import ai_chat_api as AI
import errors


# loads the ask command
def load(tree):
    @tree.command(name="ask", description="Ask anything to the bot.")
    @app_commands.describe(question="What would you like to ask?")
    async def ask(interaction, question: str):
        # defer the response
        await interaction.response.defer()

        # tries to get a response from the AI
        try:
            # Generate a response.
            formated_message: str = command_utils.format_message(interaction, question)
            response: str = AI.ask(formated_message)

            await interaction.followup.send(command_utils.clean_response(response))

        except Exception as e:
            print(e)
            # print a random error message from the errors list
            await interaction.followup.send(errors.getRandError())

    print("Loaded app command: ask")
