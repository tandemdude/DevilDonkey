# Bot requested by DevilDonkey
# Coded by github u/tandemdude
# https://github.com/tandemdude
import discord
from discord.ext import commands
import time
import json

extensions = ['cogs.OnReadyCog', 'cogs.PurgeCog', 'cogs.CustomCommandsCog', 'cogs.AnnouncementsCog', 'cogs.SetupCog', 'cogs.WelcomeCog', 'cogs.GiveawayCog']
config_file = 'config.json'

with open(config_file) as json_file:  
    config = json.load(json_file)

prefix = config['prefix']
token = 'YOUR TOKEN GOES HERE'

bot = commands.Bot(command_prefix=prefix)


def run_bot():
    if len(extensions) != 0:
        for ext in extensions:
            bot.load_extension(ext)
    bot.run(token)


while True:
    run_bot()
    time.sleep(5)
