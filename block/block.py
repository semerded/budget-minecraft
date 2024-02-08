import pygameAddons.pygameaddons as game
import globals

class Block:
    def __init__(self, blockType, xInMainMatrix, yInMainMatrix) -> None:
        self.color = globals.TERRAIN_TEXTURE[blockType]
        self.rect = game.pygame.Rect(0,0, 0, 0)
        self.mainMatrixPos = (xInMainMatrix, yInMainMatrix)
        
    def place(self, x, y, xOffset, yOffset):
        if not self.isAir():
            self.pos = (x, y)
            self.rect = game.Drawing.rectangle((self.pos[0] * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * xOffset) , (self.pos[1] * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * yOffset), game.ScreenUnit.vw(2), game.ScreenUnit.vw(2), self.color)
            game.Drawing.border(1, self.rect, game.Color.BLACK)

    @property
    def getRect(self):
        return self.rect
    
    @property
    def getMainPos(self):
        return self.mainMatrixPos
    
    def isAir(self):
        return self.color == None
            