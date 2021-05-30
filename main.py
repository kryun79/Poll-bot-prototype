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
async def on_reaction_add(reaction, user):
  message = await bot
  for emoji in Emojis:
    await message.add_reaction(emoji)
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


