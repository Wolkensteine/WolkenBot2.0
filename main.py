# imports
import discord

# Bot setup
intents = discord.Intents.all()
bot = discord.Bot(command_prefix="!", intents=intents, help_command=None)

# Keys
f = open("./Config/keys.txt")
content = f.read().splitlines()
discord_secret = content[0]

# commands
@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.command()
async def help(ctx, *, argument=None):
    ctx.respond()


# Run bot
bot.run(discord_secret)
