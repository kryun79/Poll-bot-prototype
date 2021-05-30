import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

client = discord.Client()

@client.event 
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break
    # When the bot is ready
    print(
      f"{client.user} has connected to the server" 
      f'{guild.name}(id:{guild.id})'
    )
  
client.run(TOKEN)


