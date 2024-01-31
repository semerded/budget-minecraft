import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color


GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()
print(GAME.getdisplayDimensions)

while True:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.BLUE)

    GAME.updateDisplay()