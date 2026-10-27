import random

from games import BEER_PONG

rules = BEER_PONG['rules']
setup = BEER_PONG['setup']

def logo():
    print("\n")
    print("""
██████╗░███████╗███████╗██████╗░  ██████╗░░█████╗░███╗░░██╗░██████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██╔════╝░
██████╦╝█████╗░░█████╗░░██████╔╝  ██████╔╝██║░░██║██╔██╗██║██║░░██╗░
██╔══██╗██╔══╝░░██╔══╝░░██╔══██╗  ██╔═══╝░██║░░██║██║╚████║██║░░╚██╗
██████╦╝███████╗███████╗██║░░██║  ██║░░░░░╚█████╔╝██║░╚███║╚██████╔╝
╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚══╝░╚═════╝░
""")
    
def pong_handler(players):
    logo()

    if not players:
        print("No players found.")
        return
    
    a = input("\nWould you like to view the rules and setup? Y/N\n> ").lower().replace(" ", "")

    if a == "y":
        print("\nSETUP:\n", setup)
        print("\nRULES:\n", rules)

        input("\nPress Enter when ready.")

    pong_playing(players)

def pong_playing(players):
    current_index = random.randrange(len(players))

    while True:
        current_player = players[current_index]

        print(f"\n{current_player} starts!")

        input("\n\nWhen finished press enter to return to the menu.")
        return
