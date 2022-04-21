# PyChatBot
PyChatBot is a bot client for PyChat.

## Example

This simple bot responds with `Pong!` when a user types the message `!ping`

```py
from pychatbot.bot import Bot

# initialize the bot with username, password, server
bot = Bot("ExampleBot", "BOT_PASSWORD", server=["localhost", 8888])

# handle on_message event
@bot.event
def on_message(message):
    message = message["message"]

    # respond to a user typing !ping
    if message == "!ping":
        bot.say("Pong!")

bot.run()
```


## Usage
To run the example:

- `python3 -m pip install requirements.txt`

- Create a file called .env, and add thisline: `BOT_PASSWORD="switch_to_your_password"`

- Change the `server` argument in `example_bot.py` to the server you want your bot to connect to

- `python3 example_bot.py`

