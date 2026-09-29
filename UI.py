
import Player, Globals


def clearScreen():
    print("\033[2J\033[H", end="")


def inventory():
    print(f"""
LAYER:      {Globals.oreLayers[Player.layer].capitalize()}
TOOL:       {Globals.ores[Player.tool - 1].capitalize() if Player.tool > 0 else "Fist"}
COINS:      {Player.coins}

            ORE:\tWORKERS:
MUD:        {Player.ores["mud"]}\t\t{Player.workers["mud"]}
STONE:      {Player.ores["stone"]}\t\t{Player.workers["stone"]}
COPPER:     {Player.ores["copper"]}\t\t{Player.workers["copper"]}
IRON:       {Player.ores["iron"]}\t\t{Player.workers["iron"]}
GOLD:       {Player.ores["gold"]}\t\t{Player.workers["gold"]}
DIAMOND:    {Player.ores["diamond"]}\t\t{Player.workers["diamond"]}
EMERALD:    {Player.ores["emerald"]}\t\t{Player.workers["emerald"]}
RUBY:       {Player.ores["ruby"]}\t\t{Player.workers["ruby"]}
SAPPHIRE:   {Player.ores["sapphire"]}\t\t{Player.workers["sapphire"]}
    """)


def display(*outputs):
    clearScreen()
    inventory()

    for output in outputs:
        print(output)

    if outputs:
        print()
