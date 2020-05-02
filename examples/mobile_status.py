import discord
from discord.ext import commands

description = 'An example bot with mobile status.'

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
  print('ready')

discord.gateway.IdentifyConfig.browser = 'Discord Android'
bot.run('token')
