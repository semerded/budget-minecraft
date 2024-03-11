from mapReader import MapReader
import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from block.block import Block
import globals


class MapDrawer(MapReader):
    def __init__(self, mapPath: str) -> None:
        super().__init__(mapPath)
        
    def drawMap(self):
        self.isolateVisableTerrain()
        for y, blockRow in enumerate(globals.renderdMapData):
            block : Block
            for x, block in enumerate(blockRow):
                if block == None:
                    rect = game.Drawing.rectangle((x * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * self.xOffset) , (y * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * self.yOffset), game.ScreenUnit.vw(2), game.ScreenUnit.vw(2), Color.BLACK)
                    game.Drawing.border(1, rect)
                else:
                    block.place(x, y,self.xOffset, self.yOffset)