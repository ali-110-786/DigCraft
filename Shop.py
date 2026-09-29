
import Globals, Player, Game, UI


def shopInfo():
    print("""                TOOLS:                      WORKERS:                    COINS:
MUD:            3 mud + 2 coins             3 mud + 5 coins             1 coin
STONE:          4 stone + 8 coins           3 stone + 15 coins          3 coins
COPPER:         4 copper + 20 coins         3 copper + 40 coins         8 coins
IRON:           5 iron + 45 coins           3 iron + 90 coins           18 coins
GOLD:           5 gold + 100 coins          3 gold + 200 coins          40 coins
DIAMOND:        6 diamond + 250 coins       3 diamond + 500 coins       90 coins
EMERALD:        6 emerald + 600 coins       3 emerald + 1200 coins      180 coins
RUBY:           7 ruby + 1500 coins         3 ruby + 3000 coins         350 coins
SAPPHIRE:       8 sapphire + 4000 coins     3 sapphire + 7500 coins     700 coins
    """)


def tutorial():
    shopInfo()

    action = ""
    print("Enter 't' to buy the next tool.")
    while action != "t":
        action = input().lower()

    Player.ores["mud"] -= 3
    Player.coins -= 2
    Player.tool += 1

    outputs = ("""    _______
   /_______\\
      | |
      | |
      |_|
    """, f"You bought a mud pickaxe!")

    return outputs


def shop():
    shopInfo()

    print("Enter 't' to buy the next tool, 'w' to buy workers, 's' to sell ores or 'q' to leave the shop.")
    action = input().lower()

    outputs = ()
    
    if action == "t":
        if Player.tool == 9:
            print("You already have the best pickaxe.")
        else:
            ore = Globals.oreLayers[-(Player.tool + 1)]
            cost = Globals.toolCosts[ore]

            if Player.ores[ore] >= cost[0]:
                if Player.coins >= cost[1]:
                    Player.ores[ore] -= cost[0]
                    Player.coins -= cost[1]
                    Player.tool += 1

                    outputs += ("""    _______
   /_______\\
      | |
      | |
      |_|
                    """, f"You bought a{'n' if ore[0] in 'aeiou' else ''} {ore} pickaxe!")
                else:
                    outputs += (f"You need {cost[1] - Player.ores[ore]} more coins.",)
            elif Player.coins >= cost[1]:
                outputs += (f"You need {cost[0] - Player.ores[ore]} more {ore}.",)
            else:
                outputs += (f"You need {cost[0] - Player.ores[ore]} more {ore} and {cost[1] - Player.ores[ore]} more coins.",)
    elif action == "w":
        ore = ""
        print("Enter the level of worker to buy: Mud, Stone, Copper, Iron, Gold, Diamond, Emerald, Ruby or Sapphire.")
        while not ore in Globals.ores:
            ore = input().lower()

        count = ""
        print(f"Enter the number of {ore} workers to buy:")
        while not count.isdigit():
            count = input()
        count = int(count)

        cost = Globals.workerCosts[ore]

        if count == 0:
            pass
        elif Player.ores[ore] >= cost[0] * count:
            if Player.coins >= cost[1] * count:
                Player.updateWorkers()

                Player.ores[ore] -= cost[0] * count
                Player.addCoins(-(cost[1] * count))
                Player.workers[ore] += count

                for _ in range(count):
                    outputs += ("""       O
      /|\\
     / | \\
       |
      / \\
     /   \\
                    """,)

                outputs += (f"You bought {count} {ore} worker{'' if count == 1 else 's'}!",)
            else:
                outputs += (f"You need {cost[1] - Player.ores[ore]} more coins.",)
        elif Player.coins >= cost[1] * count:
            outputs += (f"You need {cost[0] - Player.ores[ore]} more {ore}.",)
        else:
            outputs += (f"You need {cost[0] - Player.ores[ore]} more {ore} and {cost[1] - Player.ores[ore]} more coins.",)
    elif action == "s":
        ore = ""
        print("Enter the ore to sell: Mud, Stone, Copper, Iron, Gold, Diamond, Emerald, Ruby or Sapphire.")
        while not ore in Globals.ores:
            ore = input().lower()

        count = ""
        print(f"Enter the amount of {ore} to sell:")
        while not count.isdigit():
            count = input()
        count = int(count)

        if count == 0:
            pass
        elif Player.ores[ore] >= count:
            coins = Globals.sellPrices[ore] * count
            Player.ores[ore] -= count
            Player.addCoins(coins)

            outputs += (f"You earned {coins} coin{'' if coins == 1 else 's'}!",)
        else:
            outputs += (f"You do not have enough {ore} to sell.",)
    elif action == "q":
        Player.updateWorkers()
        UI.display()
        return
    
    UI.display(*outputs)
    shop()


if __name__ == "__main__":
    shop()
    Game.game()
