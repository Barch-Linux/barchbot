#!/usr/bin/env python3
"""
BarchBot

https://github.com/Barch-Linux/barchbot
"""


from discord.ext import commands
import json

TOKENS = dict(json.load(open("tokens.json", "r")))

bot = commands.Bot(command_prefix=":b:")

cogs = [
    "bname",
]  # list of cogs

for cog in cogs:
    bot.load_extension(f"cogs.{cog}")  # load the cog


bot.run(TOKENS['DISCORD_BOT_TOKEN'])
