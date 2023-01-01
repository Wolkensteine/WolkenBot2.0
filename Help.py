import discord
import datetime


async def help_command(ctx, argument):
    embed = discord.Embed(
        title="WolkenBot - Help",
        description="!help => help\n"
                    "!friend => Answer with a random sentence - good luck :)\n"
                    "!vote + vote duration in seconds => You can create a voting system (example: '!vote 60"
                    "' to make in vote with a duration of one minute) [default duration: 60 seconds - "
                    "maximal duration is 600 seconds]\n"
                    "!info => informations about the bot\n"
                    "!pin + (message content) => Will pin a custom Message [!Attention!: This will resend "
                    "the Message as an embed, which might corrupt files attached to the message!]\n"
                    "!math => Has some cool math functions implemented. Run !math.help to see all the "
                    "commands of !math\n"
                    "!gif + search term => Sends you a gif found with your search term\n"
                    "!play. + term => plays a sound specified by the term. Get help with !play.help\n"
                    "!g => Sends you a random Frog death message.\n"
                    "!rate + text => Lets you rate sth easily\n"
                    "!randomname => returns a random name\n"
                    "!dadjoke => sends you a dad joke (feature requested by binMalKurzImWald)\n"
                    "!admin.help => help you if you have the 'Admin'-Role",
        colour=0xff8c1a,
        url="https://Github.com/Wolkensteine/WolkenBot2.0",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")

    await ctx.respond(embed=embed)
