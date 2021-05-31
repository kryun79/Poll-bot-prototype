import os
import random
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

bot = commands.Bot(command_prefix='!')

emojis = [ '\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']

global vote

class MyClient(discord.Client):
  async def on_ready(self):
    print('The bot is ready and logged on as', self.user)

@bot.command(name = 'p', help = "Repeats text entered after the command.  Put sentences in quotes.")
async def poll(ctx, arg):
  if ctx.author != bot.user.id:
    await ctx.channel.send("{}".format(ctx.author.mention)+' Asks "'+arg+'"')

@bot.command(name = 'ph', help = "Pings the question to @here.  Put sentences in quotes.")
async def poll(ctx, arg):
  if ctx.author != bot.user.id:
    await ctx.channel.send("{}".format(ctx.author.mention)+' Asks '+' @here '+arg)

vote = 0
@bot.event
async def on_raw_reaction_add(payload):
  
    if payload.emoji.name == '\N{THUMBS UP SIGN}':
      global vote
      vote = vote+1
    if payload.emoji.name == '\N{THUMBS DOWN SIGN}':
      vote = vote-1
    print(int(vote))
  
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

client = MyClient
bot.run(TOKEN)