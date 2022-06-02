import os

from pychatbot.bot import Bot

load_dotenv()

bot = Bot("ExampleBot", "example")

@bot.event
def on_message(message):
    message = message["message"]

    if message[0] != "!":
        return False

    command = message[1:]
    if command == "ping":
        bot.say("Pong!")

@bot.event
def on_user_join(message):
    user = message["user"]
    if user != bot.username:
        bot.say(f"Welcome to the server @{user}!")

bot.run()