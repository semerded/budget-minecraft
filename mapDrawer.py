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
        for heightIndex, row in enumerate(self.renderdMapData):
            for widthIndex, terrainColor in enumerate(row):
                if TERRAIN_TEXTURE[terrainColor] != None:
                    rect = game.Drawing.rectangle(widthIndex * game.ScreenUnit.vw(2) - (game.ScreenUnit.vw(2) * self.xOffset), heightIndex * game.ScreenUnit.vw(2) - (game.ScreenUnit.vw(2) * self.yOffset), game.ScreenUnit.vw(2), game.ScreenUnit.vw(2), TERRAIN_TEXTURE[terrainColor])
                    game.Drawing.border(1, rect, Color.BLACK)