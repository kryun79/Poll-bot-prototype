import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

bot = commands.Bot(command_prefix='!')

emoji1 = '\N{THUMBS UP SIGN}'
emoji2 = '\N{THUMBS DOWN SIGN}'


@bot.command(name = 'rpt', help = "Repeats text entered after the command.  Put sentences in quotes.")
async def rpt(ctx, message):
  await ctx.send(message)
  if message.content.startsWith("!rpt"):
    message.react(emoji1)
    message.react(emoji2)



  
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


