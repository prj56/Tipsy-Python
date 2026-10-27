import random

from games import JENGA

rules = JENGA['rules']
setup = JENGA['setup']

def logo():
    print("\n")
    print("""
░░░░░██╗███████╗███╗░░██╗░██████╗░░█████╗░
░░░░░██║██╔════╝████╗░██║██╔════╝░██╔══██╗
░░░░░██║█████╗░░██╔██╗██║██║░░██╗░███████║
██╗░░██║██╔══╝░░██║╚████║██║░░╚██╗██╔══██║
╚█████╔╝███████╗██║░╚███║╚██████╔╝██║░░██║
░╚════╝░╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝
""")
    
def jenga_handler(players):
    logo()

    if not players:
        print("No players found.")
        return
    
    a = input("Would you like to view the rules and setup?\n> ").lower().replace(" ", "")

    if a == "y":
        print("RULES:\n", rules)
        print("SETUP:\n", setup)

        input("Press Enter when ready.")

    jenga_playing(players)

def jenga_playing(players):
    current_index = random.randrange(len(players))

    while True:
        current_player = players[current_index]

        print(f"\n{current_player}, starts!")

        input("\n\nWhen finished press enter to return to the menu.")
        return