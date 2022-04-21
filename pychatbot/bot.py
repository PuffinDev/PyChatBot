import socket
import json
from threading import Thread
from random import choice
from hashlib import sha256

from .networking import receive, send_message, send_command

class Bot:
    def __init__(self, username, password, server=["puffindev.xyz", 8888]):
        self.send_command = send_command
        self.send_message = send_message

        self.server_address = server
        self.username = username
        self.password = sha256(password.encode()).hexdigest()
    
    def run(self):
        self.init_socket()
    
    def event(self, method):
        setattr(self, method.__name__, method)

    def init_socket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(tuple(self.server_address))

        send_command(self.s, {"command": "login", "username": self.username, "password": self.password, "manual_call": False})

        self.receive_loop()

    def say(self, message):
        self.send_message(self.s, message)

    def receive_loop(self):
        while True:
            try:
                messages = receive(self.s)
            except OSError:
                return False
            except KeyboardInterrupt:
                exit()
                
            if not messages:
                continue

            for msg in messages:
                if msg == None:
                    continue

                if msg["command"] == "message":
                    self.on_message(msg)

                elif msg["command"] == "banned":
                    print("Bot has been banned")
                
                elif msg["command"] == "kicked":
                    print("Bot has been kicked")
                
                elif msg["command"] == "login_result":
                    if msg["result"] not in ["success", "account_created"]:
                        raise Exception("Authentication error")
