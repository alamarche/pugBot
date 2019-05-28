import discord
from discord.ext import commands
from pug import Pug, Team

TOKEN = "NTgyOTM0MDE0MzE1MjAwNTEy.XO1B6A.-PtyJB_3TfKiIRS5bzS75rh8Qj4"

description = "this is a meme bot for soopraball puggers only"

bot = commands.Bot(command_prefix='!', description=description)

pug = None


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def prefix(ctx, new_prefix: str):
    bot.command_prefix = new_prefix
    await ctx.send(f"Command Prefix changed to: {bot.command_prefix}")

@bot.command()
async def start(ctx, pug_size: int):
    global pug
    try:
        if pug is not None:
            await ctx.send(f"<@{ctx.author.id}> There is already an ongoing pug in this channel.")
        else:
            if pug_size == 3 or pug_size == 5:
                blue_team = Team(pug_size, "Blue")
                red_team = Team(pug_size, "Red")
                pug = Pug(pug_size)
                await ctx.send(f"{pug.pug_status('Pug has started.')}")
            else:
                await ctx.send(f"Invalid Pug Size")
    except:
        if pug_size == 3 or pug_size == 5:
            blue_team = Team(pug_size, "Blue")
            red_team = Team(pug_size, "Red")
            pug = Pug(pug_size)
            await ctx.send(f"{pug.pug_status('Pug has started.')}")
        else:
            await ctx.send(f"Invalid Pug Size")


@bot.command(aliases=["list", "players"])
async def status(ctx):
    await ctx.send(pug.pug_status(''))


@bot.command()
async def aadd(ctx, user: str, position: str):
    if position == "m":
        if len(pug.mids) >= pug.mid_limit:
            await ctx.send(f"<@{ctx.author.id}> This position is full.")
        else:
            # todo add player to mids
            pass

    elif position == "k":
        if len(pug.keeps) >= pug.keep_limit:
            await ctx.send(f"<@{ctx.author.id}> This position is full.")
        else:
            # todo add player to keep
            pass

    elif position == "d":
        if len(pug.defs) >= pug.def_limit:
            await ctx.send(f"<@{ctx.author.id}> This position is full.")
        else:
            # todo add player to def
            pass
    else:
        await ctx.send(f"<@{ctx.author.id}> Invalid position.")
    await ctx.send(pug.pug_status(''))


bot.run('NTgyOTM0MDE0MzE1MjAwNTEy.XO1B6A.-PtyJB_3TfKiIRS5bzS75rh8Qj4')
