import discord
import datetime


async def help_command(ctx, argument):

    embed = discord.Embed(
        title="WolkenBot - Help",
        colour=0xaaffaa,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")

    await ctx.respond()