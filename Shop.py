import Globals, Player
import time
def shop():
    print("""SHOP:
TOOLS:
MUD: 3 mud + 2 coins
STONE: 4 stone + 8 coins
COPPER: 4 copper + 20 coins
IRON: 5 iron + 45 coins
GOLD: 5 gold + 100 coins
DIAMOND: 6 diamond + 250 coins
EMERALD: 6 emerald + 600 coins
RUBY: 7 ruby + 1500 coins
SAPPHIRE: 8 sapphire + 4000 coins

WORKERS: (automated 10% ore)
MUD: 3 mud + 5 coins
STONE: 3 stone + 15 coins
COPPER: 3 copper + 40 coins+
IRON: 3 iron + 90 coins
GOLD: 3 gold + 200 coins
DIAMOND: 3 diamond + 500 coins
EMERALD: 3 emerald + 1200 coins
RUBY: 3 ruby + 3000 coins
SAPPHIRE: 3 sapphire + 7500 coins""")
    print("You have", Player.coins, "coins")
    choice=input("Tools, Workers or Sell ")
    if choice== "Tools":
        if Player.tool == 9:
            print("You already have the best pickaxe")
        else:
            ore = Globals.oreLayers[-(Player.tool + 1)]
            cost = Globals.toolCosts[ore]
            if Player.ores[ore] >= cost[0] and Player.coins >= cost[1]:
                Player.ores[ore] -= cost[0]
                Player.coins -= cost[1]
                Player.tool += 1
                print("""
    _______
   /_______\\
      | |
      | |
      |_|
      """)
                print("You bought a", ore, "pickaxe!")
            else:
                print("You need", cost[0], "ore and" , cost[1],  "coins to buy a", ore, "pickaxe")

