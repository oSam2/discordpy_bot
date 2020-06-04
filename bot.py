import os
import discord
from discord.ext import commands
import random


client = discord.Client()

bot = commands.Bot(command_prefix=commands.when_mentioned_or())

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Bot successfully started!')

@bot.event
async def on_message(message):
    if message.content.startswith('hello'):  ### Simple message ###
        await message.channel.send('World')

    if message.content.startswith('hi'):  ### Random message ###
        myList = ['Hi', 'Hello', 'Hey']
        await message.channel.send(random.choice(myList))

    if message.content.startswith('image'):
        channel = message.channel
        await channel.send(file=discord.File('img\\image.jpg')) ### Upload files ###




bot.run('', bot=True, reconnect=True) # Bot token