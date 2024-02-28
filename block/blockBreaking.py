import globals
import pygameAddons.pygameaddons as game
from block.block import Block

class BlockBreaking:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
        self.blockBreakRadius = []
    
    def calculateBlockBreakingRadius(self):
        self.blockBreakRadius = []
        for height in range(globals.generatedPlayerY[0] - 5, globals.generatedPlayerY[0] + 6):
            widthList = []
            for width in range(globals.generatedPlayerX - 5, globals.generatedPlayerX + 6):
                widthList.append(globals.renderdMapData[height][width])
            self.blockBreakRadius.append(widthList)
            
    def checkForBlockBreak(self):
        if game.Interactions.isHolding(game.mouseButton.leftMouseButton):
            self.calculateBlockBreakingRadius()
            for blockList in self.blockBreakRadius:
                block: Block
                for block in blockList:
                    if game.Interactions.isMouseOver(block.getRect) and self._aroundAir(block.getMainPos):
                        self.GAME.requestUpdate  
                        globals.mapData[block.getMainPos[1]][block.getMainPos[0]] = 0
                        return
                    
    def _aroundAir(self, blockPosition):
        def _isNeighbourBlockAir(xOffset: int, yOffset: int):
            return globals.mapData[blockPosition[1] + yOffset][blockPosition[0] + xOffset] == 0
        return _isNeighbourBlockAir(0, 1) or _isNeighbourBlockAir(0, -1) or _isNeighbourBlockAir(1, 0) or _isNeighbourBlockAir(-1, 0)