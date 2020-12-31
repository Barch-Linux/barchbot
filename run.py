from discord.ext import commands
import discord
import json
import os

TOKENS = dict(json.load(open("tokens.json", "r")))

bot = commands.Bot(command_prefix=":b:")

for cog in os.listdir("./cogs"):
    bot.load_extension(f"cogs.{cog[:-3]}")


bot.run(TOKENS['DISCORD_BOT_TOKEN'])