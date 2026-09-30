
import Globals, Player, Shop, UI, Save, random


def tutorial():
    action = ""
    UI.display(UI.HEADER + "Welcome to the tutorial!" + UI.END, UI.BOLD + "Enter 'd' to dig down." + UI.END)
    while action != "d":
        action = input().lower()

    Player.digDown()

    mud = Player.ores["mud"]
    coins = Player.coins
    while mud < 3 or coins < 2:
        action = ""
        print(UI.BOLD + "Enter 'm' to mine." + UI.END)
        while action != "m":
            action = input().lower()

        output = mine()

        mud = Player.ores["mud"]
        coins = Player.coins
        if mud >= 3:
            if coins >= 2:
                UI.display(output, UI.GREEN + f"You have enough {UI.END}{UI.MUDTEXT}mud{UI.END} {UI.GREEN}and {UI.END}{UI.YELLOW}coins{UI.END} {UI.GREEN}to buy a {UI.END}{UI.MUDTEXT}mud{UI.END} {UI.GREEN}pickaxe." + UI.END)
            else:
                UI.display(output, UI.RED + f"You need {UI.END}{UI.YELLOW}{2 - coins} more coin{'' if 2 - coins == 1 else 's'}{UI.END} {UI.RED}to buy a {UI.END}{UI.MUDTEXT}mud{UI.END} {UI.RED}pickaxe." + UI.END)
        else:
            if coins >= 2:
                UI.display(output, UI.RED + f"You need {UI.END}{UI.MUDTEXT}{3 - mud} more mud{UI.END} {UI.RED}to buy a {UI.END}{UI.MUDTEXT}mud{UI.END} {UI.RED}pickaxe." + UI.END)
            else:
                UI.display(output, UI.RED + f"You need {UI.END}{UI.MUDTEXT}{3 - mud} more mud{UI.END} {UI.RED}and {UI.END}{UI.YELLOW}{2 - coins} more coin{'' if 2 - coins == 1 else 's'}{UI.END} {UI.RED}to buy a mud pickaxe." + UI.END)

    action = ""
    print(UI.BOLD + "Enter 's' to enter the shop." + UI.END)
    while action != "s":
        action = input().lower()

    UI.display()
    outputs = Shop.tutorial()

    outputs += (UI.HEADER + "Congratulations! You completed the tutorial." + UI.END,)

    UI.display(*outputs)

    game()


def game():
    Player.updateWorkers()
    
    if Player.layer == 0:
        action = ""
        print(UI.BOLD + "Enter 'd' to dig down, 's' to enter the shop or 'q' to quit the game." + UI.END)
        while action != "d" and action != "s" and action != "q":
            action = input().lower()

        Player.updateWorkers()
        UI.display()

        if action == "d":
            Player.digDown()
            game()
        elif action == "s":
            Shop.shop()
            game()
        elif action == "q":
            Save.saveData()
        else:
            game()
    else:
        action = ""
        print(UI.BOLD + "Enter 'd' to dig down, 'u' to go up, 'm' to mine, 's' to enter the shop or 'q' to quit the game." + UI.END)
        while action != "d" and action != "u" and action != "m" and action != "s" and action != "q":
            action = input().lower()

        Player.updateWorkers()
        UI.display()

        if action == "d":
            Player.digDown()
            game()
        elif action == "u":
            Player.moveUp()
            game()
        elif action == "m":
            mine()
            game()
        elif action == "s":
            Shop.shop()
            game()
        elif action == "q":
            Save.saveData()
        else:
            game()


def mine():
    if Player.layer < 0:
        ore = Globals.oreLayers[Player.layer]
        oreMined = True if random.randint(0, 100) < (60 + 2 * Player.layer) else False
        if oreMined:
            Player.ores[ore] += 1
            UI.display(UI.GREEN + f"You mined {UI.END}{UI.oreColours[ore]}1 {ore}{UI.END}{UI.GREEN}!" + UI.END)
            return UI.GREEN + f"You mined {UI.END}{UI.oreColours[ore]}1 {ore}{UI.END}{UI.GREEN}!" + UI.END
        else:
            Player.addCoins(1)
            UI.display(UI.YELLOW + "You earned 1 coin." + UI.END)
            return UI.YELLOW + "You earned 1 coin." + UI.END


if __name__ == "__main__":
    if Save.loadData():
        tutorial()
    else:
        UI.display()

        action = ""
        print(UI.BOLD + "Enter 'p' to continue your current save or 'r' to restart the game:" + UI.END)
        while action != "p" and action != "r":
            action = input()

        if action == "r":
            Save.resetData()
            tutorial()
        else:
            UI.display()
            game()
