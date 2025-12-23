import discord
from discord.ext import commands
import os, random
print(os.listdir('images'))
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)
@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images\meme1nostalgia.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# This example requires the 'members' and 'message_content' privileged intents to function.

description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def lamebot(ctx):
    await ctx.send(
        "Wassup I'm lamebot and I'm lame\n"
        "Can't do much right now, but for some reason I can show you some pollution tips😭\n\n"
        "I can do some dice rolls but that's because I grabbed a random template from github 🥀\n"
        "Type ?function to see my POLLUTION TIPS?!🔥🔥"
    )

@bot.command()
async def function(ctx):
    await ctx.send(
        "Here are some functions on tips regarding pollution that I totally made by myself:\n\n"
        "`?reminder` – Use trash as a reminder, not just waste\n"
        "`?separate` – A simple way to start separating waste\n"
        "`?focus` – Focus on one area first\n"
        "`?delay` – Delay throwing trash away\n"
        "`?attention` – Notice what trash you use the most"
    )

@bot.command()
async def reminder(ctx):
    await ctx.send(
        "Before throwing something away, pause for a second.\n"
        "If you throw it away often, that’s your sign to reduce or reuse it."
    )

@bot.command()
async def separate(ctx):
    await ctx.send(
        "Start simple.\n"
        "Food waste in one bag, everything else in another.\n"
        "You don’t need special bins to begin."
    )

@bot.command()
async def focus(ctx):
    await ctx.send(
        "Don’t try to manage all your trash at once.\n"
        "Pick one place first: kitchen, desk, or car.\n"
        "One area done is better than none."
    )

@bot.command()
async def delay(ctx):
    await ctx.send(
        "Before throwing something away, see if it can be used one more time.\n"
        "Delaying trash even a little helps reduce waste."
    )

@bot.command()
async def attention(ctx):
    await ctx.send(
        "Look at your trash once before cleaning it.\n"
        "What shows up the most? That’s the best place to start reducing."
    )

@bot.command()
async def memep(ctx):
    memes = [
        "images/pandemicpollution.jpg",
        "images/pollutioncorruption.jpg",
        "images/beforeandafterhumansandtrash.jpg"
    ]

    meme = random.choice(memes)
    await ctx.send(file=discord.File(meme))



bot.run("MTQ0Mjg1ODkyNzgyOTI4Njk5Mw.GlE90N.N2dWcWKN0g2plxzDMBpSnDg_Ky-yQHtdB--lYI")