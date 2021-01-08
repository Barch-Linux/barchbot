#!/usr/bin/env python3
"""
bname.py

Automatically change the first letter of new
members' nicknames to a B emoji.
"""


import discord
from discord.ext import commands



@commands.command()
async def hello(ctx):
    await ctx.send(f"Hello there, {ctx.author}")


class Bname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print("editing member")
        await member.edit(nick=f":b:{member.nick[1:]}")


def setup(bot):
    bot.add_command(hello)
    #bot.add_cog(Bname)
