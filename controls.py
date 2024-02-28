import pygameAddons.pygameaddons as game
import globals, sys

from math import floor, ceil

class Controls:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
        self.keyboardEvents = game.pygame.key.get_pressed()
        
    def readKeyboardKeys(self):
        self.keyboardEvents = game.pygame.key.get_pressed()
        self.closeKey()
        self.playerMovement()
        self.playerJump()

    def closeKey(self):
        if self.keyboardEvents[game.pygame.K_ESCAPE]:
            game.pygame.quit()
            sys.exit()
    
    def playerMovement(self):
        
        if globals.mapData[floor(globals.playerPosition[1])][round(globals.playerPosition[0] - 0.60)] == 0 and globals.mapData[floor(globals.playerPosition[1] - 1)][ceil(globals.playerPosition[0] - 0.60)] == 0:
            if self.keyboardEvents[game.pygame.K_LEFT] or self.keyboardEvents[game.pygame.K_q]:
                globals.playerPosition[0] -= 0.10
                self.GAME.requestUpdate
        if globals.mapData[floor(globals.playerPosition[1])][round(globals.playerPosition[0] + 0.60)] == 0 and globals.mapData[floor(globals.playerPosition[1] - 1)][floor(globals.playerPosition[0] + 0.60)] == 0:
            if self.keyboardEvents[game.pygame.K_RIGHT] or self.keyboardEvents[game.pygame.K_d]:
                globals.playerPosition[0] += 0.10
                self.GAME.requestUpdate
                
                
    def playerJump(self):
        globals.playerJumpKey = self.keyboardEvents[game.pygame.K_SPACE]


        