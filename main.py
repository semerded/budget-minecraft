import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from mapDrawer import MapDrawer


GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()

mapDrawer = MapDrawer("map.json")

while True:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.LIGHT_BLUE)
    
    mapDrawer.drawMap()

    GAME.updateDisplay()