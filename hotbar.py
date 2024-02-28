import pygameAddons.pygameaddons as game 
import globals, json

class HotBarItem:
    def __init__(self, id: int) -> None:
        self._getItemData(id)
        self.id = id
        
    def _getItemData(self, id: int):
        with open("block/blockList.json") as fp:
            blockData = json.load(fp)
        self.image = game.Image(blockData[id]["image"])
        self.image.resize(game.ScreenUnit.vw(2.5), game.ScreenUnit.vw(2.5))
        self.image.convert()
        
    def place(self, index):
        self.image.place(game.ScreenUnit.vw(32.5) + (game.ScreenUnit.vw(4) * index), game.ScreenUnit.vh(92) + game.ScreenUnit.vw(1))
    
class HotBar:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
        self.hotbarBorderColor = [[250, True], [170, False], [85, False]]
        self.selectedHotSlot = 0
        self.hotbarRects = []
        self.blocksLinkedToHotbarSlot = [HotBarItem(1), HotBarItem(2), HotBarItem(8), HotBarItem(5), HotBarItem(3), HotBarItem(4), HotBarItem(7), HotBarItem(17), HotBarItem(20)]
        
    def draw(self):
        self._rgb()
        self.hotbarRects = []
        for index in range(9):
            rect = game.Drawing.rectangle(game.ScreenUnit.vw(32) + (game.ScreenUnit.vw(4) * index), game.ScreenUnit.vh(92) + game.ScreenUnit.vw(0.5), game.ScreenUnit.vw(3.5), game.ScreenUnit.vw(3.5))
            self.blocksLinkedToHotbarSlot[index].place(index)
            if index == self.selectedHotSlot:
                self.hotbarRects.append(game.Drawing.border(int(game.ScreenUnit.vw(0.5)), rect, game.Color.WHITE))
            else:
                self.hotbarRects.append(game.Drawing.border(int(game.ScreenUnit.vw(0.5)), rect, self.getHotbarColor))
            
            if game.Interactions.isHoldingInRect(rect, game.mouseButton.leftMouseButton):
                globals.blockInHand = self.blocksLinkedToHotbarSlot[index].id
                self.selectedHotSlot = index
                # self.GAME.requestUpdate
        game.pygame.display.update(self.hotbarRects)
                    
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