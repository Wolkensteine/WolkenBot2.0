# imports
import discord
from discord.ext import commands
import Help

# Bot setup
intents = discord.Intents.all()
bot = discord.Bot(intents=intents, help_command=None)

# Keys
f = open("./Config/keys.txt")
content = f.read().splitlines()
discord_secret = content[0]


# events
@bot.event
async def on_ready():
    print("Beep bop! WolkenBot 2.0 is ready!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hallo bot" \
            or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hello bot" \
            or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hallo wolkenbot" \
            or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "hello wolkenbot" \
            or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "moin wolkenbot" \
            or message.content.lower().replace("!", "").replace("?", "").replace(".", "") == "moin bot":
        await message.channel.send("Hello " + str(message.author))
        await message.add_reaction("👋")


# commands
@bot.slash_command()
async def help(ctx, *, argument=None):
    await Help.help_command(ctx, argument=None)


@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


# Run bot
bot.run(discord_secret)
