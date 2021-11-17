import discord
from discord.ext.commands import Bot
import random as rand

bot = Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'Monke has connected')



@bot.command()
async def copy_me(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def roll(ctx, sidenum):
    num = int(sidenum)
    num1 = num + 1
    await ctx.send(rand.randrange(0, num1))



bot.run('ODkxMDg4ODI0MDE5NjExNjY5.YU5RIw.Mc90lGz1mC02xL2QBF4J2vSlSR0')
