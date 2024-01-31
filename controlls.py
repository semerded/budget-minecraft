import pygameAddons.pygameaddons as game


class Controlls:
    def __init__(self, GAME: game.AppConstructor) -> None:
        self.GAME = GAME
        
    def checkForInput(self):
        if self.GAME.keyboardClick(game.pygame.K_LEFT, game.pygame.K_q):
            pass
            
        if self.GAME.keyboardClick(game.pygame.K_RIGHT, game.pygame.K_d):
            pass