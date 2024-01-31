import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color

GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME)
GAME.centerApp()

while True:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.BLUE)

    GAME.updateDisplay()