import datetime
import os
import discord
import main


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
    embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
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

    for i in range(len(main.MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" "))):
        if main.MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" ")[i] in \
                [y.name.lower() for y in message.author.roles]:
            return True

    return False


def check_permissions(message, command):
    if isinstance(message.channel, discord.channel.DMChannel):
        return True

    server_num = get_server_number(message.guild.name)
    req_rights = 0
    if command == "hello":
        req_rights = main.MyClient.hello_command[server_num]
    elif command == "friend":
        req_rights = main.MyClient.friend_command[server_num]
    elif command == "vote":
        req_rights = main.MyClient.vote_command[server_num]
    elif command == "info":
        req_rights = main.MyClient.info_command[server_num]
    elif command == "pin":
        req_rights = main.MyClient.pin_command[server_num]
    elif command == "math":
        req_rights = main.MyClient.math_command[server_num]
    elif command == "gif":
        req_rights = main.MyClient.gif_command[server_num]
    elif command == "bot":
        req_rights = main.MyClient.bot_command[server_num]
    elif command == "play":
        req_rights = main.MyClient.play_command[server_num]
    elif command == "g":
        req_rights = main.MyClient.g_command[server_num]
    elif command == "rate":
        req_rights = main.MyClient.rate_command[server_num]
    elif command == "randomname":
        req_rights = main.MyClient.random_name_command[server_num]
    elif command == "dadjokes":
        req_rights = main.MyClient.dad_joke_command[server_num]
    elif command == "mute":
        req_rights = main.MyClient.mute_commands[server_num]
    elif command == "fishmaster":
        req_rights = main.MyClient.fish_master_command[server_num]
    elif command == "donotannoy":
        req_rights = main.MyClient.do_not_annoy_command[server_num]

    if req_rights == "2":
        return True
    else:
        return get_role_access(message, req_rights)


def load_server(server_name):
    main.MyClient.servers.append(server_name)
    file = open("./Admin/" + server_name + "_accessall.txt", 'r')
    main.MyClient.access_all.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_mediumaccess.txt", 'r')
    main.MyClient.medium_access.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_noaccess.txt", 'r')
    main.MyClient.no_access.append(file.read())
    file.close()
    file = open("./Admin/" + server_name + "_command_access.txt", 'r')

    tmp = file.read().replace("\n", "").split(" ")

    main.MyClient.hello_command.append(tmp[0])
    main.MyClient.friend_command.append(tmp[1])
    main.MyClient.vote_command.append(tmp[2])
    main.MyClient.info_command.append(tmp[3])
    main.MyClient.pin_command.append(tmp[4])
    main.MyClient.math_command.append(tmp[5])
    main.MyClient.bot_command.append(tmp[6])
    main.MyClient.gif_command.append(tmp[7])
    main.MyClient.play_command.append(tmp[8])
    main.MyClient.g_command.append(tmp[9])
    main.MyClient.rate_command.append(tmp[10])
    main.MyClient.random_name_command.append(tmp[11])
    main.MyClient.dad_joke_command.append(tmp[12])
    main.MyClient.mute_commands.append(tmp[13])
    main.MyClient.fish_master_command.append(tmp[14])
    main.MyClient.do_not_annoy_command.append(tmp[15])

    file.close()
    file = open("./Admin/" + server_name + "_admin_roles.txt", 'r')
    main.MyClient.admin_roles.append(file.read().replace("\n", ""))
    file.close()

    file = open("./Admin/" + server_name + "_announcement_channels.txt", "r")
    main.MyClient.announcement_channels.append(file.read().replace("\n", ""))
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
    main.MyClient.servers.append(server_name)
    main.MyClient.access_all.append("")
    main.MyClient.medium_access.append("")
    main.MyClient.no_access.append("")
    main.MyClient.admin_roles.append("admin")

    # Setting default rights
    # 0 => It'll require all rights
    # 1 => It'll require medium rights
    # 2 => It'll require no rights
    main.MyClient.hello_command.append(2)
    main.MyClient.friend_command.append(2)
    main.MyClient.vote_command.append(1)
    main.MyClient.info_command.append(2)
    main.MyClient.pin_command.append(0)
    main.MyClient.math_command.append(2)
    main.MyClient.bot_command.append(2)
    main.MyClient.gif_command.append(1)
    main.MyClient.play_command.append(1)
    main.MyClient.g_command.append(2)
    main.MyClient.rate_command.append(1)
    main.MyClient.random_name_command.append(2)
    main.MyClient.dad_joke_command.append(2)
    main.MyClient.mute_commands.append(0)
    main.MyClient.fish_master_command.append(1)
    main.MyClient.do_not_annoy_command.append(0)

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
    for i in range(len(main.MyClient.servers)):
        if main.MyClient.servers[i] == server_name:
            return i
    return False


def save(server):
    server_num = get_server_number(server)
    with open("./Admin/" + server + "_accessall.txt", 'w') as file:
        file.write(main.MyClient.access_all[server_num])
    with open("./Admin/" + server + "_mediumaccess.txt", 'w') as file:
        file.write(main.MyClient.medium_access[server_num])
    with open("./Admin/" + server + "_noaccess.txt", 'w') as file:
        file.write(main.MyClient.no_access[server_num])
    with open("./Admin/" + server + "_admin_roles.txt", 'w') as file:
        file.write(main.MyClient.admin_roles[server_num])
    with open("./Admin/" + server + "_command_access.txt", 'w') as file:
        file.write(str(main.MyClient.hello_command[server_num]) + " " +
                   str(main.MyClient.friend_command[server_num]) + " " +
                   str(main.MyClient.vote_command[server_num]) + " " +
                   str(main.MyClient.info_command[server_num]) + " " +
                   str(main.MyClient.pin_command[server_num]) + " " +
                   str(main.MyClient.math_command[server_num]) + " " +
                   str(main.MyClient.bot_command[server_num]) + " " +
                   str(main.MyClient.gif_command[server_num]) + " " +
                   str(main.MyClient.play_command[server_num]) + " " +
                   str(main.MyClient.g_command[server_num]) + " " +
                   str(main.MyClient.rate_command[server_num]) + " " +
                   str(main.MyClient.random_name_command[server_num]) + " " +
                   str(main.MyClient.dad_joke_command[server_num]) + " " +
                   str(main.MyClient.mute_commands[server_num]) + " " +
                   str(main.MyClient.fish_master_command[server_num]) + " " +
                   str(main.MyClient.do_not_annoy_command[server_num]))
    with open("./Admin/" + server + "_announcement_channels.txt", 'w') as file:
        file.write(main.MyClient.announcement_channels[server_num])


def change_access(access, roles, server):
    if type(get_server_number(server)) != int:
        add_server(server)
    server_num = get_server_number(server)
    if access == "accessall":
        main.MyClient.access_all[server_num] = roles.lower()
    elif access == "mediumaccess":
        main.MyClient.medium_access[server_num] = roles.lower()
    elif access == "noaccess":
        main.MyClient.no_access[server_num] = roles.lower()
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
        main.MyClient.hello_command[server_num] = right_num
    elif command == "friend":
        main.MyClient.friend_command[server_num] = right_num
    elif command == "vote":
        main.MyClient.vote_command[server_num] = right_num
    elif command == "info":
        main.MyClient.info_command[server_num] = right_num
    elif command == "pin":
        main.MyClient.pin_command[server_num] = right_num
    elif command == "math":
        main.MyClient.math_command[server_num] = right_num
    elif command == "bot":
        main.MyClient.bot_command[server_num] = right_num
    elif command == "gif":
        main.MyClient.bot_command[server_num] = right_num
    elif command == "play":
        main.MyClient.play_command[server_num] = right_num
    elif command == "g":
        main.MyClient.g_command[server_num] = right_num
    elif command == "rate":
        main.MyClient.rate_command[server_num] = right_num
    elif command == "randomname":
        main.MyClient.random_name_command[server_num] = right_num
    elif command == "dadjokes":
        main.MyClient.dad_joke_command[server_num] = right_num
    elif command == "mute":
        main.MyClient.mute_commands[server_num] = right_num
    elif command == "fishmaster":
        main.MyClient.fish_master_command[server_num] = right_num
    elif command == "donotannoy":
        main.MyClient.do_not_annoy_command[server_num] = right_num
    save(server)


def add_role_as_admin(message):
    main.MyClient.admin_roles[get_server_number(message.guild.name)] += " " + message.content.lower().replace("!admin."
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
            embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
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
                embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
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
            embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
                             icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                      "WolkensteineIcon.png")

            await message.channel.send(embed=embed)
        else:
            change_command_rights(info[0], info[1], server=message.guild.name)

    elif content.startswith("admin"):
        add_role_as_admin(message)
        tmp = main.MyClient.admin_roles[get_server_number(message.guild.name)]
        embed = discord.Embed(
            title="A list of admin roles: ",
            description=tmp,
            colour=0xff8c1a,
            url="https://Github.com/Wolkensteine/WolkenBot2.0",
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")
        await message.channel.send(embed=embed)


async def admin_commands(message):
    global tmp
    tmp = 0

    if type(get_server_number(message.guild.name)) != int:
        add_server(message.guild.name)

    # This switches between different Admin commands
    for i in range(len(main.MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" "))):
        if main.MyClient.admin_roles[get_server_number(message.guild.name)].replace("\n", "").split(" ")[i] in \
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
        embed.set_footer(text="Message send by WolkenBot 2.0 created by Wolkensteine",
                         icon_url="https://raw.githubusercontent.com/Wolkensteine/Wolkensteine/main/"
                                  "WolkensteineIcon.png")

        await message.channel.send(embed=embed)
