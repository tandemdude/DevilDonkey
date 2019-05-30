# Bot owner commands extension made by github u/tandemdude
# https://github.com/tandemdude
from discord.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.is_owner()
	async def kill(self, ctx):
		await ctx.send('Bot logging out.')
		await self.bot.logout


def setup(bot):
	bot.add_cog(Owner(bot))