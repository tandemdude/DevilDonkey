# DevilDonkey Bot setup extension coded by github u/tandemdude
# https://github.com/tandemdude
import discord
import json
from discord.ext import commands

with open('config.json') as json_file:
	config = json.load(json_file)


class Setup(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def setup(self, ctx):
		"""Runs first time setup for the bot
		You will be walked through the setup process
		"""
		def check(m):
			# Checks that the message author and channel is the same
			# as the user and channel that invoked the command
			return m.author == ctx.author and m.channel == ctx.channel

		if not config['setup']:
			await ctx.send('Starting bot setup...')

			await ctx.send('Creating role "BotUser" anyone with this role will be able to use the bot commands.')
			await ctx.guild.create_role(name='BotUser')

			# Setting channel for announcements to appear
			await ctx.send('Please tag the channel you wish announcements to appear in.')
			msg = await self.bot.wait_for('message', check=check, timeout=30)
			channel = msg.channel_mentions
			config['announce_ch'] = channel[0].id

			# Setting channel for join/leave messages to appear in
			await ctx.send('Please tag the channel you wish join/leave messages to appear in.')
			msg = await self.bot.wait_for('message', check=check, timeout=30)
			channel = msg.channel_mentions
			config['welcome_ch'] = channel[0].id

			# Setting channel for giveaways to appear in
			await ctx.send('Please tag the channel you wish giveaways to appear in.')
			msg = await self.bot.wait_for('message', check=check, timeout=30)
			channel = msg.channel_mentions
			config['giveaway_ch'] = channel[0].id

			config['setup'] = 1

			with open('config.json', 'w') as file:
				json.dump(config, file)

			await ctx.send('Setup Complete')
		else:
			await ctx.send('Bot has already been set up.')


def setup(bot):
	bot.add_cog(Setup(bot))
