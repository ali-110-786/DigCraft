
import Globals, Player, Shop, UI, random


def tutorial():
    action = ""
    UI.display("Enter 'd' to dig down.")
    while action != "d":
        action = input().lower()

    Player.digDown()

    mud = Player.ores["mud"]
    coins = Player.coins
    while mud < 3 or coins < 2:
        action = ""
        print("Enter 'm' to mine.")
        while action != "m":
            action = input().lower()

        output = mine()

        mud = Player.ores["mud"]
        coins = Player.coins
        if mud >= 3:
            if coins >= 2:
                UI.display(output, "You have enough mud and coins to buy a mud pickaxe.")
            else:
                UI.display(output, f"Earn {2 - coins} more coins to buy a mud pickaxe.")
        else:
            if coins >= 2:
                UI.display(output, f"Mine {3 - mud} more mud to buy a mud pickaxe.")
            else:
                UI.display(output, f"Mine {3 - mud} more mud and {2 - coins} more coins to buy a mud pickaxe.")

    action = ""
    print("Enter 's' to enter the shop.")
    while action != "s":
        action = input().lower()

    UI.display()
    outputs = Shop.tutorial()

    outputs += ("Congratulations! You completed the tutorial.",)

    UI.display(*outputs)

    game()


def game():
    Player.updateWorkers()
    
    if Player.layer == 0:
        action = ""
        print("Enter 'd' to dig down, 's' to enter the shop or 'q' to quit the game.")
        while action != "d" and action != "s":
            action = input().lower()

        if action == "d":
            Player.digDown()
            game()
        elif action == "s":
            Player.updateWorkers()
            UI.display()
            Shop.shop()
            game()
        elif action == "q":
            return
        else:
            game()
    else:
        action = ""
        print("Enter 'd' to dig down, 'u' to go up, 'm' to mine, 's' to enter the shop or 'q' to quit the game.")
        while action != "d" and action != "u" and action != "m" and action != "s":
            action = input().lower()

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
            Player.updateWorkers()
            UI.display()
            Shop.shop()
            game()
        elif action == "q":
            return
        else:
            game()


def mine():
    if Player.layer < 0:
        ore = Globals.oreLayers[Player.layer]
        oreMined = True if random.randint(0, 100) < (60 + 2 * Player.layer) else False
        if oreMined:
            Player.ores[ore] += 1
            UI.display(f"You mined 1 {ore}!")
            return f"You mined 1 {ore}!"
        else:
            Player.addCoins(1)
            UI.display("You earned 1 coin.")
            return "You earned 1 coin."


if __name__ == "__main__":
    tutorial()
