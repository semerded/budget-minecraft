from enum import Enum
import pygameAddons.pygameaddons as game
from math import ceil
import globals

class BaseCharacter:
    def __init__(self, hp, texturePath: str) -> None:
        self.maxhp = hp
        self.hp = hp
        self.alive = True
        self.texturePath = texturePath
        self.jumping = False
        
    def moveLeft(self):
        pass
    
    def moveRight(self):
        pass
    
    def jump(self):
        pass
    
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
        
    def draw(self):
        # texture path
        self.groundCharacter()
        game.Drawing.rectangle(game.ScreenUnit.vw(47.5), game.ScreenUnit.vw(30), game.ScreenUnit.vw(2), game.ScreenUnit.vw(2), game.Color.RED)
    
    def groundCharacter(self):
        if not self.jumping:
            if globals.mapData[ceil(globals.playerPosition[1] + 1)][ceil(globals.playerPosition[0])] == 0:
                globals.playerPosition[1] += 0.10
    
  