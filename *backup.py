import os
import random
import discord
from discord.ext import commands
from discord import client
from discord.utils import get
from dotenv import load_dotenv
import aiohttp





load_dotenv()



TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']



bot = commands.Bot(command_prefix='='),rp()

emojis = [ '\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']

global vote

@bot.command(name = 'pl', help = "Repeats text entered after the command.  Put sentences in quotes.")
async def poll(ctx, arg):
  if ctx.author != bot.user.id:
    await ctx.channel.send("{}".format(ctx.author.mention)+' Asks "'+arg+'"')



@bot.command(name = 'ph', help = "Pings the question to @here.  Put sentences in quotes.")
async def ph(ctx, arg):
  if ctx.author != bot.user.id:
    channel = ctx.channel
    embed = discord.Embed(title='Hey! Someone asks ',
                          description ='{} '.format(ctx.author.mention)+ ' Asks '+'@here "'+arg +'"',
                          color = discord.Color.blue())
    await channel.send('@here')
    await channel.send(embed=embed)
    global message_id
    message_id = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author.id)



@bot.command(name = 'pe', help = "Pings the question to @everyone.  Put sentences in quotes.")
async def pe(ctx, arg):
  if ctx.author != bot.user.id:
    channel = ctx.channel
    embed = discord.Embed(title='Hey! Someone asks ',
                          description ='{} '.format(ctx.author.mention)+ ' Asks '+'@everyone "'+arg +'"',
                          color = discord.Color.blue())
    await channel.send('@everyone')
    await channel.send(embed=embed)
    global message_id
    message_id = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author.id)



@bot.command(name='quote', help = 'spits a quote')
async def u_repeat(ctx):
  quote = [
    'LMAO',
    '止めて下さい',
    (
      "AAAAAAAAAAAAAAAAAAAAA"
    )
  ]
  response = random.choice(quote)
  await ctx.send(response)

bot.run(TOKEN)