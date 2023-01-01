import discord
import datetime


async def math_root(message, num1, num2):
    temp_text = "The " + num1 + ". root of " + num2 + " is: " + \
                str(float(num1) ** 1 / float(num2))
    embed = discord.Embed(
        title="Math.Root",
        description=temp_text,
        colour=0xcc33ff,
        url="https://Github.com/Wolkensteine/WolkenBot2.0",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await message.channel.send(embed=embed)


async def math_square(message, num1, num2):
    temp_text = num1 + "^" + num2 + " = " + str(float(num1) ** float(num2))
    embed = discord.Embed(
        title="Math.Square",
        description=temp_text,
        color=0xcc33ff,
        url="https://Github.com/Wolkensteine/WolkenBot2.0",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")
    await message.channel.send(embed=embed)
