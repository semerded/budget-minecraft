import json, globals
import pygameAddons.pygameaddons as game
from math import ceil, floor

class MapReader:
    def __init__(self, mapPath: str) -> None:
        self.mapPath = mapPath
        self.mapData: list = []
        self.renderdMapData: list = []
        self.xOffset = 0
        self.yOffset = 0
        
    def openAndReadFile(self):
        with open(self.mapPath) as filePath:
            self.mapData = json.load(filePath)
        
    def isolateVisableTerrain(self):
        self.renderdMapData = []
        widthRange = (ceil(globals.playerPosition[0] - 30), ceil(globals.playerPosition[0] + 30))
        heightRange = (ceil(globals.playerPosition[1] - 10), ceil(globals.playerPosition[1] + 21))
        self.xOffset = (globals.playerPosition[0] - 30) - floor(globals.playerPosition[0] - 30)
        self.yOffset = (globals.playerPosition[1] - 10) - floor(globals.playerPosition[1] - 10)
        for height in range(*heightRange):
            widthList = []
            for width in range(*widthRange):
                widthList.append(self.mapData[height][width])
            self.renderdMapData.append(widthList)
            # print(self.renderdMapData)
            # print("")