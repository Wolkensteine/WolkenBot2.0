![GitHub Repo stars](https://img.shields.io/github/stars/Wolkensteine/WolkenBot2.0?label=Stars%20%3A%20%29)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Wolkensteine/WolkenBot2.0)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/Wolkensteine/WolkenBot2.0)
![Lines of code](https://img.shields.io/tokei/lines/github.com/Wolkensteine/WolkenBot2.0)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Wolkensteine/WolkenBot2.0)
![Discord](https://img.shields.io/discord/1034396323652317274?color=blue&label=Discord&logo=discord)

# WolkenBot2.0
This is the second etaration of my discord bot. The first etaration is found [here](https://github.com/Wolkensteine/WolkenBot)!<br>
This is just the newest fully functional version of the bot.<br>
Btw when you like the bot you might want to visit my discord, so feel free to join me and some friends! [invite link](https://discord.gg/vk9v2x4EjT)

# Requirements
You will need [pycord](https://pycord.dev/) instead of the normal discord.py library, else the bot will not work.

## Maybe added at some point
### Message counter
```python
  if message.content.startswith('+stat'):
        print(f'Stats command was called by {message.author} in {message.channel}. Now calculating amount of send '
              f'messages for every member in that channel.')

        await message.channel.send('Calculating...')

        counter = []
        members = []

        for i in message.channel.members:
            counter.append(0)
            members.append(i)

        print(f'There are {len(members)} members in {message.channel}.')

        messages = await message.channel.history(limit=9999999).flatten()

        for msg in messages:
            if type(get_member_number(msg.author, members)) == int:
                counter[get_member_number(msg.author, members)] += 1
        description = ""
        print(f'There are {len(messages)} messages in {message.channel}.')
        description += f'There are {len(messages)} messages in {message.channel}.\n'
        for i in range(len(members)):
            print(f'{members[i]} has {counter[i]} messages in {message.channel}.')
            description += f'{members[i]} has {counter[i]} messages in {message.channel}. That are ' \
                           f'{counter[i] / len(messages) * 100}% off all the messages. \n'
        embed = discord.Embed(
            title="Statistics",
            description=description,
            colour=0x99ffbb,
            url="https://Github.com/Wolkensteine/WolkenBot2.0",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)


def get_member_number(member, members):
    print(f'Searching for {member}s number.')
    counter = 0
    for i in members:
        if i == member:
            return counter
        counter += 1

``` 
