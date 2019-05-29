# Giveaway extension coded by github u/tandemdude
# https://github.com/tandemdude
import discord
import asyncio
import json
import datetime
import random
from datetime import timedelta
from discord.ext import commands


class Giveaway(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.previous_giveaway = 0

	@commands.command()
	@commands.has_role('BotUser')
	async def gstart(self, ctx):
		"""Starts a giveaway in the channel specified during setup
		The bot will walk you through setup, just run !gstart
		"""
		with open('config.json') as json_file:
			config = json.load(json_file)

		giveaway_channel = self.bot.get_channel(config["giveaway_ch"])

		def create_embed(item, end_time, winners, minutes, hours):
			day, time = end_time[0], end_time[1]
			g = discord.Embed(title=f'{winners}x {item}', description=f'{hours}h {minutes}m remaining', color=0xffd700)
			g.set_footer(text=f'Ends on {day} at {time} UTC')
			return g

		def check(m):
			return m.content.isdigit() and m.author == ctx.author

		await ctx.send('Beginning giveaway setup:')

		await ctx.send('Please enter the number of winners to be picked')
		number_of_winners = (await self.bot.wait_for('message', check=check, timeout=60)).content
		await ctx.send('Parameter saved')

		await ctx.send('Please enter the item being given away')
		item = (await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)).content
		await ctx.send('Parameter saved')

		await ctx.send('Please enter the amount of time for the giveaway to run in minutes')
		minutes_to_end = (await self.bot.wait_for('message', check=check, timeout=60)).content
		await ctx.send('Parameter saved')
		
		end_time_datetime = datetime.datetime.utcnow() + timedelta(minutes=int(minutes_to_end))
		end_time = [end_time_datetime.strftime('%Y-%m-%d'), end_time_datetime.strftime('%H:%M')]

		giveaway = create_embed(item, end_time, number_of_winners, int(minutes_to_end)%60, int(minutes_to_end)//60)
		giveaway_msg = await giveaway_channel.send('🎉 Giveaway! 🎉', embed=giveaway)
		await giveaway_msg.add_reaction('🎉')
		await ctx.send(f'Posted new giveaway of `{item}`. Giveaway ID = {giveaway_msg.id}')

		time_now = datetime.datetime.utcnow()
		while time_now < end_time_datetime:
			time_now = datetime.datetime.utcnow()
			time_to_end = end_time_datetime - time_now
			seconds = time_to_end.seconds
			minutes, seconds = divmod(seconds, 60)
			hours, minutes = divmod(minutes, 60)
			new_embed = create_embed(item, end_time, number_of_winners, minutes, hours)
			await giveaway_msg.edit(embed=new_embed)
			await asyncio.sleep(1)

		reacted_giveaway_msg = await giveaway_channel.fetch_message(giveaway_msg.id)

		for reaction in reacted_giveaway_msg.reactions:

			if str(reaction.emoji) == '🎉':
				giveaway_reaction = reaction
				reacted_users = await giveaway_reaction.users().flatten()
				users = [u for u in reacted_users if not u.bot]

				if len(users) > 0:
					giveaway_winners = random.sample(users, int(number_of_winners))
					new_embed = discord.Embed(title=f'{number_of_winners}x {item}', description='Giveaway Ended')
					new_embed.set_footer(text=f'Ended on {end_time[0]} at {end_time[1]} UTC')
					await giveaway_msg.edit(embed=new_embed)
					mentions = []
					for user in giveaway_winners:
						mentions.append(user.mention)
					char = ', '
					await giveaway_channel.send(f'🎉 Congratulations {char.join(mentions)} for winning `{item}`! 🎉')
				else:
					await giveaway_channel.send('No one entered the giveaway 😢')

		self.previous_giveaway = giveaway_msg.id

	@commands.command()
	async def greroll(self, ctx):
		"""Rerolls one entry for the previous giveaway
		"""
		with open('config.json') as json_file:
			config = json.load(json_file)

		giveaway_channel = self.bot.get_channel(config["giveaway_ch"])

		await ctx.send('Rerolling most recent giveaway.')
		reacted_giveaway_msg = await giveaway_channel.fetch_message(self.previous_giveaway)

		for reaction in reacted_giveaway_msg.reactions:

			if str(reaction.emoji) == '🎉':
				print('reaction found')
				giveaway_reaction = reaction
				reacted_users = await giveaway_reaction.users().flatten()
				print('flattened')
				users = [u for u in reacted_users if not u.bot]
				
				if len(users) > 0:
					giveaway_winner = random.choice(users)
					await giveaway_channel.send(f'The new winner is {giveaway_winner.mention}')
				else:
					await giveaway_channel.send('No one entered the giveaway 😢')


def setup(bot):
	bot.add_cog(Giveaway(bot))
