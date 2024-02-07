from character.baseCharacter import BaseCharacter
from controls import Controls
from block.blockBreaking import BlockBreaking
import pygameAddons.pygameaddons as game
import globals

class Player(BaseCharacter):
    def __init__(self, GAME: game.AppConstructor, hp, texturePath: str) -> None:
        super().__init__(hp, texturePath)
        self.controls = Controls(GAME)
        self.blockBreaking = BlockBreaking()
        self.jumpCounter = 0
    def playerJump(self):
        if self.jumpCounter < 2 and self.controls.playerJump():
            self.jumping = True
            self.jumpFrameCounter = 0
            self.jumpCounter += 1
     
        
        if self.jumping:
            self.jump()
            globals.playerPosition[1] -= 0.27
        if self.isCharacterOnGround():
            self.jumpCounter = 0
            
    def draw(self):
        self.characterHandler()
        self.blockBreaking.checkForBlockBreak()
        self.playerJump()
        
    def _checkForValidBlockToBreak(self):
        if game.Interactions.isClicked(game.mouseButton.leftMouseButton):
            pass
        
    def breakBlock(self):
        pass
    