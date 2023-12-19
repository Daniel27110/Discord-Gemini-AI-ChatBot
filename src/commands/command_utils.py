from dotenv import load_dotenv
import os

# loads the .env file and token
load_dotenv()

# import the bot name
bot_name: str | None = os.getenv("BOT_NAME")
if bot_name is None:
    print("No bot name found in .env file.")

# import the personality prompt
personality_prompt: str | None = os.getenv("PERSONALITY_PROMPT")
if personality_prompt is None:
    print("No personality prompt found in .env file.")


# creates the chat message in the apropiate format
def format_message(interaction, message: str):
    # format = "Hi I'm {username}, {personality_prompt} \n {message}"
    username: str = interaction.user.nick or interaction.user.name
    introduction: str = f"Hi I'm {username}, {personality_prompt}"
    formated_message: str = f"{introduction} \n {message}"

    return formated_message


# cleans the message from the bot's response
def clean_response(response: str) -> str:
    # Remove possible introductions in the form "bot_name: "
    response = response.replace(f"{bot_name}: ", "")

    # if the message has over 2000 characters, it will be cut
    # and the last 3 characters will be replaced with "..."
    if len(response) > 2000:
        response = response[:1997] + "..."

    return response
