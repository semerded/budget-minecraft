from mapReader import MapReader
import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
import globals


class MapDrawer(MapReader):
    def __init__(self, mapPath: str) -> None:
        super().__init__(mapPath)
        self.openAndReadFile()
    
        
    def drawMap(self):
        self.isolateVisableTerrain()
        for y, blockRow in enumerate(globals.renderdMapData):
            for x, block in enumerate(blockRow):
                block.place(x, y,self.xOffset, self.yOffset)