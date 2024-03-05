from pygameAddons.colors import Color
from block.block import makeBlockTextureList, Block
from block.blockBreakingAnimation import BlockBreakingAnimation






playerPosition = [500, 130]
mapData = []
renderdMapData = []
BLOCK_TEXTURES: list[Block] = []
BLOCK_BREAKING_TEXTURES = []
blockBreakingAnimation = BlockBreakingAnimation()

makeBlockTextureList()

blockInHand = 1

miningSpeedMultiplier = 1

requestNewRender = True
currentRenderedRange = [-1, -1]

playerJumpKey = False

generatedPlayerY = [14, 15]
generatedPlayerX = 25
playerRect = None

frameRenderRequested_debug = False

