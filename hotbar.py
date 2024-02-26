import pygameAddons.pygameaddons as game 
import globals

class HotBar:
    def __init__(self) -> None:
        self.hotbarBorderColor = [[250, True], [170, False], [85, False]]
        self.selectedHotSlot = 0
        self.blocksLinkedToHotbarSlot = [1, 2, 8, 5, 3, 4, 7, 17, 20]
    
    def draw(self):
        self._rgb()
        for index in range(9):
            rect = game.Drawing.rectangle(game.ScreenUnit.vw(32) + (game.ScreenUnit.vw(4) * index), game.ScreenUnit.vh(92) + game.ScreenUnit.vw(0.5), game.ScreenUnit.vw(3.5), game.ScreenUnit.vw(3.5))
            if index == self.selectedHotSlot:
                game.Drawing.border(int(game.ScreenUnit.vw(0.5)), rect, game.Color.WHITE)
            else:
                game.Drawing.border(int(game.ScreenUnit.vw(0.5)), rect, self.getHotbarColor)
            
            
            if game.Interactions.isHoldingInRect(rect, game.mouseButton.leftMouseButton):
                globals.blockInHand = self.blocksLinkedToHotbarSlot[index]
                self.selectedHotSlot = index
                
            
            
    def _rgb(self):
        for index in range(len(self.hotbarBorderColor)):
            if self.hotbarBorderColor[index][1]:
                self.hotbarBorderColor[index][0] += 1
                if self.hotbarBorderColor[index][0] >= 250:
                    self.hotbarBorderColor[index][1] = False
            else:
                self.hotbarBorderColor[index][0] -= 1
                if self.hotbarBorderColor[index][0] <= 5:
                    self.hotbarBorderColor[index][1] = True
                    
            

    @property  
    def getHotbarColor(self):
        returnValue = []
        for value in self.hotbarBorderColor:
            returnValue.append(value[0])
        return returnValue