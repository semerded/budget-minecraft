import random, json

map = []

height = 290
width = 10

with open("block/blockList.json") as fp:
    mapdata = json.load(fp)

for heightLayer in range(height):
    mapLayer = []
    for widthLayer in range(width):
        if heightLayer <= 130:
            mapLayer.append(mapdata[0]["name"])

        elif heightLayer == 131:
            mapLayer.append(mapdata[1]['name'])

        elif heightLayer >= 132 and heightLayer <= 140:
            mapLayer.append(mapdata[2]['name'])

        elif heightLayer >= 246 and heightLayer < 253: 
            chanceOnObamium = random.randint(0,499)
            if chanceOnObamium == 333:
                mapLayer.append(mapdata[17]["name"])
            elif chanceOnObamium != 333:
                chanceOnRandomOre = random.randint(0,74)
                if chanceOnRandomOre == 0:
                    mapLayer.append(mapdata[random.randint(16,25)]["name"])
                else:
                    mapLayer.append(mapdata[8]["name"])

        elif heightLayer > 140 and heightLayer < 253:
            chanceOnRandomOre = random.randint(0,74)
            if chanceOnRandomOre == 0:
                mapLayer.append(mapdata[random.randint(16,25)]["name"])
            else:
                mapLayer.append(mapdata[8]["name"])
    
        elif heightLayer == 253:
            if random.randint(0,4) == 2:
                mapLayer.append(mapdata[9]["name"])
            else:
                mapLayer.append(mapdata[8]["name"])

        elif heightLayer == 254:
            if random.randint(0,2) == 2:
                mapLayer.append(mapdata[9]["name"])
            else:
                mapLayer.append(mapdata[8]["name"])
        
        elif heightLayer == 255 or heightLayer == 256:
            mapLayer.append(mapdata[9]["name"])

        elif heightLayer > 256:
            mapLayer.append(mapdata[0]["name"])

        map.append(mapLayer)
    print(map)