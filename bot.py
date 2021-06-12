import discord
import re
from translate import *

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('just type lul')
    else:
        if re.search('[a-z0-9_]', message.content):
            await message.channel.send(engToMorse(message.content))
        else:
            await message.channel.send(morseToEng(message.content))

    #if message.content.startswith('')
client.run("TOKEN")