
import asyncio
import time
import threading

from bot import MorseBot
from server import Server
import config

def start_server():
    server = Server()
    server.start_server()

threading.Thread(target=start_server).start()

bot = MorseBot()
bot.run(config.TOKEN)

