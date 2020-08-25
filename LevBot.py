import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Watching Team Levation'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'quack':
        await client.send_message(message.channel,'{name} Goes Quack')
    if message.content == 'Quack':
        await client.send_message(message.channel,'{name} Goes Quack')
    if ('Fuck ') in message.content:
       await client.delete_message(message)
    if ('Fuck ') in message.content:
       await client.delete_message(message)
    if ('Ass') in message.content:
       await client.delete_message(message)
    if ('sex') in message.content:
       await client.delete_message(message)
    if ('shit') in message.content:
       await client.delete_message(message)
client.run('NzQ3NjAyNTcyNzI1OTc3MTgx.X0RRJw.mVtDEDaYlPHgL0gPfOLSKJTp-Ek')
