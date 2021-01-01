#!/usr/bin/env python3
"""
BarchBot

https://github.com/Barch-Linux/barchbot
"""


from discord.ext import commands
import json
import os

TOKENS = dict(json.load(open("tokens.json", "r")))

bot = commands.Bot(command_prefix=":b:")

for cog in os.listdir("./cogs"):
    bot.load_extension("cogs.bname")  # cog to add B to usernames


bot.run(TOKENS['DISCORD_BOT_TOKEN'])
