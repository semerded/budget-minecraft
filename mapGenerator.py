import random

map = []
mapLayer = []

height = 128
width = 2560

for heightLayer in range(height):
    for widthLayer in range(width):
        mapLayer.append(random.randint())
    
    map.append(mapLayer)

print(map)