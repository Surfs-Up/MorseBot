import discord
import re
from translate import *
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    #await channel.send("hello")
    channel = bot.get_channel(853131344581099523)
    print(channel)
    await channel.send("lul")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!"):
        pass
    else:
        if re.search('.' and '-', message.content):
            await message.channel.send(morseToEng(message.content))
        else:
            await message.channel.send(engToMorse(message.content))
    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    await ctx.channel.send('just type lul')

@bot.command()
async def link(ctx):
    embed = discord.Embed(
        title = "github link",
        url = "https://github.com/Surfs-Up/MorseBot"
        #thumbnail="https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F22%2Fb7%2F3d%2F22b73ddfc4cbe22a4a6a4799bb37488b.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F797840890237780980%2F&tbnid=DYf3laN9ggHabM&vet=12ahUKEwjmiorEvZLxAhXOSawKHQ3VDq4QMygBegUIARDWAQ..i&docid=XZVKok964gm7RM&w=750&h=1000&itg=1&q=mike%20wazowski%20meme&ved=2ahUKEwjmiorEvZLxAhXOSawKHQ3VDq4QMygBegUIARDWAQ"
    )
    await ctx.channel.send(embed=embed)

bot.run(config.TOKEN)