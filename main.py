import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from mapDrawer import MapDrawer
from character.player import Player
from controls import Controls
import sys, globals


GAME = game.AppConstructor(game.ScreenUnit.dw(50),game.ScreenUnit.dh(50), game.pygame.NOFRAME)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()

mapDrawer = MapDrawer("map.json")

testCharacter = Player(GAME, 100, "")

controls = Controls(GAME)

while True:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.LIGHT_BLUE)
    
    # temp
    if GAME.keyboardClick(game.pygame.K_ESCAPE):
        sys.exit() 
    
    
    mapDrawer.drawMap()
    
    testCharacter.draw() 
    print(globals.mapData[round(globals.playerPosition[1])][round(globals.playerPosition[0])], globals.playerPosition)
    # globals.mapData[round(globals.playerPosition[1])][round(globals.playerPosition[0]) - 1] = 3
    controls.playerMovement()
    GAME.updateDisplay()