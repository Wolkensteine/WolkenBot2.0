# MyClient class
class MyClient:
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
