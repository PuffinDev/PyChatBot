import os
from dotenv import load_dotenv
from pychatbot.bot import Bot

load_dotenv()

bot = Bot("Example", os.getenv("BOT_PASSWORD"))

@bot.event
def on_message(message):
    message = message["message"]
    
    if message[0] != "!":
        return False
    
    command = message[1:]
    if command == "ping":
        bot.say("Pong!")

bot.run()