import pygameAddons.pygameaddons as game
from pygameAddons.colors import Color
from mapGenerator import generateMap
from mapDrawer import MapDrawer
from character.player import Player
from controls import Controls
from hotbar import HotBar
from block.block import sizeBlockTextureList, loadBlockBreakingTextures
import globals

"""
lees de readme!
"""


GAME = game.AppConstructor(game.ScreenUnit.dw(100),game.ScreenUnit.dh(100), game.pygame.NOFRAME, manualUpdating=True)
GAME.setAspectratio(game.ScreenUnit.aspectRatio(game.aspectRatios.ratio16to9))
GAME.centerApp()

titleScreen = game.Image("titlescreen.png")
titleScreen.resize(game.ScreenUnit.vw(100), game.ScreenUnit.vh(100))
titleScreen.place(0, 0)
game.Text.simpleText((0, 0), "loading map, pls wait", game.Font.FONT100, Color.RED)
game.Updating.updateDisplay()

sizeBlockTextureList()
loadBlockBreakingTextures()

globals.mapData = generateMap(1000, 290)
mapDrawer = MapDrawer("map.json")

JAMAL = Player(GAME, 100, "character/jamal.png")

controls = Controls(GAME)

hotbar = HotBar(GAME)

def printFPS():
    fps = GAME.clock.get_fps()
    game.Text.simpleText((5, 5), round(fps, 2), color= Color.GREEN)
    game.Text.simpleText((5, 25), globals.playerPosition, color= Color.GREEN)
    game.Text.simpleText((5, 45), globals.frameRenderRequested_debug, color= Color.GREEN)
    globals.frameRenderRequested_debug = False
    game.pygame.display.update(game.pygame.Rect(5, 5, 50, 20))


while 1:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(Color.LIGHT_BLUE)  
    
    # menu?
        
    controls.readKeyboardKeys()   

    
    JAMAL.draw() 
    if GAME.firstFrame() or GAME.updateAvalible:
        mapDrawer.drawMap()
    globals.blockBreakingAnimation.place()
    hotbar.draw()
    
    printFPS()
    
    