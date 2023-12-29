# Discord AI Chatbot

A Discord bot capable of AI Chatting using the Google Gemini API.

This project can be used as a standalone bot or be used as a template for constructing more elaborate discord bots.


### Commands: 
- **Help:** shows the command list.
- **Ping:** pings the bot and gets latency.
- **Ask:** ask any question to the bot without interrupting the conversation in the chat-channel.


### Channels:
- **Chat-channel:** Allows for continuous conversation with the chatbot with lasting message memory.

  
# Installation

Clone the latest version of the project:

```bash
$ git clone https://github.com/Daniel27110/Discord-AI-ChatBot.git
```

Install the packaging tool [Pipenv](https://pipenv.pypa.io/en/latest/) in order to install all dependancies:

```bash
$ pip install pipenv
```

Create the Pipenv virtual enviroment and install all dependancies:

```bash
$ pipenv shell

$ pipenv install
```

Define all your enviromental variables in the '**src/.env**' file as shown in '**src/.env_sample**', then run the discord bot:

```bash
(Discord-Chatbot) $ python src/main.py
```

Alternatively, run the discord bot using pipenv directly:

```bash
$ pipenv run python src/main.py
```

