import random, json
from pyperclip import copy

map = []

height = 290
width = 1000

def generateTree(heightLayer, widthLayer):
        map[heightLayer -1][widthLayer] = mapdata[5]["id"]
        map[heightLayer -2][widthLayer] = mapdata[5]["id"]
        map[heightLayer -3][widthLayer] = mapdata[5]["id"]
        map[heightLayer -2][widthLayer-1] = mapdata[6]["id"]
        map[heightLayer -2][widthLayer-2] = mapdata[6]["id"]
        map[heightLayer -2][widthLayer+1] = mapdata[6]["id"]
        map[heightLayer -2][widthLayer+2] = mapdata[6]["id"]
        map[heightLayer -3][widthLayer-1] = mapdata[6]["id"]
        map[heightLayer -3][widthLayer+1] = mapdata[6]["id"]
        map[heightLayer -4][widthLayer] = mapdata[6]["id"]
        map[heightLayer -4][widthLayer-1] = mapdata[6]["id"]
        map[heightLayer -4][widthLayer+1] = mapdata[6]["id"]
        map[heightLayer -5][widthLayer] = mapdata[6]["id"]


def generateCave(heightLayer, widthLayer):
    if heightLayer > 150 and heightLayer < 230:
        chanceOnCaveSystem = random.randint(0,1000)
        if chanceOnCaveSystem == 1:
            pass

with open("block/blockList.json") as fp:
    mapdata = json.load(fp)

for heightLayer in range(height):
    mapLayer = []
    for widthLayer in range(width):
        if heightLayer <= 129:
            mapLayer.append(mapdata[0]["id"])

        elif heightLayer == 130:
            chanceOnTree = random.randint(0,20)
            if chanceOnTree == 1:
                mapLayer.append(mapdata[5]["id"])
            else:
                mapLayer.append(mapdata[0]["id"])

        elif heightLayer == 131:
            mapLayer.append(mapdata[1]['id'])

        elif heightLayer >= 132 and heightLayer <= 140:
            mapLayer.append(mapdata[2]['id'])

        elif heightLayer > 140 and heightLayer < 253:
            chanceOnRandomOre = random.randint(0,74)
            if chanceOnRandomOre == 0:
                mapLayer.append(mapdata[random.randint(10,25)]["id"])
            else:
                mapLayer.append(mapdata[8]["id"])

        elif heightLayer >= 246 and heightLayer < 253: 
            chanceOnObamium = random.randint(0,499)
            if chanceOnObamium == 333:
                mapLayer.append(mapdata[17]["id"])
            elif chanceOnObamium != 333:
                chanceOnRandomOre = random.randint(0,74)
                if chanceOnRandomOre == 0:
                    mapLayer.append(mapdata[random.randint(10,25)]["id"])
                else:
                    mapLayer.append(mapdata[8]["id"])
    
        elif heightLayer == 253:
            if random.randint(0,4) == 2:
                mapLayer.append(mapdata[9]["id"])
            else:
                mapLayer.append(mapdata[8]["id"])

        elif heightLayer == 254:
            if random.randint(0,2) == 2:
                mapLayer.append(mapdata[9]["id"])
            else:
                mapLayer.append(mapdata[8]["id"])
        
        elif heightLayer == 255 or heightLayer == 256:
            mapLayer.append(mapdata[9]["id"])

        elif heightLayer > 256:
            mapLayer.append(mapdata[0]["id"])

        if mapdata[5]["id"] in mapLayer:
            if mapLayer[-2] == mapdata[5]["id"]:
                mapLayer[-1] = mapdata[0]["id"]

        if mapdata[5]["id"] in mapLayer:
            if mapLayer[widthLayer] == mapdata[5]["id"]:
                generateTree(heightLayer, widthLayer)

    map.append(mapLayer)
    # print(map)
    
copy(f"{map}")