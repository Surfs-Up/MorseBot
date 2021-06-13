import discord
import re
from translate import *
from discord.ext import commands
import config

class MorseBot(commands.Bot):

    PREFIX='!'

    def __init__(self):
        commands.Bot.__init__(self, command_prefix=MorseBot.PREFIX)

        self.channel = None
        # bot.remove_command("help")

    async def on_ready(self):
        self.channel = self.get_channel(config.CHANNEL)
        print('MorseBot is now online')

    async def on_message(self, message):
        if message.author.bot:
            return

        if re.search('.' and '-', message.content):
            await message.channel.send(morseToEng(message.content))
        else:
            await message.channel.send(engToMorse(message.content))

    async def send_letter(self, letter):
        await self.channel.send(letter)

    def add_commands(self):
        # @self.commands(name=""
        pass

# @bot.event
# async def on_ready(self):
#     print(f'{bot.user.name} has connected to Discord!')
#     self.channel = bot.get_channel(853131344581099523)
#     print(channel)
#     await channel.send("lul")

# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return
#     if message.content.startswith("!"):
#         pass
#     else:
#         if re.search('.' and '-', message.content):
#             await message.channel.send(morseToEng(message.content))
#         else:
#             await message.channel.send(engToMorse(message.content))
#     await bot.process_commands(message)

# @bot.command()
# async def help(ctx):
#     await ctx.channel.send('just type lul')

# @bot.command()
# async def link(ctx):
#     embed = discord.Embed(
#         title = "github link",
#         url = "https://github.com/Surfs-Up/MorseBot"
#     )
#     await ctx.channel.send(embed=embed)

# bot = MorseBot()
# bot.run(config.TOKEN)

