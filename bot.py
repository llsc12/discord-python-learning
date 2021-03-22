# bot.py
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!', intents=discord.Intents.all()) # Head over to discord.com/developers/applications and enable intents on the bot


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")


@client.command()
async def shrug(ctx, *, text):
    await ctx.send(str(text)+str("¯\_(ツ)_/¯"))


@client.command()
async def embed(message, title:str=None, description:str=None, location:int=None):
    if title is None:
        title=""
    if description is None:
        description=""
    title=title.replace("_"," ")
    description=description.replace("_"," ")
    embed=discord.Embed(title=title, description=description)
    if location is None:
        await message.send(embed=embed)
    else:
        channel = client.get_channel(location)
        await channel.send(embed=embed)
        

client.run(TOKEN)
