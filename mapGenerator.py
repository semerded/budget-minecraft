import random, json
from pyperclip import copy

map = []

height = 290
width = 100

with open("block/blockList.json") as fp:
    mapdata = json.load(fp)

for heightLayer in range(height):
    mapLayer = []
    for widthLayer in range(width):
        if heightLayer <= 130:
            mapLayer.append(mapdata[0]["id"])

        elif heightLayer == 131:
            mapLayer.append(mapdata[1]['id'])

        elif heightLayer >= 132 and heightLayer <= 140:
            mapLayer.append(mapdata[2]['id'])

        elif heightLayer >= 246 and heightLayer < 253: 
            chanceOnObamium = random.randint(0,499)
            if chanceOnObamium == 333:
                mapLayer.append(mapdata[17]["id"])
            elif chanceOnObamium != 333:
                chanceOnRandomOre = random.randint(0,74)
                if chanceOnRandomOre == 0:
                    mapLayer.append(mapdata[random.randint(16,25)]["id"])
                else:
                    mapLayer.append(mapdata[8]["id"])

        elif heightLayer > 140 and heightLayer < 253:
            chanceOnRandomOre = random.randint(0,74)
            if chanceOnRandomOre == 0:
                mapLayer.append(mapdata[random.randint(16,25)]["id"])
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
    
    map.append(mapLayer)
    # print(map)
    
copy(f"{map}")