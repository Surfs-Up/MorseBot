
import asyncio
import time

from bot import MorseBot
from server import Server
import config

IP = "localhost"
PORT = 5050

loop = asyncio.get_event_loop()

morse_server = Server(IP, PORT)
morse_bot = MorseBot()

asyncio.ensure_future(morse_server.server)
asyncio.ensure_future(morse_bot.run(config.TOKEN))
loop.run_forever()

