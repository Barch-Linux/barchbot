import discord
from discord.ext import commands


class Bname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print("editing member")
        await member.edit(nick=f":b:{member.nick[1:]}")
"""
barch
"""


def setup(bot):
    bot.add_cog(Bname(bot))
