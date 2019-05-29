# Purge extension coded by github u/tandemdude
# https://github.com/tandemdude
import discord
from discord.ext import commands


class Purge(commands.Cog):

	@commands.command()
	@commands.has_role('BotUser')
	async def purge(self, ctx, param: int):
		"""Purges x messages from the channel, format !purge x
		"""
		count = min(param+1, 100)
		deleted = await ctx.channel.purge(limit=count)
		embed = discord.Embed(title=f'Deleted **{len(deleted)-1}** messages', description=f'☑ Requested by {ctx.author.display_name}', color=0x00ff00)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Purge())
