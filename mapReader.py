import json, globals
import pygameAddons.pygameaddons as game

class MapReader:
    def __init__(self, mapPath: str) -> None:
        self.mapPath = mapPath
        self.mapData: list = []
        self.renderdMapData: list = []
        
    def openAndReadFile(self):
        with open(self.mapPath) as filePath:
            self.mapData = json.load(filePath)
        
    def isolateVisableTerrain(self):
        widthRange = (globals.playerPosition[0] - 11, globals.playerPosition[0] + 11)
        heightRange = (globals.playerPosition[1] - 5, globals.playerPosition[1] + 9)
        for height in range(*heightRange):
            widthList = []
            for width in range(*widthRange):
                widthList.append(self.mapData[height][width])
            self.renderdMapData.append(widthList)
            print(self.renderdMapData)
            print("")