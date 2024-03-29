from enum import Enum
import pygameAddons.pygameaddons as game
from math import ceil, floor
import globals

class BaseCharacter:
    jumpFrameCounter = 0
    JUMP_FOR_AMOUNT_OF_FRAMES = 20
    jumping = False
    alive = True

    
    def __init__(self, GAME: game.AppConstructor, hp, texturePath: str) -> None:
        self.GAME = GAME
        self.maxhp = hp
        self.hp = hp
        self.characterImage = game.Image(texturePath)
        self.characterImage.resize(game.ScreenUnit.vw(2), game.ScreenUnit.vw(4))

    def moveLeft(self):
        pass
    
    def moveRight(self):
        pass
    
    def jump(self):
        if self.jumping:
            self._checkHeadCollision()
            self.jumpFrameCounter += 1
        if self.jumpFrameCounter == self.JUMP_FOR_AMOUNT_OF_FRAMES:
            self.jumpFrameCounter = 0
            self.jumping = False
        self.GAME.requestUpdate

        
    
    def updateHealth(self, difference: int):
        self.hp += difference
        self.checkHealth()
        
    def checkHealth(self):
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        if self.hp <= 0:
            self.dead()
    
    def dead(self):
        self.alive = False
        
    def characterHandler(self):
        # texture path
        self.groundCharacter()
        self._roundGroundPosition()
        self.characterImage.place(game.ScreenUnit.vw(50), game.ScreenUnit.vw(28))

    
    def groundCharacter(self):
        if not self.jumping:
            if not self.isCharacterOnGround():
                globals.playerPosition[1] += 0.35
                self.GAME.requestUpdate
                
                
    def isCharacterOnGround(self):
        return globals.mapData[floor(globals.playerPosition[1] + 1)][floor(globals.playerPosition[0])] != 0 or globals.mapData[floor(globals.playerPosition[1] + 1)][ceil(globals.playerPosition[0])] != 0
    
    def _roundGroundPosition(self):
        if not self.jumping and self.isCharacterOnGround():
            globals.playerPosition[1] = floor(globals.playerPosition[1])
            
    def _checkHeadCollision(self):
        if globals.mapData[ceil(globals.playerPosition[1] - 2)][floor(globals.playerPosition[0])] != 0 or globals.mapData[ceil(globals.playerPosition[1] - 2)][ceil(globals.playerPosition[0])] != 0 :
            self.jumping = False
            self.jumpFrameCounter = 0
    
  