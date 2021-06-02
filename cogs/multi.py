import random
import discord
from discord.ext import commands
from dotenv import load_dotenv


bot = commands.Bot(command_prefix='$')


load_dotenv()

global vote

class polls(commands):
  @bot.command(name = 'pl', help = "Repeats text entered after the command.  Put sentences in quotes.")
  async def poll(ctx, arg):
    if ctx.author != bot.user.id:
      await ctx.channel.send("{}".format(ctx.author.mention)+' Asks "'+arg+'"')
  @commands.command(name = 'ph', help = "Pings the question to @here.  Put sentences in quotes.")
  async def ph(ctx, arg):
    if ctx.author != bot.user.id:
      channel = ctx.channel
      embed = discord.Embed(title='Hey! Someone asks ',
                          description ='{} '.format(ctx.author.mention)+ ' Asks '+'@here "'+arg +'"',
                          color = discord.Color.blue())
      await channel.send('@here')
      await channel.send(embed=embed)
      global message_id
      message_id = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author.id)



  @commands.command(name = 'pe', help = "Pings the question to @everyone.  Put sentences in quotes.")
  async def pe(ctx, arg):
    if ctx.author != bot.user.id:
      channel = ctx.channel
      embed = discord.Embed(title='Hey! Someone asks ',
                          description ='{} '.format(ctx.author.mention)+ ' Asks '+'@everyone "'+arg +'"',
                          color = discord.Color.blue())
      await channel.send('@everyone')
      await channel.send(embed=embed)
      global message_id
      message_id = discord.utils.get(await channel.history(limit=100).flatten(), author=ctx.author.id)



  @commands.command(name='quote', help = 'spits a quote')
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