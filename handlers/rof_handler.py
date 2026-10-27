import random

from games import RING_OF_FIRE

rules = RING_OF_FIRE['rules']
setup = RING_OF_FIRE['setup']
card_rules = RING_OF_FIRE['card_value']

def logo():
    print("\n")
    print("""
██████╗░██╗███╗░░██╗░██████╗░  ░█████╗░███████╗  ███████╗██╗██████╗░███████╗
██╔══██╗██║████╗░██║██╔════╝░  ██╔══██╗██╔════╝  ██╔════╝██║██╔══██╗██╔════╝
██████╔╝██║██╔██╗██║██║░░██╗░  ██║░░██║█████╗░░  █████╗░░██║██████╔╝█████╗░░
██╔══██╗██║██║╚████║██║░░╚██╗  ██║░░██║██╔══╝░░  ██╔══╝░░██║██╔══██╗██╔══╝░░
██║░░██║██║██║░╚███║╚██████╔╝  ╚█████╔╝██║░░░░░  ██║░░░░░██║██║░░██║███████╗
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝
""")

def rof_handler(players):
    logo()

    if not players:
        print("No players found.")
        return

    a = input("\nWould you like to view the rules and setup? Y/N\n> ").lower().replace(" ", "")

    if a == "y":
        print("\nSETUP:\n", setup)
        print("\nRULES:\n", rules)

        input("\nPress Enter when ready.")

    rof_playing(players, card_rules)

def rof_playing(players, card_rules):
    current_index = random.randrange(len(players))

    while True:
        current_player = players[current_index]

        print(f"\n{current_player}, please pick a card.")

        card = input("\nEnter your card (or QUIT to quit)\n> ").strip().lower()

        if card == "quit":
            print("Game ended! Returning to main menu")
            return

        for item in card_rules:
            if item["card"] == card:
                print(f"\nCard {card.upper()} selected.")
                print(f"Action: {item['action']}")
                break
            
        else:
            print("Invalid card, please try again.")
            continue

        input("\nPress Enter for the next player... ")

        current_index = (current_index + 1) % len(players)