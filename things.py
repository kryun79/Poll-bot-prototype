import os
import random
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import aiohttp

def keepboot(self):
  super().run(self.config["Discord_TOKEN"], reconnect=True)