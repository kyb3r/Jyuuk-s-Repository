import discord
from discord.ext import commands
import random
import datetime

bot = commands.Bot(command_prefix='.')

startup_extensions = ['cogs.moderation']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping():
    await bot.say('pong')

@bot.command(pass_context=True)
async def printemoji(ctx):
    author = ctx.author
    server = ctx.message.server
    channel = ctx.message.channel
    
    await bot.send_message("Hey")


@bot.command(pass_context=True)
async def ball8(ctx, *, msg):
    choices = ['yes','no']
    choice = random.choice(choices)
    await bot.say('Question: {} \n Answer: {}'.format(msg, choice))

@bot.command(pass_context=True)
async def date(ctx):
    today = datetime.date.today()
    await bot.say('The data is: {}'.format(today))

@bot.command(pass_context=True, name='user')
async def outputUsername(ctx):
    user = ctx.message.author
    username = str(user.name)
    await bot.say("Your username is: {}".format(username))

@bot.command(pass_context=True, name = 'letteruser')
async def findUsersbyletter(ctx,letter):
    server = ctx.message.server
    members = [str(i) for i in server.members if i.name.lower().startswith(letter.lower())]
    await bot.say('```bf\n'+', '.join(members)+'```')

@bot.command(pass_context=True)
async def embed(ctx):
    em = discord.Embed(color=0x00FFFF,
                       description = 'Hello im an embed')
    await bot.say('aghuaghag', embed=em)
    


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
   
    
    

bot.run('MzM5NzcxOTIwMjQ3NDIyOTgw.DFo1Gg.VmSGjpUTUQhO25QGvumdhEN-QuU')

