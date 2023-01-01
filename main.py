# imports
import discord
import Help
import admin
import datetime

# Bot setup
intents = discord.Intents.all()
bot = discord.Bot(intents=intents, help_command=None)

# Keys
f = open("./Config/keys.txt")
content = f.read().splitlines()
discord_secret = content[0]


# commands
@bot.slash_command()
async def help(ctx, *, argument=None):
    await Help.help_command(ctx, argument)


@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.slash_command()
async def info(ctx):
    embed = discord.Embed(
        title="Info",
        description="WolkenBot 2.0 - Version 1.0.0\nWhen you have any problems either report directly to "
                    "@Wolkensteine or to your server administrator\n"
                    "There is now an official discord!\n"
                    "My invite link: https://discord.gg/vk9v2x4EjT",
        colour=0x00ccff,
        url="https://Github.com/Wolkensteine/WolkenBot2.0",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message by WolkenBot 2.0",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await ctx.respond(embed=embed)


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


# Run bot
admin.load_settings()
bot.run(discord_secret)
