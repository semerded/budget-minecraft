import json
import pygameAddons.pygameaddons as game

class MapReader:
    def __init__(self, mapPath: str) -> None:
        self.mapPath = mapPath
        self.mapData = None
        self.currentPosition = [10, 5]
        self.renderdMapData = None
        
    def openAndReadFile(self):
        with open(self.mapPath) as filePath:
            self.mapData = json.load(filePath)
            
    def getPosition(self, playerPosX: int, playerPosY: int):
        self.currentPosition = [playerPosX, playerPosY]
        
    def isolateVisableTerrain(self):
        pass