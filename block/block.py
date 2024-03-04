import pygameAddons.pygameaddons as game
import globals, json

def makeBlockTextureList(): 
    with open("block/blockList.json") as fp:
        blockData = json.load(fp)
    for data in blockData:
        if data["image"] != None:
            blockDataDict = {"name": data["name"], "image": game.Image(data["image"]), "hardness": data["hardness"]}
            globals.BLOCK_TEXTURES.append(blockDataDict)
        else:
            blockDataDict = {"name": data["name"], "image": None, "hardness": 0}
            globals.BLOCK_TEXTURES.append(blockDataDict)


def loadBlockBreakingTextures():
    for index in range(8):
        imageNumber = index + 1
        globals.BLOCK_BREAKING_TEXTURES.append(game.Image("block/blockbreaking_textures/%s.png" %imageNumber))
        globals.BLOCK_BREAKING_TEXTURES[index].resize(game.ScreenUnit.vw(2), game.ScreenUnit.vw(2))

            
def sizeBlockTextureList():
    for index in range(len(globals.BLOCK_TEXTURES)):
        if index != 0:
            globals.BLOCK_TEXTURES[index]["image"].resize(game.ScreenUnit.vw(2), game.ScreenUnit.vw(2))
            globals.BLOCK_TEXTURES[index]["image"].convert()

class Block:
    def __init__(self, blockType: int, xInMainMatrix, yInMainMatrix) -> None:
        self.blockTexture: game.Image = globals.BLOCK_TEXTURES[blockType]["image"]
        self.name = globals.BLOCK_TEXTURES[blockType]["name"]
        self.hardness = globals.BLOCK_TEXTURES[blockType]["hardness"]

        self.rect = game.pygame.Rect(0,0, 0, 0)
        self.mainMatrixPos = (xInMainMatrix, yInMainMatrix)
        
    def place(self, x, y, xOffset, yOffset):
        self.rect = game.pygame.Rect((x * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * xOffset) , (y * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * yOffset), game.ScreenUnit.vw(2), game.ScreenUnit.vw(2))
        if not self.isAir():
            self.blockTexture.place(self.rect.x, self.rect.y)
            # self.rect = game.Drawing.rectangle((x * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * xOffset) , (y * game.ScreenUnit.vw(2)) - (game.ScreenUnit.vw(2) * yOffset), game.ScreenUnit.vw(2), game.ScreenUnit.vw(2), game.Color.GREEN)
            game.Drawing.border(1, self.rect, game.Color.BLACK)
        

    @property
    def getRect(self):
        return self.rect
    
    @property
    def getMainPos(self):
        return self.mainMatrixPos
    
    def isAir(self):
        return self.blockTexture == None
            