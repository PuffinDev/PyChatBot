# PyChatBot
PyChatBot is a bot client for PyChat.

## Example

This simple bot responds with `Pong!` when a user types the message `!ping`

```py
from pychatbot.bot import Bot

# initialize the bot with username, password, server
# it is best to use a .env file to store your bot password, but for the sake of simplicity it has been left out in this example.
# however, example_bot.py does make use of env
bot = Bot("ExampleBot", "password_goes_here", server=["localhost", 8888])

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
To run the example_bot.py:

- `python3 -m pip install requirements.txt`

- Create a file called .env, and add this line: `BOT_PASSWORD="your_password_here"`

- Change the `server` argument in `example_bot.py` to the server you want your bot to connect to

- `python3 example_bot.py`

