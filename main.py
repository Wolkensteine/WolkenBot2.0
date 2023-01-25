# You are allowed to use the code in this project as long as you follow the licence, which you can find on the
# corresponding GitHub page: https://github.com/Wolkensteine/WolkenBot2.0

# imports
import datetime
import discord
import Help
import admin as ad
import MathCommands

# Bot setup
intents = discord.Intents.all()
bot = discord.Bot(intents=intents, help_command=None)

# Keys
f = open("./Config/keys.txt")
content = f.read().splitlines()
discord_secret = content[0]


# commands
@bot.slash_command(name="help", description="This command will give you help. You can define a specific theme that you need help for.")
async def help(ctx, *, subject=None):
    await Help.help_command(ctx, subject)


@bot.slash_command(name="hello", description="This command will make the bot greet someone. You can provide a name to be greeted.")
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.slash_command(name="info", description="This command will provide you with information about the bot.")
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


admin = discord.SlashCommandGroup("admin", "Admin related commands")


@admin.command(name="role_rights", description="Change the rights of a specified role")
async def role_rights(ctx, role, rights):
    if await ad.admin_right_check(ctx):
        ad.change_access(rights, role, ctx.guild.name)


@admin.command(name="command_rights", description="Change the needed rights for a command")
async def command_rights(ctx, command, rights):
    if await ad.admin_right_check(ctx):
        ad.change_command_rights(rights, command, server=ctx.guild.name)


@admin.command(name="add_admin_role", description="Add a role as admin role")
async def add_admin_role(ctx, role):
    if await ad.admin_right_check(ctx):
        ad.add_role_as_admin(ctx, role)


bot.add_application_command(admin)
math = discord.SlashCommandGroup("math", "Math related commands")


@math.command(name="math_square", description="This will calculate: num1^num2")
async def square(ctx, num1, num2):
    await MathCommands.math_square(ctx, num1, num2)


@math.command(name="math_root", description="This will calculate: take the num2th root of num1")
async def square(ctx, num1, num2):
    await MathCommands.math_square(ctx, num1, num2)


bot.add_application_command(math)


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
        await message.channel.send("Hello " + str(message.author).split("#")[0])
        await message.add_reaction("👋")


# Run bot
ad.load_settings()
bot.run(discord_secret)
