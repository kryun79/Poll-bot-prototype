import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

bot = commands.Bot(command_prefix='!')

@bot.command(name='repeat', help = 'will eventualy repeat the user\'s text')
async def u_repeat(ctx):
  quote = [
    'apple',
    '_',
    (
      'AH'
    )
  ]
  response = random.choice(quote)
  await ctx.send(response)

bot.run(TOKEN)


