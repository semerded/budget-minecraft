import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from mapDrawer import MapDrawer
from character.player import Player
from controls import Controls
from hotbar import HotBar
import sys, globals


GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()

mapDrawer = MapDrawer("map.json")

testCharacter = Player(GAME, 100, "")

controls = Controls(GAME)

hotbar = HotBar()


while True:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.LIGHT_BLUE)
    
    # temp (wordt verandert met menu)
    if GAME.keyboardClick(game.pygame.K_ESCAPE):
        sys.exit() 
    
    controls.playerMovement()
    
    mapDrawer.drawMap()
    
    testCharacter.draw() 
    hotbar.draw()
    GAME.updateDisplay()
    