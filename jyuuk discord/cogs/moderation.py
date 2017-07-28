import discord
from discord.ext import commands

class Moderation:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def kick(self, ctx, user : discord.Member):
        try:               
            await self.bot.kick(user)
        except:
            await self.bot.say('I dont have the perms.')
        else:
            await self.bot.say('I kicked {}.'.format(user.name))


def setup(bot):
    bot.add_cog(Moderation(bot))
