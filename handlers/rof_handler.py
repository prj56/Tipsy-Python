from games import RING_OF_FIRE

rules = RING_OF_FIRE['rules']
setup = RING_OF_FIRE['setup']

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

def rof_handler():
    logo()

    a = input("\nWould you like to view the rules and setup? Y/N\n> ").strip().replace(" ", "")

    if a == "y":
        print("\nSETUP:\n", setup)
        print("\nRULES:\n", rules)

        b = input("\nEnter Y when ready.\n> ").strip().replace(" ", "")

        if b == "y":
            print("Game on!")

    else:
        print("Game on!")