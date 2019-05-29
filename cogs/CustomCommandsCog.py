# Custom Commands extension made by github u/tandemdude
# https://github.com/tandemdude
from discord.ext import commands


class CustomCommands(commands.Cog):

    @commands.command()
    async def website(self, ctx):
        await ctx.send('**Your URL Here**')

    @commands.command()
    async def ip(self, ctx):
    	await ctx.send('**Your Server IP Here**')

def setup(bot):
    bot.add_cog(CustomCommands())