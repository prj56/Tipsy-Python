```
   _______                     ______  __________  ______  _   __
  /_  __(_)___  _______  __   / __ \ \/ /_  __/ / / / __ \/ | / /
   / / / / __ \/ ___/ / / /  / /_/ /\  / / / / /_/ / / / /  |/ / 
  / / / / /_/ (__  ) /_/ /  / ____/ / / / / / __  / /_/ / /|  /  
 /_/ /_/ .___/____/\__, /  /_/     /_/ /_/ /_/ /_/\____/_/ |_/   
     /_/         /____/  
```

A python-based drinking game selector that helps you find a suitable party game based on what you have.

## Requirements

- Python 3.13 or laters
- No external dependencies required

# About The Project

Tipsy Python is currently a command based application designed to make choosing a drinking game easier.

Instead of having to manually search online for games and their rules, users can enter their group size
what equiptment they have and available equiptment. The program will automatically filter through a 
collection of games and display compatible options with their rules

Authors: prj56 & cooperchalmers200925-dev
Version: v0.02

# Features

- **Player Filtering** — Filters games based on minimum and maximum player requirements.
- **Equipment Filtering** — Checks whether players have the equipment required for each game.
- **Game Information** — Stores game descriptions, setup instructions and rules.
- **Expandable Game Library** — New games can easily be added using Python dictionaries.
- **Command-Line Interface** — Simple text-based interaction.

# Built With

- Python 3.13.15
- Python dictionaries and lists
- List comprehensions
- Conditional Statements

# Prerequisites

Currently, if you wish to use this make sure python is installed on your computer.

# Installation

1. Clone the repository
    ```bash
    git clone https://github.com/YOUR_USERNAME/Tipsy-Python.git
    ```
2. Navigate to the project folder
    ```bash
    cd Tipsy-Python
    ```
3. Run the application
    ```bash
    python main.py
    ```

And your done!

# Project Structure
```
Tipsy-Python/
├── DEPRECIATED               # Files that are to be deleted in future releases
├── handlers                  # Where the game's handlers are stored
│   └── bullshit_handler.py   # Bullshit's current Handler
│   └── jenga_handler.py      # Jenga's current Handler
│   └── pong_handler.py       # Beer Pong's current Handler
│   └── quarters_handler.py   # Quarters' current Handler
│   └── rof_handler.py        # Ring of fire's current handler
├── main.py                   # User input and game filtering
├── games.py                  # Game definitions and requirements
└── README.md                 # Project documentation
```
