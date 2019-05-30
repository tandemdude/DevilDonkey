# Uptime extension made by github u/tandemdude
# https://github.com/tandemdude
import time
import discord
from discord.ext import commands


class Uptime(commands.Cog):

	def __init__(self):
		self.start_time = time.monotonic()

	@commands.command()
	async def uptime(self, ctx):
		time_now = time.monotonic()
		s = time_now - self.start_time
		m, s = divmod(s, 60)
		h, m = divmod(m, 60)
		d, h = divmod(h, 24)
		embed = discord.Embed(title='🕛 Current Uptime:', description=f'**{round(d)} Days, {round(h)} Hours, {round(m)} Minutes, {round(s)} Seconds.**', color=0x8d06a8)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Uptime())