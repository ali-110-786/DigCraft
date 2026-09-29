
import Globals, UI, time

layer = 0

def updateLayer(newLayer):
    global layer
    layer = newLayer
    UI.display(f"You are now on layer: {Globals.oreLayers[layer].capitalize()}")

def digDown():
    if -tool <= layer and layer > -9:
        updateLayer(layer - 1)
    else:
        UI.display("You do not have the required tool to dig down.")

def moveUp():
    if layer < 0:
        updateLayer(layer + 1)
    else:
        UI.display("Unable to go any higher.")


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

def updateWorkers():
    global coins, ores, lastWorker
    timeElapsed = int(time.time() - lastWorker)
    
    for worker, count in workers.items():
        value = Globals.ores.index(worker) + 1
        otc = (23 - 2 * value) / 100
        coins += round(timeElapsed * value * count * (1 / otc))
        ores[worker] += round(timeElapsed * count * otc)
        
    updateTime()
