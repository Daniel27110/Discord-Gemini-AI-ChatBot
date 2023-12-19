import ai_chat_api.gemini as gemini

# the desired generative ai is imported here


# ask the ai a question
def ask(question):
    return gemini.ask(question)


# chat with the ai
def chat(message):
    return gemini.chat(message)


# setup ai chat api
def setup_ai_chat(personality_prompt: str):
    gemini.setup_ai_chat(personality_prompt)
