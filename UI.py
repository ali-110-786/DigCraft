
import Player, Globals, UI


def clearScreen():
    print("\033[2J\033[H", end="")


def inventory():
    layer = Globals.oreLayers[Player.layer]
    tool = Globals.ores[Player.tool - 1] if Player.tool > 0 else "fist"

    print(f"""
{BOLD}{"LAYER:":<12}{END}{oreColours[layer]}{layer.capitalize()}{END}
{BOLD}{"TOOL:":<12}{END}{oreColours[tool]}{tool.capitalize()}{END}
{BOLD}{YELLOW}{"COINS:":<12}{END}{YELLOW}{Player.coins}{END}

{"":<12}{BOLD}{"ORE:":<12}{"WORKERS:":<12}{END}
{BOLD}{MUD}{"MUD:":<12}{END}{MUD}{Player.ores["mud"]:<12}{Player.workers["mud"]:<12}{END}
{BOLD}{STONE}{"STONE:":<12}{END}{STONE}{Player.ores["stone"]:<12}{Player.workers["stone"]:<12}{END}
{BOLD}{COPPER}{"COPPER:":<12}{END}{COPPER}{Player.ores["copper"]:<12}{Player.workers["copper"]:<12}{END}
{BOLD}{IRON}{"IRON:":<12}{END}{IRON}{Player.ores["iron"]:<12}{Player.workers["iron"]:<12}{END}
{BOLD}{GOLD}{"GOLD:":<12}{END}{GOLD}{Player.ores["gold"]:<12}{Player.workers["gold"]:<12}{END}
{BOLD}{DIAMOND}{"DIAMOND:":<12}{END}{DIAMOND}{Player.ores["diamond"]:<12}{Player.workers["diamond"]:<12}{END}
{BOLD}{EMERALD}{"EMERALD:":<12}{END}{EMERALD}{Player.ores["emerald"]:<12}{Player.workers["emerald"]:<12}{END}
{BOLD}{RUBY}{"RUBY:":<12}{END}{RUBY}{Player.ores["ruby"]:<12}{Player.workers["ruby"]:<12}{END}
{BOLD}{SAPPHIRE}{"SAPPHIRE:":<12}{END}{SAPPHIRE}{Player.ores["sapphire"]:<12}{Player.workers["sapphire"]:<12}{END}
    """)


def display(*outputs):
    clearScreen()
    inventory()

    for output in outputs:
        print(output)

    if outputs:
        print()


HEADER = '\033[95m'
BOLD = '\033[1m'

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'

MUD = '\033[48;5;94m'
STONE = '\033[48;5;245m'
COPPER = '\033[48;5;208m'
IRON = '\033[48;5;251m'
GOLD = '\033[48;5;220m'
DIAMOND = '\033[48;5;51m'
EMERALD = '\033[48;5;46m'
RUBY = '\033[48;5;160m'
SAPPHIRE = '\033[48;5;33m'

MUDTEXT = '\033[38;5;94m'
STONETEXT = '\033[38;5;245m'
COPPERTEXT = '\033[38;5;208m'
IRONTEXT = '\033[38;5;251m'
GOLDTEXT = '\033[38;5;220m'
DIAMONDTEXT = '\033[38;5;51m'
EMERALDTEXT = '\033[38;5;46m'
RUBYTEXT = '\033[38;5;160m'
SAPPHIRETEXT = '\033[38;5;33m'

oreColours = {
    "mud": MUDTEXT,
    "stone": STONETEXT,
    "copper": COPPERTEXT,
    "iron": IRONTEXT,
    "gold": GOLDTEXT,
    "diamond": DIAMONDTEXT,
    "emerald": EMERALDTEXT,
    "ruby": RUBYTEXT,
    "sapphire": SAPPHIRETEXT,
    "home": "",
    "fist": ""
}

END = '\033[0m'


pickaxe = [
    "  _______  ",
    " /_______\\ ",
    "    | |   ",
    "    | |   ",
    "    |_|   "
]

def displayPickaxe():
    return "".join([line + "\n" for line in pickaxe])

worker = [
    "   O   ",
    "  /|\\  ",
    " / | \\ ",
    "   |   ",
    "  / \\  ",
    " /   \\ "
]

def displayWorkers(count):
    return "".join([line * count + "\n" for line in worker])
