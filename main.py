import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from mapDrawer import MapDrawer
from character.player import Player
from controls import Controls
from hotbar import HotBar
from block.block import sizeBlockTextureList
import sys, globals


GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()

sizeBlockTextureList()

mapDrawer = MapDrawer("map.json")

testCharacter = Player(GAME, 100, "")

controls = Controls(GAME)

hotbar = HotBar()

def printFPS():
    fps = GAME.clock.get_fps()
    game.Text.simpleText((5, 5), fps, color= Color.GREEN)


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
    
    printFPS()
    
    GAME.updateDisplay()
    