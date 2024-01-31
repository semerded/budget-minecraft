from enum import Enum



class Character:
    def __init__(self, hp) -> None:
        self.maxhp = hp
        self.hp = hp
        self.alive = True
        
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
    
  