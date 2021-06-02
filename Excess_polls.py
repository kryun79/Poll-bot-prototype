import discord
import asyncio
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import aiohttp
import logging


class rp(commands.AutoShardedBot):
    def __init__(self, config):
        prefixes = ["$", "rp:", "Rp:", "RP:"]
        super().__init__(
            command_prefix = prefixes,
            status = discord.Status.online,
            activity = discord.Game(name = "$help"))
        self.load_extension('cogs.poll')
        self.config = config
        self.shard_count = self.config["shards"]["count"]
        shard_ids_list = []
        shard_ids = []
        
        # create list of shard ids
        for i in range(self.config["shards"]["first_shard_id"], self.config["shards"]["last_shard_id"]+1):
            shard_ids_list.append(i)
        self.shard_ids = tuple(shard_ids_list)

    async def on_ready(self):
        self.http_session = aiohttp.ClientSession()
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("--------")
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)
    def run(self):
        super().run(self.config["discord_token"], reconnect=True)
