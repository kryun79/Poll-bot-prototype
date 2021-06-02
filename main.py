import os
import random
import discord
from discord.ext import commands
from discord import client
from discord.utils import get
from dotenv import load_dotenv
from Excess_polls import rp
import json


with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = os.environ['Discord_TOKEN']
GUILD = os.environ['Discord_Guild']

load_dotenv()

bot = rp(config)
bot.run()