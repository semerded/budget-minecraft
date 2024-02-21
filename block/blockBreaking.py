import globals
import pygameAddons.pygameaddons as game
from block.block import Block

class BlockBreaking:
    def __init__(self) -> None:
        self.blockBreakRadius = []
    
    def calculateBlockBreakingRadius(self):
        self.blockBreakRadius = []
        for height in range(globals.generatedPlayerY[0] - 5, globals.generatedPlayerY[0] + 6):
            widthList = []
            for width in range(globals.generatedPlayerX - 5, globals.generatedPlayerX + 6):
                widthList.append(globals.renderdMapData[height][width])
            self.blockBreakRadius.append(widthList)
            
    def checkForBlockBreak(self):
        if game.Interactions.isClicked(game.mouseButton.leftMouseButton):
            self.calculateBlockBreakingRadius()
            for blockList in self.blockBreakRadius:
                block: Block
                for block in blockList:
                    if game.Interactions.isMouseOver(block.getRect):
                        globals.mapData[block.getMainPos[1]][block.getMainPos[0]] = 0
                        return