# Commands extension made by github u/tandemdude
# https://github.com/tandemdude
from discord.ext import commands
import random

possible_responses = ['It is certain', 'It is decidely so', 'Without a doubt', 'Yes - definitely',
						'you may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
						'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later',
						'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
						"Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good',
						'Very doubtful']


class CustomCommands(commands.Cog):

    @commands.command()
    async def website(self, ctx):
        await ctx.send('**Your URL Here**')

    @commands.command()
    async def ip(self, ctx):
    	await ctx.send('**Your Server IP Here**')

    @commands.command(name='8ball')
    async def eightball(self, ctx):
    	await ctx.send(f'🎱 {random.choice(possible_responses)}')

def setup(bot):
    bot.add_cog(CustomCommands())