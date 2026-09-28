
import Globals, time

layer = 0

def updateLayer(newLayer):
    global layer
    layer = newLayer
    print(f"You are now on layer: {Globals.oreLayers[layer].upper()}")

def digDown():
    if -tool <= layer and layer > -9:
        updateLayer(layer - 1)
    else:
        print("You do not have the required tool to dig down.")

def moveUp():
    if layer < 0:
        updateLayer(layer + 1)
    else:
        print("Unable to go any higher.")


coins = 0

def addCoins(count):
    global coins
    coins += count


tool = 0


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

def addOre(ore):
    global ores
    ores[ore] += 1


workers = {
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


lastWorker = time.time()

def updateTime():
    global lastWorker
    lastWorker = time.time()
