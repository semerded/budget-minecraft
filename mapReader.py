import json, globals
import pygameAddons.pygameaddons as game
from block.block import Block

class MapReader:
    def __init__(self, mapPath: str) -> None:
        self.mapPath = mapPath
        self.xOffset = 0
        self.yOffset = 0
        
        
    def openAndReadFile(self):
        with open(self.mapPath) as filePath:
            globals.mapData = json.load(filePath)
        
    def isolateVisableTerrain(self):
        widthRange = (round(globals.playerPosition[0] - 25), round(globals.playerPosition[0] + 27))
        heightRange = (round(globals.playerPosition[1] - 15), round(globals.playerPosition[1] + 15))
        self.xOffset = (globals.playerPosition[0] - 30) - round(globals.playerPosition[0] - 30)
        self.yOffset = (globals.playerPosition[1] - 15) - round(globals.playerPosition[1] - 15)
        
        if globals.currentRenderedRange[0] != widthRange or globals.currentRenderedRange[1] != heightRange:
            globals.currentRenderedRange[0] = widthRange
            globals.currentRenderedRange[1] = heightRange
            globals.requestNewRender = True

        if globals.requestNewRender:
            globals.renderdMapData = []

            globals.frameRenderRequested_debug = True
            for height in range(*heightRange):
                widthList = []
                for width in range(*widthRange):
                    if self._subjectedToAir(width, height):
                        widthList.append(Block(globals.mapData[height][width], width, height))
                    else:
                        widthList.append(None)
                globals.renderdMapData.append(widthList)
            globals.requestNewRender = False

    def _subjectedToAir(self, xPos: int, yPos: int):
        def _isNeighbourBlockAir(xOffset: int, yOffset: int):
            return globals.mapData[yPos + yOffset][xPos + xOffset] == 0
        result = False
        for y in range(-2, 3):
            for x in range(-2, 3):
                if _isNeighbourBlockAir(x, y):
                    result = True
        return result
                    
        # return _isNeighbourBlockAir(0, 1) or _isNeighbourBlockAir(0, -1) or _isNeighbourBlockAir(1, 0) or _isNeighbourBlockAir(-1, 0) or _isNeighbourBlockAir(1, 1) or _isNeighbourBlockAir(1, -1) or _isNeighbourBlockAir(-1, 1) or _isNeighbourBlockAir(-1, -1)