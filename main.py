import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from mapDrawer import MapDrawer
from character.player import Player
from controls import Controls
from hotbar import HotBar
from block.block import sizeBlockTextureList
import globals


GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME, manualUpdating=True)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()

sizeBlockTextureList()

mapDrawer = MapDrawer("map.json")

JAMAL = Player(GAME, 100, "")

controls = Controls(GAME)

hotbar = HotBar(GAME)

def printFPS():
    fps = GAME.clock.get_fps()
    game.Text.simpleText((5, 5), fps, color= Color.GREEN)
    game.Text.simpleText((5, 25), globals.playerPosition, color= Color.GREEN)


while 1:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.LIGHT_BLUE)  
    
    # menu?
        
    controls.readKeyboardKeys()   

    
    JAMAL.draw() 
    if GAME.firstFrame() or GAME.updateAvalible:
        mapDrawer.drawMap()
    hotbar.draw()
    
    printFPS()
    
    