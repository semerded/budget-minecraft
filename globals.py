from pygameAddons.colors import Color
from block.block import makeBlockTextureList, Block





playerPosition = [50, 50]
mapData = []
renderdMapData = []
BLOCK_TEXTURES: list[Block] = []

makeBlockTextureList()

blockInHand = 1

playerJumpKey = False

generatedPlayerY = [14, 15]
generatedPlayerX = 25
playerRect = None

