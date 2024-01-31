import json, globals
import pygameAddons.pygameaddons as game

class MapReader:
    def __init__(self, mapPath: str) -> None:
        self.mapPath = mapPath
        self.mapData = None
        self.renderdMapData = None
        
    def openAndReadFile(self):
        with open(self.mapPath) as filePath:
            self.mapData = json.load(filePath)
        
    def isolateVisableTerrain(self):
        pass