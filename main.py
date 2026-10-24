import random

# Handlers Imports
from handlers.rof_handler import rof_handler

from games import GAMES

# Global Variables
game = None # The game
players = None # Amount of players
cards = None # Do they have cards
solo_cups = None # Do they have solo cups
jenga_blocks = None # Do they have jenga blocks

names = []

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

    selected_game = random.choice(available_games)

    assign_games(selected_game['name'])

game_handlers = {
    "Ring of fire": rof_handler
}

def assign_games(game):
    handler = game_handlers.get(game)

    if handler is None:
        print("Not working")

    handler(names)

def get_names():
    global names

    names.clear()

    for i in range(players):
        while True:
            name = input(f"Enter Player {i + 1}: ").strip()

            if name:
                names.append(name)
                break

            print("Please enter a valid name.")

def validate_input(question):
    while True:
        answer = input(question).lower().replace(" ", "")

        if answer in ("y" or "yes"):
            return True
        
        elif answer in ("n", "no"):
            return False
        
        else:
            print("Please enter either Y or N.\n")

def get_players():
    while True:
        try:
            count = int(input("How many players are there?\n> "))
            
            if count < 1:
                print("Please enter at least one player.\n")
                continue

            return count
        
        except ValueError:
            print("Please enter a valid number.\n")

def menu():
    global players, cards, solo_cups, jenga_blocks

    logo()
    
    players = get_players()

    cards = validate_input(
        "Do you have a deck of cards? Y/N\n> "
    )

    solo_cups = validate_input(
        "Do you have solo cups and ping pong ball? Y/N\n> "
    )

    jenga_blocks = validate_input(
        "Do you have any jenga blocks? Y/N\n> "
    )

    get_names()
    handle_games(players)

menu()