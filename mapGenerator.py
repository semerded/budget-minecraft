import random, json

map = []
mapLayer = []

height = 290
width = 100

with open("Blocks.json") as fp:
    mapdata = json.load(fp)

for heightLayer in range(height):
    for widthLayer in range(width):
        if heightLayer <= 130:
            mapLayer.append(mapdata["Surface"]["Air"])

        elif heightLayer == 131:
            mapLayer.append(mapdata["Surface"]["Grass"])

        elif heightLayer >= 246 and heightLayer < 253:
            chanceOnObamium = random.randint(0,499)
            if chanceOnObamium == 333:
                mapLayer.append(mapdata["Ores"]["Obamium"])
            elif chanceOnObamium != 0:
                chanceOnRandomOre = random.randint(0,74)
                if chanceOnRandomOre == 0:
                    mapdataOre = mapdata["Ores"]
                    mapLayer.append(random.choice( list(mapdataOre.items()))[1])
                else:
                    mapLayer.append(mapdata["Underground"]["Stone"])

        elif heightLayer >= 98 and heightLayer < 253:
            chanceOnRandomOre = random.randint(0,74)
            if chanceOnRandomOre == 0:
                mapdataOre = mapdata["Ores"]
                mapLayer.append(random.choice( list(mapdataOre.items()))[1])
            else:
                mapLayer.append(mapdata["Underground"]["Stone"])
    
        elif heightLayer == 253:
            if random.randint(0,4) == 2:
                mapLayer.append(mapdata["Underground"]["Bedrock"])
            else:
                mapLayer.append(mapdata["Underground"]["Stone"])

        elif heightLayer == 254:
            if random.randint(0,2) == 2:
                mapLayer.append(mapdata["Underground"]["Bedrock"])
            else:
                mapLayer.append(mapdata["Underground"]["Stone"])
        
        elif heightLayer == 255 or heightLayer == 256:
            mapLayer.append(mapdata["Underground"]["Bedrock"])

        elif heightLayer > 256:
            mapLayer.append(mapdata["Surface"]["Air"])








    print(mapLayer)
    map.append(mapLayer)