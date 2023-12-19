# Discord AI Chatbot

A Discord bot capable of AI Chatting using the Google Gemini API


### Commands: 
- Help: shows command list
- Ping: pings the bot and get latency
- Ask: ask any question to the bot without interrupting the conversation in the chat-channel

### Channels:
 - chat-channel: Allows for continuous conversation with the chatbot with lasting message memory

# Installation

Clone the latest version of the project:

```
$ git clone https://github.com/Daniel27110/Discord-AI-ChatBot.git
```

Install the packaging tool [Pipenv](https://pipenv.pypa.io/en/latest/) in order to install all dependancies:

```
$ pip install pipenv
```

Create the Pipenv virtual enviroment and install all dependancies:

```
$ pipenv shell

$ pipenv install
```

Define all your enviromental variables in the src/.env file and run the discord bot:
```
(Discord-Chatbot) $ python src/main.py
```

