import globals
import pygameAddons.pygameaddons as game
from block.block import Block

class BlockPlacing:
    def __init__(self, GAME: game.AppConstructor, playerRect = game.pygame.Rect) -> None:
        self.GAME = GAME
        self.playerRect = playerRect
        self.blockBreakRadius = []
    
    def calculateBlockPlacingRadius(self):
        self.blockBreakRadius = []
        for height in range(globals.generatedPlayerY[0] - 5, globals.generatedPlayerY[0] + 6):
            widthList = []
            for width in range(globals.generatedPlayerX - 5, globals.generatedPlayerX + 6):
                widthList.append(globals.renderdMapData[height][width])
            self.blockBreakRadius.append(widthList) 
    
    def _checkIfBlockCollidesWithPlayer(self, blockRect):
        return game.Interactions.rectInRect(self.playerRect, blockRect)
    
    def _checkIfBlockWouldBeLevitating(self, blockPosition: tuple):
        def _isNeighbourBlockAir(xOffset: int, yOffset: int):
            return globals.mapData[blockPosition[1] + yOffset][blockPosition[0] + xOffset] == 0
        return _isNeighbourBlockAir(0, 1) and _isNeighbourBlockAir(0, -1) and _isNeighbourBlockAir(1, 0) and _isNeighbourBlockAir(-1, 0)
            
            
            
    def checkForBlockPlace(self):
        if game.Interactions.isHolding(game.mouseButton.rightMouseButton):
            self.calculateBlockPlacingRadius()
            for blockList in self.blockBreakRadius:
                block: Block
                for block in blockList:
                    if block != None:
                        if game.Interactions.isMouseOver(block.getRect):
                            if globals.mapData[block.getMainPos[1]][block.getMainPos[0]] == 0 and not self._checkIfBlockCollidesWithPlayer(block.getRect) and not self._checkIfBlockWouldBeLevitating(block.getMainPos):
                                    self.GAME.requestUpdate
                                    globals.mapData[block.getMainPos[1]][block.getMainPos[0]] = globals.blockInHand
                            return
                    