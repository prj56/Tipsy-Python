import random

from games import GAMES

# Global Variables
game = None # The game
players = None # Amount of players
cards = None # Do they have cards
solo_cups = None # Do they have solo cups
jenga_blocks = None # Do they have jenga blocks

# Print out the logo when called
def logo():
    print("")
    print(r"   _______                     ______  __________  ______  _   __")
    print(r"  /_  __(_)___  _______  __   / __ \ \/ /_  __/ / / / __ \/ | / /")
    print(r"   / / / / __ \/ ___/ / / /  / /_/ /\  / / / / /_/ / / / /  |/ /")
    print(r"  / / / / /_/ (__  ) /_/ /  / ____/ / / / / / __  / /_/ / /|  /")
    print(r" /_/ /_/ .___/____/\__, /  /_/     /_/ /_/ /_/ /_/\____/_/ |_/")
    print(r"      /_/         /____/  ")
    print("")
    print("")

# Routing to game file and formatting
def handle_games(players):
    global jenga_blocks, cards, solo_cups, game

    # Filtering for player amount
    available_games = [
        game for game in GAMES
        if int(game["min_players"]) <= players <= int(game["max_players"])
    ]

    # Filtering by equiptment
    available_games = [
        game for game in available_games
        if (not game["jenga_blocks"] or jenga_blocks)
        and (not game["cards"] or cards)
        and (not game["solo_cups"] or solo_cups)
    ]

    # Afterwards here will direct to each game's handler

    for game in available_games:
        print(game["name"])

# Format cards and solo_cups
def format_options():
    global cards, solo_cups, jenga_blocks

    if cards == "yes" or cards == "y":
        cards = True

    elif cards == "no" or cards == "n":
        cards = False
    else:
        print("Please enter either Y or N.\n")
        menu()

    if solo_cups == "yes" or solo_cups == "y":
        solo_cups = True

    elif solo_cups == "no" or solo_cups == "n":
        solo_cups = False

    else:
        print("Please enter either Y or N.\n")
        menu()

    if jenga_blocks == "yes" or jenga_blocks == "y":
        jenga_blocks = True

    elif jenga_blocks == "no" or jenga_blocks == "n":
        jenga_blocks = False

    else:
        print("please enter either Y or N\n"),
        menu()   
    
    
    handle_games(players)

def menu():
    global players, cards, solo_cups, jenga_blocks
    logo()
    
    players = int(input("How many players are there?\n> "))
    cards = input("Do you have a deck of cards? Y / N\n> ").lower().replace(" ", "")
    solo_cups = input("Do you have any solo cups and a ping pong ball? Y / N\n> ").lower().replace(" ", "")
    jenga_blocks = input("Do you have jenga blocks? Y / N\n> ").lower().replace(" ", "")

    format_options()

menu()