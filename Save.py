
import Player, Globals


def loadData():
    with open("save.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]

    if lines[0] == "tutorial":
        return True
    
    Player.tool = int(lines[1])
    Player.addCoins(int(lines[2]))

    for index, ore in enumerate(Globals.ores):
        (oreCount, workersCount) = lines[3 + index].split(",")
        Player.ores[ore] = int(oreCount)
        Player.workers[ore] = int(workersCount)


def saveData(tutorial=False):
    save = f"""{"tutorial" if tutorial else "game"}
{Player.tool}
{Player.coins}
{Player.ores["mud"]},{Player.workers["mud"]}
{Player.ores["stone"]},{Player.workers["stone"]}
{Player.ores["copper"]},{Player.workers["copper"]}
{Player.ores["iron"]},{Player.workers["iron"]}
{Player.ores["gold"]},{Player.workers["gold"]}
{Player.ores["diamond"]},{Player.workers["diamond"]}
{Player.ores["emerald"]},{Player.workers["emerald"]}
{Player.ores["ruby"]},{Player.workers["ruby"]}
{Player.ores["sapphire"]},{Player.workers["sapphire"]}"""
    
    with open("save.txt", "w") as file:
        file.write(save)


def resetData():
    Player.tool = 0
    Player.coins = 0
    
    for ore in Globals.ores:
        Player.ores[ore] = 0
        Player.workers[ore] = 0

    saveData(True)
