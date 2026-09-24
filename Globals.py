
ores = {
    "mud": 0,
    "stone": 0,
    "copper": 0,
    "iron": 0,
    "gold": 0,
    "diamond": 0,
    "emerald": 0,
    "ruby": 0,
    "sapphire": 0
}

tool = 0

coins = 0

def addOre(ore):
    global ores
    ores[ore] += 1

def updateTool(toolId):
    global tool
    tool = toolId

def addCoins(count):
    global coins
    coins += count
