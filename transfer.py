import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

client = discord.Client()

@client.event 
async def on_ready():
  guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # When the bot is ready
  print(
    f"{client.user} has connected to the server:\n" 
    f'{guild.name}(id:{guild.id})'
  )
  
client.run(TOKEN)


