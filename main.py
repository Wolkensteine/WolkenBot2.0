# imports
import discord
import Help
import admin

# Bot setup
intents = discord.Intents.all()
bot = discord.Bot(intents=intents, help_command=None)

# Keys
f = open("./Config/keys.txt")
content = f.read().splitlines()
discord_secret = content[0]

# MyClient class
class MyClient(discord.Client):
    vote_channel = None
    vote_creator = ""
    votes_per_theme = []
    voting_themes = []
    vote_running = False
    vote_duration = 30

    # rights that might be granted
    # if a role is not in one of the categories it will default to mediumaccess
    access_all = []
    medium_access = []
    no_access = []
    # Array with the server names to see which level must be loaded
    servers = []
    # Arrays for the needed rights for a specific command
    # 0 => access all
    # 1 => medium access
    # 2 => no access
    hello_command = []
    friend_command = []
    vote_command = []
    info_command = []
    pin_command = []
    math_command = []
    bot_command = []
    gif_command = []
    play_command = []
    g_command = []
    rate_command = []
    random_name_command = []
    dad_joke_command = []
    mute_commands = []
    fish_master_command = []
    do_not_annoy_command = []
    # Admin roles
    admin_roles = []
    # announcements
    announcement_channels = []


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
admin.load_settings()
bot.run(discord_secret)
