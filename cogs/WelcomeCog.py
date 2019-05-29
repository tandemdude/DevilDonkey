# User welcome extension coded by github u/tandemdude
# https://github.com/tandemdude
import discord
import json
from discord.ext import commands


class Welcome(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		with open('config.json') as json_file:
			config = json.load(json_file)
		welcome_channel_id = config['welcome_ch']
		if welcome_channel_id != 0:
			a = discord.Embed(title='Welcome!', color=0xde2bea)
			a.set_author(name=f'{member.display_name} Has joined the server!', icon_url=member.avatar_url)
			welcome_channel = self.bot.get_channel(welcome_channel_id)
			await welcome_channel.send(embed=a)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		with open('config.json') as json_file:
			config = json.load(json_file)
		welcome_channel_id = config['welcome_ch']
		if welcome_channel_id != 0:
			a = discord.Embed(title='See you again soon!', color=0xde2bea)
			a.set_author(name=f'😢 {member.display_name} Has left the server', icon_url=member.avatar_url)
			welcome_channel = self.bot.get_channel(welcome_channel_id)
			await welcome_channel.send(embed=a)


def setup(bot):
	bot.add_cog(Welcome(bot))
