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
        self.creativeKey()

    def closeKey(self):
        if self.keyboardEvents[game.pygame.K_ESCAPE]:
            game.pygame.quit()
            sys.exit()
    
    def playerMovement(self):
        
        if globals.mapData[floor(globals.playerPosition[1])][round(globals.playerPosition[0] - 0.60)] == 0 and globals.mapData[floor(globals.playerPosition[1] - 1)][ceil(globals.playerPosition[0] - 0.60)] == 0:
            if self.keyboardEvents[game.pygame.K_LEFT] or self.keyboardEvents[game.pygame.K_q]:
                globals.playerPosition[0] -= 0.1
                self.GAME.requestUpdate
        if globals.mapData[floor(globals.playerPosition[1])][round(globals.playerPosition[0] + 0.60)] == 0 and globals.mapData[floor(globals.playerPosition[1] - 1)][floor(globals.playerPosition[0] + 0.60)] == 0:
            if self.keyboardEvents[game.pygame.K_RIGHT] or self.keyboardEvents[game.pygame.K_d]:
                globals.playerPosition[0] += 0.1
                self.GAME.requestUpdate
                
                
    def playerJump(self):
        globals.playerJumpKey = self.keyboardEvents[game.pygame.K_SPACE]
        
    def creativeKey(self):
        if self.keyboardEvents[game.pygame.K_F3]:
            globals.miningSpeedMultiplier = 9999999999999999999999999 # om bedrock te breken
        if self.keyboardEvents[game.pygame.K_BACKSPACE]:
            globals.miningSpeedMultiplier = 1


        