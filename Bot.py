import random
import os
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import random as rand
from itertools import cycle

bot = Bot(command_prefix='.')

status = cycle(['Bananas!', 'Monke Buisness', 'monkey together strong'])
@bot.event
async def on_ready():
    change_status.start()
    print('Bot is Online!')



@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server')


@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')


@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful.", ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{error}')



@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount : int):
    await ctx.channel.purge(limit=ammount)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        await ctx.send('please put in required information for commands for more info type .help <command name>')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('you don\'t have the permissions to use that command')






@bot.command()
async def monke(ctx, ammount=1):
    await ctx.channel.purge(limit=ammount)
    await ctx.send('Bananas!!!!!')

# @bot.command()
# async def kick(ctx, member : discord.member, *, reason=none):
#    await member.kick(reason=reason)

# @bot.command()
# async def ban(ctx, member : discord.member, *, reason=none):
#   await member.ban(reason=reason)

# @bot.command()
# async def unban(ctx, *, member):
#    banned_users = await ctx.guild.bans()
#          user = ban_entry.user
#
#          if (user.name, user.discriminator) == (member_name, member_discriminator):
#            await ctx.guild.unban(user)

@tasks.loop(minutes=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

import random

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)


bot.run('enter token here')
