# PyChatBot
PyChatBot is a bot client for PyChat.

## Example

This bot responds with `Pong!` when a user types the message `!ping`

```py
import os
from dotenv import load_dotenv
from pychatbot.bot import Bot

load_dotenv()

bot = Bot("Example", os.getenv("BOT_PASSWORD"))

@bot.event
def on_message(message):
    if message[0] != "!":
        return False
    
    command = message[1:]
    if command == "ping":
        bot.say("Pong!")

bot.run()
```


## Usage
To run the example:

- `python3 -m pip install requirements.txt`

- Create a file called .env, and add thisline: `BOT_PASSWORD="switch_to_your_password"`

- `python3 example_bot.py`

