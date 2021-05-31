import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

bot = commands.Bot(command_prefix='!')

Emojis = ['Thumbs Up Sign', 'Thumbs Down Sign']


@bot.command(name = 'rpt', help = "Repeats text entered after the command.  Put sentences in quotes.")
async def rpt(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_message(message):
  message = 'l'
  await message.add_reaction(Emojis[1])
  await message.add_reaction(Emojis[0])

  
@bot.command(name='quote', help = 'will eventualy repeat the user\'s text')
async def u_repeat(ctx):
  quote = [
    'apple',
    '_',
    (
      "AAAAAAAAAAAAAAAAAAAAA"
    )
  ]
  response = random.choice(quote)
  await ctx.send(response)

bot.run(TOKEN)


