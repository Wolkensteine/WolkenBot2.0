import discord
import datetime


async def help_command(ctx, argument):
    if argument == "math":
        print()
    elif argument == "admin":
        embed = discord.Embed(
            title="Some help for you my Admin friend!",
            description="You need to have a role named admin or an other role with privileged access.\n"
                        "'/admin rights role' <right> <role> * n\n"
                        "<right>s:\n"
                        "accessall => grant access to all commands for a role\n"
                        "mediumaccess => grant access to most commands for a role\n"
                        "noaccess => deny access to all commands for a role\n"
                        "'/admin rights command' <right> <command>\n"
                        "<command>'s: /<command>\n"
                        "The rights are the same as above.\n"
                        "This will set a required permission level for a command.",
            colour=0xff8c1a,
            url="https://Github.com/Wolkensteine/WolkenBot2.0",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message by WolkenBot 2.0",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
    elif argument == "play":
        print()
    else:
        embed = discord.Embed(
            title="WolkenBot - Help",
            description="/help => help\n"
                        "/friend => Answer with a random sentence - good luck :)\n"
                        "/vote + vote duration in seconds => You can create a voting system (example: '/vote 60"
                        "' to make in vote with a duration of one minute) [default duration: 60 seconds - "
                        "maximal duration is 600 seconds]\n"
                        "/info => informations about the bot\n"
                        "/pin + (message content) => Will pin a custom Message [!Attention!: This will resend "
                        "the Message as an embed, which might corrupt files attached to the message!]\n"
                        "/math => Has some cool math functions implemented. Run '/help math' to see all the "
                        "commands of /math\n"
                        "/play + term => plays a sound specified by the term. Get help with '/help play'\n"
                        "/g => Sends you a random Frog death message.\n"
                        "/rate + text => Lets you rate sth easily\n"
                        "/randomname => returns a random name\n"
                        "/dadjoke => sends you a dad joke (feature requested by binMalKurzImWald)\n"
                        "/help admin => help you if you have the 'Admin'-Role",
            colour=0xff8c1a,
            url="https://Github.com/Wolkensteine/WolkenBot2.0",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message by WolkenBot 2.0",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")

    await ctx.respond(embed=embed)
