import random

map = []
mapLayer = []

height = 128
width = 2560

for heightLayer in range(height):
    for widthLayer in range(width):
        if heightLayer >= 61:
            mapLayer.append(0)

        elif heightLayer == 60:
            mapLayer.append(1)

        elif heightLayer <= 59:
            mapLayer.append(random.randint(1,26))

        elif heightLayer <= 40 and heightLayer >= 1:
            mapLayer.append(random.randint(1,26))

        elif heightLayer <= 10:
            chanceOnObamium = random.randint(0,499)

            if chanceOnObamium == 0:
                mapLayer.append("Obamium")

            elif chanceOnObamium != 0:
                mapLayer.append(random.randint(1,26))
    
        elif heightLayer >= 0:
            mapLayer.append("Bedrock")
    map.append(mapLayer)