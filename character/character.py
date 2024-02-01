from enum import Enum
import pygameAddons.pygameaddons as game

class Character:
    def __init__(self, hp, texturePath: str) -> None:
        self.maxhp = hp
        self.hp = hp
        self.alive = True
        self.texturePath = texturePath
        
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
        game.Drawing.rectangle(game.ScreenUnit.vw(47.5), game.ScreenUnit.vw(30), game.ScreenUnit.vw(5), game.ScreenUnit.vw(10), game.Color.RED)
    
  