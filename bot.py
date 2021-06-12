import discord
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
        await message.channel.send('`"!m->" will turn a message from morse code to english \n "!->m" will turn a message from english to morse code`')

    if message.content.startswith('.' or '-'):
        await message.channel.send(engToMorse(message.content))
    else:
        await message.channel.send(engToMorse(message.content))

    #if message.content.startswith('')
client.run("ODUzMTMwODA0NTUzMDU2MjY2.YMQ5-g.8RNnNxU4vudRrfX8Dkr2nyAJQf8")
