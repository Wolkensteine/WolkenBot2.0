import datetime
import os
import discord
from Variables import MyClient


# Mute command
async def create_mute_role(message):
    print("Creating mute role")
    mute_role = await message.guild.create_role(name="Mute")
    perms = discord.Permissions()
    perms.update(read_messages=True, read_message_history=True, connect=True, speak=False, send_messages=False)
    await mute_role.edit(reason=None, colour=discord.Colour.dark_grey(), permissions=perms)


def check_for_mute_role(message):
    if discord.utils.get(message.guild.roles, name='Mute'):
        return True
    else:
        return False


async def mute_command(message):
    if not check_for_mute_role(message):
        await create_mute_role(message)
    tmp = message.content.replace("!mute ", "").replace("!Mute", "")
    for member in message.guild.members:
        if member.name.lower() == tmp.lower():
            user = member
            await user.add_roles(discord.utils.get(message.guild.roles, name='Mute'))


async def un_mute_command(message):
    if not check_for_mute_role(message):
        await create_mute_role(message)
    tmp = message.content.replace("!unmute ", "").replace("!Unmute", "")
    for member in message.guild.members:
        if member.name.lower() == tmp.lower():
            user = member
            await user.remove_roles(discord.utils.get(message.guild.roles, name='Mute'))


# Permissions and their configuration
async def permission_denied(message):
    embed = discord.Embed(
        title="Access denied!",
        colour=0xff0000,
        url="https://Github.com/Wolkensteine/WolkenBot",
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_footer(text="Message by WolkenBot 2.0",
                     icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                              "WolkensteineIcon.png")

    await message.channel.send(embed=embed)


def get_role_access(message, rights):
    if isinstance(message.channel, discord.channel.DMChannel):
        return True

    tmp = "_accessall.txt"

    if rights == "0":
        tmp = "_accessall.txt"
    elif rights == "1":
        tmp = "_mediumaccess.txt"
    elif rights == "2":
        return True

    with open("./Admin/" + message.guild.name + tmp) as file:
        tmp = file.read().replace("\n", "")

    tmp = tmp.split(" ")

    for i in range(len(tmp)):
        if tmp[i] in [y.name.lower() for y in message.author.roles]:
            return True

    for i in range(len(MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" "))):
        if MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" ")[i] in \
                [y.name.lower() for y in message.author.roles]:
            return True

    return False


def check_permissions(message, command):
    if isinstance(message.channel, discord.channel.DMChannel):
        return True

    server_num = get_server_number(message.guild.name)
    req_rights = 0
    if command == "hello":
        req_rights = MyClient.hello_command[server_num]
    elif command == "friend":
        req_rights = MyClient.friend_command[server_num]
    elif command == "vote":
        req_rights = MyClient.vote_command[server_num]
    elif command == "info":
        req_rights = MyClient.info_command[server_num]
    elif command == "pin":
        req_rights = MyClient.pin_command[server_num]
    elif command == "math":
        req_rights = MyClient.math_command[server_num]
    elif command == "gif":
        req_rights = MyClient.gif_command[server_num]
    elif command == "bot":
        req_rights = MyClient.bot_command[server_num]
    elif command == "play":
        req_rights = MyClient.play_command[server_num]
    elif command == "g":
        req_rights = MyClient.g_command[server_num]
    elif command == "rate":
        req_rights = MyClient.rate_command[server_num]
    elif command == "randomname":
        req_rights = MyClient.random_name_command[server_num]
    elif command == "dadjokes":
        req_rights = MyClient.dad_joke_command[server_num]
    elif command == "mute":
        req_rights = MyClient.mute_commands[server_num]
    elif command == "fishmaster":
        req_rights = MyClient.fish_master_command[server_num]
    elif command == "donotannoy":
        req_rights = MyClient.do_not_annoy_command[server_num]

    if req_rights == "2":
        return True
    else:
        return get_role_access(message, req_rights)


def load_server(server_name):
    MyClient.servers.append(server_name)
    file = open("./Admin/" + server_name + "_accessall.txt", 'r')
    MyClient.access_all.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_mediumaccess.txt", 'r')
    MyClient.medium_access.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_noaccess.txt", 'r')
    MyClient.no_access.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_command_access.txt", 'r')

    tmp = file.read().replace("\n", "").split(" ")

    MyClient.hello_command.append(tmp[0])
    MyClient.friend_command.append(tmp[1])
    MyClient.vote_command.append(tmp[2])
    MyClient.info_command.append(tmp[3])
    MyClient.pin_command.append(tmp[4])
    MyClient.math_command.append(tmp[5])
    MyClient.bot_command.append(tmp[6])
    MyClient.gif_command.append(tmp[7])
    MyClient.play_command.append(tmp[8])
    MyClient.g_command.append(tmp[9])
    MyClient.rate_command.append(tmp[10])
    MyClient.random_name_command.append(tmp[11])
    MyClient.dad_joke_command.append(tmp[12])
    MyClient.mute_commands.append(tmp[13])
    MyClient.fish_master_command.append(tmp[14])
    MyClient.do_not_annoy_command.append(tmp[15])

    file.close()
    file = open("./Admin/" + server_name + "_admin_roles.txt", 'r')
    MyClient.admin_roles.append(file.read().replace("\n", ""))
    file.close()

    file = open("./Admin/" + server_name + "_announcement_channels.txt", "r")
    MyClient.announcement_channels.append(file.read().replace("\n", ""))
    file.close()


def load_settings():
    file_list = os.listdir(path=r"./Admin/")
    for i in range(len(file_list)):
        tmp = file_list[i].replace("_accessall.txt", "").replace("_mediumaccess.txt", "").replace("_noaccess.txt", "").\
            replace("_command_access.txt", "").replace("_admin_roles.txt", "").replace("_announcement_channels.txt", "")
        if type(get_server_number(tmp)) != int:
            load_server(tmp)


def add_server(server_name):
    print("Adding server: " + server_name)
    MyClient.servers.append(server_name)
    MyClient.access_all.append("")
    MyClient.medium_access.append("")
    MyClient.no_access.append("")
    MyClient.admin_roles.append("admin")

    # Setting default rights
    # 0 => It'll require all rights
    # 1 => It'll require medium rights
    # 2 => It'll require no rights
    MyClient.hello_command.append(2)
    MyClient.friend_command.append(2)
    MyClient.vote_command.append(1)
    MyClient.info_command.append(2)
    MyClient.pin_command.append(0)
    MyClient.math_command.append(2)
    MyClient.bot_command.append(2)
    MyClient.gif_command.append(1)
    MyClient.play_command.append(1)
    MyClient.g_command.append(2)
    MyClient.rate_command.append(1)
    MyClient.random_name_command.append(2)
    MyClient.dad_joke_command.append(2)
    MyClient.mute_commands.append(0)
    MyClient.fish_master_command.append(1)
    MyClient.do_not_annoy_command.append(0)

    file = open("./Admin/" + server_name + "_accessall.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_mediumaccess.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_noaccess.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_command_access.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_admin_roles.txt", 'w')
    file.close()
    file = open("./Admin/" + server_name + "_announcement_channels.txt", "w")
    file.close()
    save(server_name)


def get_server_number(server_name):
    for i in range(len(MyClient.servers)):
        if MyClient.servers[i] == server_name:
            return i
    return False


def save(server):
    server_num = get_server_number(server)
    with open("./Admin/" + server + "_accessall.txt", 'w') as file:
        file.write(MyClient.access_all[server_num])
    with open("./Admin/" + server + "_mediumaccess.txt", 'w') as file:
        file.write(MyClient.medium_access[server_num])
    with open("./Admin/" + server + "_noaccess.txt", 'w') as file:
        file.write(MyClient.no_access[server_num])
    with open("./Admin/" + server + "_admin_roles.txt", 'w') as file:
        file.write(MyClient.admin_roles[server_num])
    with open("./Admin/" + server + "_command_access.txt", 'w') as file:
        file.write(str(MyClient.hello_command[server_num]) + " " +
                   str(MyClient.friend_command[server_num]) + " " +
                   str(MyClient.vote_command[server_num]) + " " +
                   str(MyClient.info_command[server_num]) + " " +
                   str(MyClient.pin_command[server_num]) + " " +
                   str(MyClient.math_command[server_num]) + " " +
                   str(MyClient.bot_command[server_num]) + " " +
                   str(MyClient.gif_command[server_num]) + " " +
                   str(MyClient.play_command[server_num]) + " " +
                   str(MyClient.g_command[server_num]) + " " +
                   str(MyClient.rate_command[server_num]) + " " +
                   str(MyClient.random_name_command[server_num]) + " " +
                   str(MyClient.dad_joke_command[server_num]) + " " +
                   str(MyClient.mute_commands[server_num]) + " " +
                   str(MyClient.fish_master_command[server_num]) + " " +
                   str(MyClient.do_not_annoy_command[server_num]))
    with open("./Admin/" + server + "_announcement_channels.txt", 'w') as file:
        file.write(MyClient.announcement_channels[server_num])


def change_access(access, roles, server):
    if type(get_server_number(server)) != int:
        add_server(server)
    server_num = get_server_number(server)
    if access == "accessall":
        MyClient.access_all[server_num] = roles.lower()
    elif access == "mediumaccess":
        MyClient.medium_access[server_num] = roles.lower()
    elif access == "noaccess":
        MyClient.no_access[server_num] = roles.lower()
    save(server)


def change_command_rights(right, command, server):
    if not get_server_number(server):
        add_server(server)
    server_num = get_server_number(server)
    right_num = 2
    if right == "accessall":
        right_num = 0
    elif right == "mediumaccess":
        right_num = 1
    if command == "hello":
        MyClient.hello_command[server_num] = right_num
    elif command == "friend":
        MyClient.friend_command[server_num] = right_num
    elif command == "vote":
        MyClient.vote_command[server_num] = right_num
    elif command == "info":
        MyClient.info_command[server_num] = right_num
    elif command == "pin":
        MyClient.pin_command[server_num] = right_num
    elif command == "math":
        MyClient.math_command[server_num] = right_num
    elif command == "bot":
        MyClient.bot_command[server_num] = right_num
    elif command == "gif":
        MyClient.bot_command[server_num] = right_num
    elif command == "play":
        MyClient.play_command[server_num] = right_num
    elif command == "g":
        MyClient.g_command[server_num] = right_num
    elif command == "rate":
        MyClient.rate_command[server_num] = right_num
    elif command == "randomname":
        MyClient.random_name_command[server_num] = right_num
    elif command == "dadjokes":
        MyClient.dad_joke_command[server_num] = right_num
    elif command == "mute":
        MyClient.mute_commands[server_num] = right_num
    elif command == "fishmaster":
        MyClient.fish_master_command[server_num] = right_num
    elif command == "donotannoy":
        MyClient.do_not_annoy_command[server_num] = right_num
    save(server)


def add_role_as_admin(message):
    MyClient.admin_roles[get_server_number(message.guild.name)] += " " + message.content.lower().replace("!admin."
                                                                                                              "rights "
                                                                                                              "admin ",
                                                                                                              "")


async def admin_rights_command(message, content):
    # Admins can configure rights with this command
    if content.startswith("role"):
        info = content.replace("role ", "").split(" ")
        if len(info) < 2:
            embed = discord.Embed(
                title="Sorry. I don't remember if this command could run without at least 2 arguments.",
                description="You should try this: !admin.rights role <right> <role> * n",
                colour=0xff0000,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text="Message by WolkenBot 2.0",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")

            await message.channel.send(embed=embed)
        else:
            right = info[0]
            roles = info[1]
            for i in range(len(info) - 2):
                roles += " " + info[i + 2]

            if right == "accessall" or right == "mediumaccess" or right == "noaccess":
                change_access(right, roles, message.guild.name)
            else:
                embed = discord.Embed(
                    title="Sorry. I don't remember that as a right.",
                    description="You should try this: !admin.rights role <right> <role> * n\n"
                                "There are the following rights:\n"
                                "accessall.json => grant access to all commands for a role\n"
                                "mediumaccess => grant access to most commands for a role\n"
                                "noaccess => deny access to all commands for a role\n",
                    colour=0xff0000,
                    url="https://Github.com/Wolkensteine/WolkenBot",
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Message by WolkenBot 2.0",
                                 icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                          "WolkensteineIcon.png")

                await message.channel.send(embed=embed)

    elif content.startswith("command"):
        info = content.replace("command ", "").split(" ")
        if len(info) != 2:
            embed = discord.Embed(
                title="Sorry. I don't remember if this command could run without 2 arguments.",
                description="You should try this: !admin.rights command <right> <command>",
                colour=0xff0000,
                url="https://Github.com/Wolkensteine/WolkenBot",
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_footer(text="Message by WolkenBot 2.0",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")

            await message.channel.send(embed=embed)
        else:
            change_command_rights(info[0], info[1], server=message.guild.name)

    elif content.startswith("admin"):
        add_role_as_admin(message)
        tmp = MyClient.admin_roles[get_server_number(message.guild.name)]
        embed = discord.Embed(
            title="A list of admin roles: ",
            description=tmp,
            colour=0xff8c1a,
            url="https://Github.com/Wolkensteine/WolkenBot2.0",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message by WolkenBot 2.0",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)


async def admin_commands(message):
    global tmp
    tmp = 0

    if type(get_server_number(message.guild.name)) != int:
        add_server(message.guild.name)

    # This switches between different Admin commands
    for i in range(len(MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" "))):
        if MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" ")[i] in \
                [y.name.lower() for y in message.author.roles]:
            if message.content.lower().replace("!admin.", "").startswith("rights"):
                await admin_rights_command(message, message.content.lower().replace("!admin.rights ", ""))
            if message.content.lower().replace("!admin.", "").startswith("help"):
                await admin_help(message)
            tmp = 1
            break

    if tmp == 0:
        embed = discord.Embed(
            title="Access denied!",
            colour=0xff0000,
            url="https://Github.com/Wolkensteine/WolkenBot",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message by WolkenBot 2.0",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")

        await message.channel.send(embed=embed)
