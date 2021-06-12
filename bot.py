import discord
import re
from translate import *
import config

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


async def get_online_users():
    return ['abc', 'efg', 'hij', 'klm']

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!help'):
        await message.channel.send('just type lul')
    elif message.content.startswith('!online'):
        users = await get_online_users()

        out = ""
        for i, user in enumerate(users):
            out += str(i) + ". " + user + "\n"

        embed = discord.Embed(
            title = "Currently Online",
            thumbnail="https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F22%2Fb7%2F3d%2F22b73ddfc4cbe22a4a6a4799bb37488b.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F797840890237780980%2F&tbnid=DYf3laN9ggHabM&vet=12ahUKEwjmiorEvZLxAhXOSawKHQ3VDq4QMygBegUIARDWAQ..i&docid=XZVKok964gm7RM&w=750&h=1000&itg=1&q=mike%20wazowski%20meme&ved=2ahUKEwjmiorEvZLxAhXOSawKHQ3VDq4QMygBegUIARDWAQ",
            footer="https://github.com/Surfs-Up/MorseBot",
            description=out
        )

        await message.channel.send(embed=embed)
    else:
        if re.search('^[.-]*$', message.content):
            await message.channel.send(morseToEng(message.content))
        else:
            await message.channel.send(engToMorse(message.content))
            

    #if message.content.startswith('')
client.run(config.TOKEN)