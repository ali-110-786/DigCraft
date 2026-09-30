
import Globals, Player, Game, UI


def shopInfo():
    print(f"""{"":<12}{UI.BOLD}{"TOOLS:":<28}{"WORKERS:":<28}{"COINS:":<12}{UI.END}
{UI.BOLD}{UI.MUDTEXT}{"MUD:":<12}{UI.END}{UI.MUDTEXT}{"3 mud + 2 coins":<28}{"3 mud + 5 coins":<28}{"1 coin":<12}{UI.END}
{UI.BOLD}{UI.STONETEXT}{"STONE:":<12}{UI.END}{UI.STONETEXT}{"4 stone + 8 coins":<28}{"3 stone + 15 coins":<28}{"3 coins":<12}{UI.END}
{UI.BOLD}{UI.COPPERTEXT}{"COPPER:":<12}{UI.END}{UI.COPPERTEXT}{"4 copper + 20 coins":<28}{"3 copper + 40 coins":<28}{"8 coins":<12}{UI.END}
{UI.BOLD}{UI.IRONTEXT}{"IRON:":<12}{UI.END}{UI.IRONTEXT}{"5 iron + 45 coins":<28}{"3 iron + 90 coins":<28}{"18 coins":<12}{UI.END}
{UI.BOLD}{UI.GOLDTEXT}{"GOLD:":<12}{UI.END}{UI.GOLDTEXT}{"5 gold + 100 coins":<28}{"3 gold + 200 coins":<28}{"40 coins":<12}{UI.END}
{UI.BOLD}{UI.DIAMONDTEXT}{"DIAMOND:":<12}{UI.END}{UI.DIAMONDTEXT}{"6 diamond + 250 coins":<28}{"3 diamond + 500 coins":<28}{"90 coins":<12}{UI.END}
{UI.BOLD}{UI.EMERALDTEXT}{"EMERALD:":<12}{UI.END}{UI.EMERALDTEXT}{"6 emerald + 600 coins":<28}{"3 emerald + 1200 coins":<28}{"180 coins":<12}{UI.END}
{UI.BOLD}{UI.RUBYTEXT}{"RUBY:":<12}{UI.END}{UI.RUBYTEXT}{"7 ruby + 1500 coins":<28}{"3 ruby + 3000 coins":<28}{"350 coins":<12}{UI.END}
{UI.BOLD}{UI.SAPPHIRETEXT}{"SAPPHIRE:":<12}{UI.END}{UI.SAPPHIRETEXT}{"8 sapphire + 4000 coins":<28}{"3 sapphire + 7500 coins":<28}{"700 coins":<12}{UI.END}
    """)


def tutorial():
    shopInfo()

    action = ""
    print(UI.BOLD + "Enter 't' to buy the next tool." + UI.END)
    while action != "t":
        action = input().lower()

    Player.ores["mud"] -= 3
    Player.coins -= 2
    Player.tool += 1

    outputs = (UI.MUDTEXT + UI.displayPickaxe() + UI.END, UI.GREEN + f"You bought a {UI.END}{UI.MUDTEXT}mud{UI.END} {UI.GREEN}pickaxe!" + UI.END)

    return outputs


def shop():
    shopInfo()

    print(UI.BOLD + "Enter 't' to buy the next tool, 'w' to buy workers, 's' to sell ores or 'q' to leave the shop." + UI.END)
    action = input().lower()

    outputs = ()
    
    if action == "t":
        Player.updateWorkers()
        UI.display()

        if Player.tool == 9:
            print(UI.BOLD + "You already have the best pickaxe." + UI.END)
        else:
            ore = Globals.oreLayers[-(Player.tool + 1)]
            cost = Globals.toolCosts[ore]

            if Player.ores[ore] >= cost[0]:
                if Player.coins >= cost[1]:
                    Player.ores[ore] -= cost[0]
                    Player.coins -= cost[1]
                    Player.tool += 1

                    outputs += (UI.oreColours[ore] + UI.displayPickaxe() + UI.END, UI.GREEN + f"You bought a{'n' if ore[0] in 'aeiou' else ''} {UI.END}{UI.oreColours[ore]}{ore}{UI.END} {UI.GREEN}pickaxe!" + UI.END)
                else:
                    outputs += (UI.RED + f"You need {UI.END}{UI.YELLOW}{cost[1] - Player.coins} more coin{'' if cost[1] - Player.coins == 1 else 's'}{UI.END}{UI.RED} to buy a {UI.END}{UI.oreColours[ore]}{ore}{UI.END}{UI.RED} pickaxe." + UI.END,)
            elif Player.coins >= cost[1]:
                outputs += (UI.RED + f"You need {UI.END}{UI.oreColours[ore]}{cost[0] - Player.ores[ore]} more {ore}{UI.END}{UI.RED} to buy a {UI.END}{UI.oreColours[ore]}{ore}{UI.END}{UI.RED} pickaxe." + UI.END,)
            else:
                outputs += (UI.RED + f"You need {UI.END}{UI.oreColours[ore]}{cost[0] - Player.ores[ore]} more {ore}{UI.END}{UI.RED} and {UI.END}{UI.YELLOW}{cost[1] - Player.coins} more coin{'' if cost[1] - Player.coins == 1 else 's'}{UI.END}{UI.RED} to buy a {UI.END}{UI.oreColours[ore]}{ore}{UI.END}{UI.RED} pickaxe." + UI.END,)
    elif action == "w":
        Player.updateWorkers()
        UI.display()

        ore = ""
        print(UI.BOLD + f"Enter the level of worker to buy: {UI.END}{UI.MUDTEXT}mud{UI.END}, {UI.STONETEXT}stone{UI.END}, {UI.COPPERTEXT}copper{UI.END}, {UI.IRONTEXT}iron{UI.END}, {UI.GOLDTEXT}gold{UI.END}, {UI.DIAMONDTEXT}diamond{UI.END}, {UI.EMERALDTEXT}emerald{UI.END}, {UI.RUBYTEXT}ruby{UI.END} or {UI.SAPPHIRETEXT}sapphire{UI.END}{UI.BOLD}." + UI.END)
        while not ore in Globals.ores:
            ore = input().lower()

        count = ""
        print(UI.BOLD + f"Enter the number of {UI.END}{UI.oreColours[ore]}{ore}{UI.END} {UI.BOLD}workers to buy ('m' for max):" + UI.END)
        while not count.isdigit() and count != "m":
            count = input()

        cost = Globals.workerCosts[ore]

        if count == "m":
            oreCount = Player.ores[ore] // cost[0]
            coinsCount = Player.coins // cost[1]

            if oreCount == 0:
                if coinsCount == 0:
                    outputs += (UI.RED + f"You do not have enough {UI.END}{UI.oreColours[ore]}{ore}{UI.END}{UI.RED} or {UI.END}{UI.YELLOW}coins{UI.END}{UI.RED}." + UI.END,)
                else:
                    outputs += (UI.RED + f"You do not have enough {UI.END}{UI.oreColours[ore]}{ore}{UI.END}{UI.RED}." + UI.END,)
            elif coinsCount == 0:
                outputs += (UI.RED + f"You do not have enough {UI.END}{UI.YELLOW}coins{UI.END}{UI.RED}." + UI.END,)

            count = min(oreCount, coinsCount)
        else:
            count = int(count)
        
        if count == 0:
            pass
        elif Player.ores[ore] >= cost[0] * count:
            if Player.coins >= cost[1] * count:
                Player.updateWorkers()

                Player.ores[ore] -= cost[0] * count
                Player.addCoins(-(cost[1] * count))
                Player.workers[ore] += count

                outputs += (UI.oreColours[ore] + UI.displayWorkers(count) + UI.END, UI.GREEN + f"You bought {count} {UI.END}{UI.oreColours[ore]}{ore}{UI.END} {UI.GREEN}worker{'' if count == 1 else 's'}!" + UI.END)
            else:
                outputs += (UI.RED + f"You need {UI.END}{UI.YELLOW}{cost[1] - Player.coins} more coin{'' if cost[1] - Player.coins == 1 else 's'}{UI.END}{UI.RED}." + UI.END,)
        elif Player.coins >= cost[1]:
            outputs += (UI.RED + f"You need {UI.END}{UI.oreColours[ore]}{cost[0] - Player.ores[ore]} more {ore}{UI.END}{UI.RED}." + UI.END,)
        else:
            outputs += (UI.RED + f"You need {UI.END}{UI.oreColours[ore]}{cost[0] - Player.ores[ore]} more {ore}{UI.END}{UI.RED} and {UI.END}{UI.YELLOW}{cost[1] - Player.coins} more coin{'' if cost[1] - Player.coins == 1 else 's'}{UI.END}{UI.RED}." + UI.END,)
    elif action == "s":
        Player.updateWorkers()
        UI.display()

        ore = ""
        print(UI.BOLD + f"Enter the ore to sell: {UI.END}{UI.MUDTEXT}mud{UI.END}, {UI.STONETEXT}stone{UI.END}, {UI.COPPERTEXT}copper{UI.END}, {UI.IRONTEXT}iron{UI.END}, {UI.GOLDTEXT}gold{UI.END}, {UI.DIAMONDTEXT}diamond{UI.END}, {UI.EMERALDTEXT}emerald{UI.END}, {UI.RUBYTEXT}ruby{UI.END} or {UI.SAPPHIRETEXT}sapphire{UI.END}{UI.BOLD}." + UI.END)
        while not ore in Globals.ores:
            ore = input().lower()

        count = ""
        print(UI.BOLD + f"Enter the amount of {UI.END}{UI.oreColours[ore]}{ore}{UI.END} {UI.BOLD}to sell ('m' for max):" + UI.END)
        while not count.isdigit() and count != "m":
            count = input()

        cost = Globals.sellPrices[ore]

        if count == "m":
            count = Player.ores[ore]
            if count == 0:
                outputs += (UI.RED + f"You do not have enough {UI.END}{UI.oreColours[ore]}{ore}{UI.END}{UI.RED}." + UI.END,)
        else:
            count = int(count)

        if count == 0:
            pass
        elif Player.ores[ore] >= count:
            coins = Globals.sellPrices[ore] * count
            Player.ores[ore] -= count
            Player.addCoins(coins)

            outputs += (UI.GREEN + f"You sold {UI.END}{UI.oreColours[ore]}{count} {ore}{UI.END} {UI.GREEN}for {UI.END}{UI.YELLOW}{coins} coin{'' if coins == 1 else 's'}{UI.END}{UI.GREEN}!" + UI.END,)
        else:
            outputs += (UI.RED + f"You do not have enough {UI.END}{UI.oreColours[ore]}{ore}{UI.END} {UI.RED}to sell." + UI.END,)
    elif action == "q":
        Player.updateWorkers()
        UI.display()
        return
    
    UI.display(*outputs)
    shop()


if __name__ == "__main__":
    shop()
    Game.game()
