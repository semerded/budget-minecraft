import pygameAddons.pygameaddons as game
import globals

from math import floor, ceil

class Controls:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
    
    def playerMovement(self):
        keyboard = game.pygame.key.get_pressed()
        
        if globals.mapData[floor(globals.playerPosition[1])][round(globals.playerPosition[0] - 0.60)] == 0 and globals.mapData[floor(globals.playerPosition[1] - 1)][ceil(globals.playerPosition[0] - 0.60)] == 0:
            if keyboard[game.pygame.K_LEFT] or keyboard[game.pygame.K_q]:
                globals.playerPosition[0] -= 0.10
        if globals.mapData[floor(globals.playerPosition[1])][round(globals.playerPosition[0] + 0.60)] == 0 and globals.mapData[floor(globals.playerPosition[1] - 1)][floor(globals.playerPosition[0] + 0.60)] == 0:
            if keyboard[game.pygame.K_RIGHT] or keyboard[game.pygame.K_d]:
                globals.playerPosition[0] += 0.10
                
    def playerJump(self):
        return self.GAME.keyboardClick(game.pygame.K_SPACE)
        