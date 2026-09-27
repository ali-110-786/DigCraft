
import Globals, Player, Shop, random


def tutorial():
    action = ""
    print("Enter 'd' to dig down.")
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

        mine()

        mud = Player.ores["mud"]
        coins = Player.coins
        if mud >= 3:
            if coins >= 2:
                print("You have enough mud and coins to buy a mud pickaxe.")
            else:
                print(f"Earn {2 - coins} more coins to buy a mud pickaxe.")
        else:
            if coins >= 2:
                print(f"Mine {3 - mud} more mud to buy a mud pickaxe.")
            else:
                print(f"Mine {3 - mud} more mud and {2 - coins} more coins to buy a mud pickaxe.")

    action = ""
    print("Enter 's' to enter the shop.")
    while action != "s":
        action = input().lower()

    Shop.shop() # Placeholder: buy mud pickaxe
    Player.tool = 1

    game()


def game():
    if Player.layer == 0:
        action = ""
        print("Enter 'd' to dig down or 's' to enter the shop.")
        while action != "d" and action != "s":
            action = input().lower()

        if action == "d":
            Player.digDown()
            game()
        else:
            Shop.shop() # Placeholder
    else:
        action = ""
        print("Enter 'd' to dig down, 'u' to go up, 'm' to mine or 's' to enter the shop.")
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
        else:
            Shop.shop() # Placeholder


def mine():
    if Player.layer < 0:
        ore = Globals.oreLayers[Player.layer]
        oreMined = True if random.randint(0, 100) < (23 + 2 * Player.layer) else False
        if oreMined:
            Player.addOre(ore)
            print(f"You mined 1 {ore}!")
        else:
            Player.addCoins(1)
            print("You earned 1 coin.")


if __name__ == "__main__":
    tutorial()
