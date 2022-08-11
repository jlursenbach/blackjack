#!/usr/bin/env python3
# Jacob Ursenbach
# CPSC 386-01
# 2022-07-21
# jlursenbach@csu.fullerton.edu
# @jlursenbach
#
# Lab 02-00
#
# Blackjack game
#

"""
This is the game loop for the blackjack game!
Can be used to add new games
Uses menu system to load players and enter game
"""
from blackjackgame.table import Table
from blackjackgame.menu import Menu
from blackjackgame.player_box import PlayerBox

ACTIVE_PLAYERS = []
PLR_FILE = PlayerBox()

LAST_PROGRAM_UPDATE = 20210810

TITLE_PAGE = [
    "xxxxxxxxxxxxxxxxxxxx -------- Welcome to -------- xxxxxxxxxxxxxxxxxxxx",
    "    ____    _                  _           _                  _       ",
    r"   |  _ \  | |                | |         | |                | |      ",
    "   | |_) | | |   __ _    ___  | | __      | |   __ _    ___  | | __   ",
    "   |  _ <  | |  / _` |  / __| | |/ /  _   | |  / _` |  / __| | |/ /   ",
    "   | |_) | | | | (_| | | (__  |   <  | |__| | | (_| | | (__  |   <    ",
    r"   |____/  |_|  \__,_|  \___| |_|\_\  \____/   \__,_|  \___| |_|\_\   ",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    f"Last System Update: {LAST_PROGRAM_UPDATE}                         -Jacob Ursenbach-",
]


def player_menu():
    """
    THis menu is used to add delete and load players
    :return: None
    """
    # Header String
    player_header = [
        r" __                      __                       ",
        r"|__) |     /\  \ / |__  |__)     |\/| |__  |\ | |  | ",
        r"|    |___ /~~\  |  |___ |  \     |  | |___ | \| \__/ ",
    ]

    # sets all existing players to be printed at top of menu
    body = ["Saved Players:\n-----"]

    for item in PLR_FILE.players:
        body.append(item.__str__())

    body.append("-----\n")

    # creates menu object
    menu = Menu(name="Player Menu", header=player_header)

    # fills menu object with options/functions
    menu.update(
        {
            'M': (menu.print_menu, (), "Print Menu", False, False),
            'N': (PLR_FILE.add_player, (), "New Player", True, False),
            'P': (PLR_FILE.print_players, (), "Player Database", True, False),
            'D': (PLR_FILE.delete_player, (), "Delete Player", True, False),
            # the formatting wouldn't pass unless I split this up like this.
            'S': (PLR_FILE.save_player_file, (), "Save Game", True, False),
            'L': (load_player, (), "Load Player", True, False),
            'I': (choose_player, (), "Load Index", True, False),
            'U': (unload_player, (), "Unload Player", True, False),
            'A': (loaded_players, (), "Show Loaded Players", True, False),
            'Q': (menu.quit_program, (), "Go Back", True, False),
        }
    )
    menu.run_menu()


def loaded_players():
    """
    prints all players that are loaded for gameplay
    :return: None
    """
    print("Loaded Players:")
    if ACTIVE_PLAYERS:
        for player in ACTIVE_PLAYERS:
            print(player)
    else:
        print("No active players.")


def loaded_players_str():
    """
    creates a string of loaded players list
    :return: string of players
    """
    statement = ''
    statement += "Loaded Players:\n"
    if ACTIVE_PLAYERS:
        for player in ACTIVE_PLAYERS:
            statement += f"{player}\n"
    else:
        statement = "NO ACTIVE PLAYERS"

    return statement


def load_box():
    """
    box for loading players
    :return:
    """
    loading_box = []
    print("---Players Not Loaded---")
    for actor in PLR_FILE.players.values():
        if actor not in ACTIVE_PLAYERS:
            loading_box.append(actor)
            print(f"index:{loading_box.index(actor)} - {actor}")
    print(":::::ACTIVE PLAYERS:::::")
    for actor in ACTIVE_PLAYERS:
        print(actor)
    return loading_box


def choose_player():
    """
    Prints a list of the available players
    Loaded and not loaded
    takes an int and loads the player at that index
    :return:
    """
    loading_box = load_box()

    index_choice = '-1'

    if len(PLR_FILE.players) > 0:
        index_choice = '-1'
        while 0 > int(index_choice) or int(index_choice) > len(loading_box) - 1:
            index_choice = 'none'
            while not str.isnumeric(index_choice):
                index_choice = input("Input index of player to load:")
                if index_choice.lower() == 'q':
                    return

    if len(ACTIVE_PLAYERS) < 4 and index_choice:
        ACTIVE_PLAYERS.append(loading_box[int(index_choice)])
    load_box()


def check_loaded(player_id: str) -> bool:
    """
    Checks if a specific player ID is loaded
    Used in loop to load and unload
    :param player_id:
    :return: None
    """

    already_loaded = False

    for player in ACTIVE_PLAYERS:
        if player.unique_id == player_id:
            already_loaded = True

    return already_loaded


def load_player():
    """
    If player is not already loaded adds them to play list
    :return: None
    """
    # input in function because menu parameters finicky
    player_id = input("ID:")

    # checks if player is allowed to be loaded
    # 4 players max
    if len(ACTIVE_PLAYERS) >= 4:
        print("You may load a maximum of 4 players")
        loaded_players()
        print("Please unload a player to load a player")
    else:
        # can't load a loaded player
        already_loaded = check_loaded(player_id)

        # checks passed: loads player
        if not already_loaded:
            if player_id in PLR_FILE.players.keys():
                player = PLR_FILE.get_player(player_id)
                ACTIVE_PLAYERS.append(player)
            else:
                print("Player_ID does not exist")
        else:
            print("Player is already loaded")
    loaded_players()


def unload_player():
    """
    Finds player object and unloads
    :return:
    """
    # input in function because menu parameters finicky
    player_id = input("ID:")

    # checks if player is loaded
    already_loaded = check_loaded(player_id)

    # if they, remove them
    if already_loaded:
        for actor in ACTIVE_PLAYERS:
            if actor.unique_id == player_id:
                ACTIVE_PLAYERS.remove(actor)
            else:
                print("Player_ID does not exist")
    else:
        print("Player is already loaded")


def main_menu():
    """
    The main menu loop
    :return: False (menu no longer running)
    """
    title = []

    body = [
        r"select 'M' to print the menu if needed",
        r"                                          ",
        r" |\/|  /\  | |\ |     |\/| |__  |\ | |  | ",
        r" |  | /~~\ | | \|     |  | |___ | \| \__/ ",
    ]
    foot = []

    # declaring the menu here so it can be used as a parameter, and print its self
    # menu = {}
    menu = Menu(name="Main Menu", header=title, body=body, footer=foot)

    # menu format = (function, parameters, "Menu Text", Show_Item?, prnt_aftr)
    menu.update(
        {
            'M': (menu.print_menu, (), "Print Menu", False, False),
            'B': (game_loop, (), "Play BlackJack!!!", True, False),
            'P': (player_menu, (), "PLayer Load Menu", True, True),
            'S': (PLR_FILE.save_player_file, (), 'Save Game', True, False),
            'A': (loaded_players, (), "Print Active Players", True, False),
            'C': (print_credits, (), "Credits", True, False),
            'Q': (menu.quit_program, (), "Quit", True, False),
        }
    )
    return menu.run_menu()


def game_loop():
    """
    Calls Table object and starts game
    Provides player box so that Table can save state
    # as of 20220725 table save not implemented
    :return:
    """
    # can only start a game if players are loaded
    if ACTIVE_PLAYERS:
        Table(ACTIVE_PLAYERS, box=PLR_FILE)
        return True

    print("You must have an active player loaded to play.")
    return False


def print_credits():
    """
    Prints some credits
    Open Source
    :return:
    """
    # reprints title
    for line in TITLE_PAGE:
        print(line)

    # credits
    print(
        "This project was coded by Jacob Ursenbach\n"
        "jacob.ursenbach@gmail.com\n"
        "open source: \n"
        "https://github.com/mshafae-summer-2022/cpsc-386-02-blackjack-jlursenbach\n"
        "It was a project for a game design course.\n"
        "Prof: Dr. Michael Shafae - CSUF"
    )


def main():
    """
    Runs file
    :return: None
    """

    # Print Title
    for item in TITLE_PAGE:
        print(item)

    # user input to show title screen
    input("\n       -------------- PRESS ENTER TO CONTINUE --------------\n")

    # prime loop
    program_is_running = True

    while program_is_running:
        # run_menu returns false once loop is broken
        program_is_running = main_menu()

        # sentinel to re-enter menu on faulty click
        user_continue = input("do you want to quit the program? (Y/N)")
        if user_continue.upper() == 'N':
            program_is_running = True

        print("Goodbye")


if __name__ == "__main__":
    game_loop()
