import discord
import datetime


async def Math_command(message):
    if message.content.lower().replace("!math.", "").startswith("root"):
        inputs = message.content.lower().replace("!math.square ", "").split(" ")
        temp_text = "The " + inputs[1] + ". root of " + inputs[2] + " is: " + \
                    str(float(inputs[2]) ** 1 / float(inputs[1]))
        embed = discord.Embed(
            title="Math.Root",
            description=temp_text,
            colour=0xcc33ff,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)
    elif message.content.lower().replace("!math.", "").startswith("square"):
        inputs = message.content.lower().replace("!math.square ", "").split("^")
        temp_text = inputs[0] + "^" + inputs[1] + " = " + str(float(inputs[0]) ** float(inputs[1]))
        embed = discord.Embed(
            title="Math.Square",
            description=temp_text,
            color=0xcc33ff,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot made by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)
