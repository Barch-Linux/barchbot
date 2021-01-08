#!/usr/bin/env python3
"""
BarchBot

https://github.com/Barch-Linux/barchbot
"""


import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(module)s %(levelname)s\t - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
#logging.basicConfig(level=logging.DEBUG,
                    #format="%(module)s:%(levelname)s: %(message)s")

from discord.ext import commands
import settings

bot = commands.Bot(command_prefix="b!")

extensions = [
    "bname",
]

logger.info(f"Loading {len(extensions)} extensions")
for ext in extensions:
    bot.load_extension(f"cogs.{ext}")
    logger.debug(f"  Loaded: {ext}")


@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user}")

bot.run(settings.TOKEN)
