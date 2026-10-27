RING_OF_FIRE = {
        "name": "Ring of fire",
        "min_players": 3,
        "max_players": 8,
        "cards": True,
        "solo_cups": False,
        "jenga_blocks": False,
        "setup": "Clear off your table, set a cup in the centre with a deck of cards placed around the cup in a circle.",
        "rules": "Each person has a cup or bottle of their preffered drink, one person at a time, clockwise picks a card.",
        "card_value": [
            {
                "card": "a",
                "action": "Waterfall, Everyone drinks clockwise from the person who drew the card until the person who\ndrew the card decides to stop."
            },

            {
                "card": "2",
                "action": "Choose, The person who drew the card gets to choose the person that drinks."
            },

            {
                "card": "3",
                "action": "Me, The person who drew the card drinks."
            },

            {
                "card": "4",
                "action": "Whore, All girls have to drink."
            },

            {
                "card": "5",
                "action": "Thumb Master, You can put your thumb on the table and everyone must follow however the last person to do so\nmust drink and this continues until another person draws a five."
            },

            {
                "card": "6",
                "action": "Dicks, All guys Drink."
            },

            {
                "card": "7",
                "action": "Heaven, Randomly point your finger to the sky, last to do so drinks."
            },

            {
                "card": "8",
                "action": "Mate, Choose someone to drink same time as you for the rest of the game."
            },

            {
                "card": "9",
                "action": "Rhyme, Choose a word then clockwise everyone has to rhyme until someone cant, they drink."
            },

            {
                "card": "10",
                "action": "Category, Pick a category and everyone has to say a word in that category until someone cant\nthey drink."
            },

            {
                "card": "j",
                "action": "Rule, Make a rule everyone has to follow e.g. you have to drink stood on your left foot."
            },

            {
                "card": "q",
                "action": "Questions, Go in a cricle asking questions, first to not ask one drinks."
            },

            {
                "card": "k",
                "action": "Pour, pour a little of your drink into the cup in the middle and whoever picks the last king\ndrinks the middle cup."
            }
            ]
}

BEER_PONG = {
    "name": "Beer Pong",
    "min_players": 2,
    "max_players": 2,
    "cards": False,
    "solo_cups": True,
    "jenga_blocks": False,
    "setup": "Clear off a table and put a line down the middle portrait then place cups in a triangle.",
    "rules": "Bounce your ping pong ball if it lands in a cup the other person drinks the whole cup, continue unitl the cups are all drunk on one side "
}

JENGA = {
    "name": "Jenga",
    "min_players": 2,
    "max_players": 5,
    "cards": False,
    "solo_cups": False,
    "jenga_blocks": True,
    "setup": "Set up the jenga blocks in a tower, but the twist is that you write challenges underneath the blocks for people to do.",
    "rules": "Take turns removing a block from the tower and placing it on top, once a block is removed the person must\ncomplete the challenge written on the block, if they fail to do so they must drink. If the tower falls the person\n,who knocked it over must drink and rebuild the tower."

}

BULLSHIT = {
    "name": "Bullshit",
    "min_players": 4,
    "max_players": 8,
    "cards": True,
    "solo_cups": False,
    "jenga_blocks": False,
    "setup": "Deal out all the cards to the players.",
    "rules": "Players take turns placing cards face down claiming their value e.g. i placed a 3, the next person then needs\nto place their card and it needs to be higher than the original claimed value however you can lie about your\ncards value but if someone says bullshit then the person reveals their card and if this card was what they claimed\nthen the accusser drinks but if its not then the accussed drinks.",

}

QUARTERS = {
    "name": "Quarters",
    "min_players": 3,
    "max_players": 6,
    "cards": False,
    "solo_cups": True,
    "jenga_blocks": False,
    "setup": "Fill a cup with your drink and place it in the middle of the table, then each player takes a turn\ntrying to bounce a quarter into the cup.",
    "rules": "If you make the quarter in the cup then you get to choose someone to drink, if you miss then you drink."
}


GAMES = [
    RING_OF_FIRE,
    BEER_PONG,
    JENGA,
    BULLSHIT,
    QUARTERS
]