import json, globals
import pygameAddons.pygameaddons as game
from block.block import Block

class MapReader:
    def __init__(self, mapPath: str) -> None:
        self.mapPath = mapPath
        self.xOffset = 0
        self.yOffset = 0
        
    def openAndReadFile(self):
        with open(self.mapPath) as filePath:
            globals.mapData = json.load(filePath)
        
    def isolateVisableTerrain(self):
        globals.renderdMapData = []
        widthRange = (round(globals.playerPosition[0] - 25), round(globals.playerPosition[0] + 27))
        heightRange = (round(globals.playerPosition[1] - 15), round(globals.playerPosition[1] + 15))
        self.xOffset = (globals.playerPosition[0] - 30) - round(globals.playerPosition[0] - 30)
        self.yOffset = (globals.playerPosition[1] - 15) - round(globals.playerPosition[1] - 15)

        for height in range(*heightRange):
            widthList = []
            for width in range(*widthRange):
                widthList.append(Block(globals.mapData[height][width], width, height))
            globals.renderdMapData.append(widthList)
