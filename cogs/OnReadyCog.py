# On ready listener extension coded by github u/tandemdude
# https://github.com/tandemdude
import discord
import json
from discord.ext import commands

with open('config.json') as json_file:
    config = json.load(json_file)


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('The bot is ready!')
        await self.bot.change_presence(activity=discord.Game(name=f'{config["prefix"]}help'))


def setup(bot):
    bot.add_cog(OnReady(bot))