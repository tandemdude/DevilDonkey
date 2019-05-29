# Announcements extension coded by github u/tandemdude
# https://github.com/tandemdude
import json
import discord
from discord.ext import commands


class Announcements(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_role('BotUser')
	async def announce(self, ctx):
		"""Sends an announcement to the channel specified during setup
		The bot will walk you through the announcement, just run !announce
		"""
		with open('config.json') as json_file:
			config = json.load(json_file)

		announcement_channel_id = config['announce_ch']
		await ctx.send('Please type the announcement title.')
		title = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
		await ctx.send('Please enter the announcement text.')
		announcement = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
		a = discord.Embed(title=title.content.title(), description=announcement.content, color=0xde2bea)
		announcement_channel = self.bot.get_channel(announcement_channel_id)
		await announcement_channel.send('@everyone')
		await announcement_channel.send(embed=a)


def setup(bot):
	bot.add_cog(Announcements(bot))
