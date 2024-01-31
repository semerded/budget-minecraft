from mapReader import MapReader
import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
import globals

TERRAIN_TEXTURE = [None, Color.GREEN, Color.BROWN, Color.LIGHT_GRAY]

class MapDrawer(MapReader):
    def __init__(self, mapPath: str) -> None:
        super().__init__(mapPath)
        self.openAndReadFile()
    
        
    def drawMap(self):
        self.isolateVisableTerrain()
        self.renderdMapData = self.mapData
        for heightIndex, row in enumerate(self.renderdMapData):
            for widthIndex, terrainColor in enumerate(row):
                if TERRAIN_TEXTURE[terrainColor] != None:
                    game.Drawing.rectangle(widthIndex * game.ScreenUnit.vw(5), heightIndex * game.ScreenUnit.vw(5), game.ScreenUnit.vw(5), game.ScreenUnit.vw(5), TERRAIN_TEXTURE[terrainColor])