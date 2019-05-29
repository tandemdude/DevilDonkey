# Bot requested by DevilDonkey
# Coded by github u/tandemdude
# https://github.com/tandemdude
import discord
from discord.ext import commands
import time
import configparser
import json

# Sets up parser and reads the file containing the bot token
parser = configparser.ConfigParser()
parser.read('TOKEN.INI')

# List of all extensions to be loaded
extensions = ['cogs.OnReadyCog', 'cogs.PurgeCog', 'cogs.CustomCommandsCog', 'cogs.AnnouncementsCog', 'cogs.SetupCog', 'cogs.WelcomeCog', 'cogs.GiveawayCog']
config_file = 'config.json'

# Opens configuration file
with open(config_file) as json_file:  
    config = json.load(json_file)

# Declares the bot prefix and token, taking values from files
prefix = config['prefix']
token = parser['DEFAULT']['token']

# bot = commands.Bot(command_prefix=prefix)

# Main function creates bot, loads extensions and runs the bot
def run_bot():
	bot = commands.Bot(command_prefix=prefix)
    if len(extensions) != 0:
        for ext in extensions:
            bot.load_extension(ext)
    bot.run(token)

# Keeps the bot alive 
while True:
    run_bot()
    time.sleep(5)
