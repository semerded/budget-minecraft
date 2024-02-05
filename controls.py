import pygameAddons.pygameaddons as game
import globals


class Controls:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
    
    def playerMovement(self):
        keyboard = game.pygame.key.get_pressed()
        if keyboard[game.pygame.K_LEFT] or keyboard[game.pygame.K_q]:
            globals.playerPosition[0] -= 0.10
            
        if keyboard[game.pygame.K_RIGHT] or keyboard[game.pygame.K_d]:
            globals.playerPosition[0] += 0.10
            
    def playerJump(self):
        return self.GAME.keyboardClick(game.pygame.K_SPACE)
        