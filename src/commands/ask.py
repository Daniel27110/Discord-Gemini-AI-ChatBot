import commands.command_utils as command_utils
from discord import app_commands
import ai_chat_api as ai_api
import errors


# loads the ask command
def load(tree):

    @tree.command(name="ask", description="Ask anything to the bot.")
    @app_commands.describe(question="What would you like to ask?")
    async def ask(interaction, question: str):

        # defer the interaction response to avoid timeout
        await interaction.response.defer()

        try:

            # generate a response
            user_question = command_utils.format_user_question(interaction, question)
            response = ai_api.ask(user_question)

            await interaction.followup.send(command_utils.clean_response(response))

        except Exception as e:

            # print the error to the console and return an error message
            print(e)
            return errors.getErrorMessage()

    print("Loaded app command: ask")
