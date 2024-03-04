import globals
import pygameAddons.pygameaddons as game
from block.block import Block
from math import ceil

class BlockBreaking:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
        self.blockBreakRadius = []
        self.breakingTickCounter = 0
    
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
                    if block != None:
                        if game.Interactions.isMouseOver(block.getRect) and self._subjectedToAir(block.getMainPos):
                            self.GAME.requestUpdate
                            globals.requestNewRender = True
                            self.breakingTickCounter += 1
                            
                                                        
                            if self.breakingTickCounter >= (block.hardness / globals.miningSpeedMultiplier):
                                globals.mapData[block.getMainPos[1]][block.getMainPos[0]] = 0
                                self.breakingTickCounter = 0
                                globals.blockBreakingAnimation.setBlockBreakingAnimation(False)
                                return
                            globals.blockBreakingAnimation.setBlockBreakingAnimation(ceil((self.breakingTickCounter / block.hardness) * 8), block.getRect)
                            return
        else: 
            self.breakingTickCounter = 0
            globals.blockBreakingAnimation.setBlockBreakingAnimation(False)
        
                    
    def _subjectedToAir(self, blockPosition):
        def _isNeighbourBlockAir(xOffset: int, yOffset: int):
            return globals.mapData[blockPosition[1] + yOffset][blockPosition[0] + xOffset] == 0
        return _isNeighbourBlockAir(0, 1) or _isNeighbourBlockAir(0, -1) or _isNeighbourBlockAir(1, 0) or _isNeighbourBlockAir(-1, 0)