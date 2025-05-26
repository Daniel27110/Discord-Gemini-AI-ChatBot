from dotenv import load_dotenv
import os


# loads the .env file and token
load_dotenv()

# import the bot name
bot_name = os.getenv("BOT_NAME")

# checks if the bot name is None
if bot_name is None:
    raise ValueError("BOT_NAME not found in .env file.")

# import the personality prompt
personality_prompt = os.getenv("PERSONALITY_PROMPT")

# checks if the personality prompt is None
if personality_prompt is None:
    raise ValueError("PERSONALITY_PROMPT not found in .env file.")


# formats the user question to be sent to the AI model
def format_user_question(interaction, message):

    # format = "Hi I'm {username}, {personality_prompt} \n {message}"
    username = interaction.user.nick or interaction.user.name
    introduction = f"Hi I'm {username}, {personality_prompt}"
    formatted_message = f"{introduction} \n {message}"

    return formatted_message


# formats the user message to be sent to the AI model
def format_user_message(message):

    # format = "{username}: {message}"
    username = message.author.display_name or message.author.name
    formatted_message = f"{username}: {message.content}"

    return formatted_message


# cleans the message from the bot's response
def clean_response(response):

    # Removes all text in bold
    response = response.replace("*", "")

    # Remove possible introductions of the form "bot_name:"
    response = response.replace(f"{bot_name}:", "")

    # removes any possible extra spaces
    response = response.strip()

    # removes all emojis
    response = "".join(c for c in response if c.isprintable() and not c.isspace())

    # truncates the response if it is too long
    response = response[:2000]

    return response
