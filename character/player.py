from character.baseCharacter import BaseCharacter
from block.blockBreaking import BlockBreaking
from block.blockPlacing import BlockPlacing
import pygameAddons.pygameaddons as game
import globals

class Player(BaseCharacter):
    def __init__(self, GAME: game.AppConstructor, hp, texturePath: str) -> None:
        super().__init__(GAME, hp, texturePath)
        self.GAME = GAME
        self.blockBreaking = BlockBreaking(GAME)
        self.blockPlacing = BlockPlacing(GAME, game.pygame.Rect(game.ScreenUnit.vw(50), game.ScreenUnit.vw(28), game.ScreenUnit.vw(2), game.ScreenUnit.vw(4)))
        self.jumpCounter = 0
        
    def playerJump(self):
        if self.jumpCounter < 2 and globals.playerJumpKey:
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
        self.blockPlacing.checkForBlockPlace()
        self.playerJump()
        
        
    def _checkForValidBlockToBreak(self):
        if game.Interactions.isClicked(game.mouseButton.leftMouseButton):
            pass
        
    def breakBlock(self):
        pass
    