import discord
import asyncio
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import aiohttp


class Rp(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

        self.emojis = [
                      '👍',
                      '👎',
                      '🤷',
        ]

    # parses the title, which should be in between curly brackets ('{ title }')
    def find_title(self, message):
        # this is the index of the first character of the title
        first = message.find('{') + 1
        # index of the last character of the title
        last = message.find('}')
        if first == 0 or last == -1:
            return "Not using the command correctly"
        return message[first:last]
    # parses the options (recursively), which should be in between square brackets ('[ option n ]')
    def find_options(self, message, options):
        # first index of the first character of the option
        first = message.find('[') + 1
        # index of the last character of the title
        last = message.find(']')
        if (first == 0 or last == -1):
            if len(options) < 2:
                return "Not using the command correctly"
            elif len(options) > 3:
                return "Not using the command correctly"
            else:
                return options
        options.append(message[first:last])
        message = message[last+1:]
        return self.find_options(message, options) 

   
    
    #@commands.Cog.listener()
    @commands.cooldown(2,60,BucketType.user) 
    @commands.command(name="Rp")
    # Limit how often a command can be used, (num per, seconds, BucketType.default/user/member/guild/channel/role)
    async def poll(self, ctx):
        message = ctx.message
        if not message.author.bot:
            if message.content.startswith("=Rp") or message.content.startswith("Rp:") or message.content.startswith("rp:") or message.content.startswith("=rp:") or message.content.startswith("=RP:"):
                messageContent = message.clean_content

                
                title = self.find_title(messageContent)
                options = self.find_options(messageContent, [])

                try:
                    pollMessage = ""
                    i = 0
                    for choice in options:
                        if not options[i] == "":
                            if len(options) > 3:
                                await message.channel.send("Please make sure you are using the command correctly and have less than 3 options.")
                                return
                            elif not i == len(options):
                                pollMessage = pollMessage + "\n\n" + self.emojis[i] + " " + choice
                        i += 1
                    e = discord.Embed(title="**" + title + "**",
                            description=pollMessage,
                                      colour=0x83bae3)
                    pollMessage = await message.channel.send(embed=e)
                    i = 0
                    final_options = []  # There is a better way to do this for sure, but it also works that way
                    for choice in options:
                        if not i == len(options) and not options[i] == "":
                            final_options.append(choice)
                            await pollMessage.add_reaction(self.emojis[i])
                        i += 1
                except KeyError:
                    return "Please make sure you are using the format 'poll: {title} [Option1] [Option2] [Option 3]'"
            else:
                return
    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)

def setup(bot):
    bot.add_cog(Rp(bot))
