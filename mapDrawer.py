from mapReader import MapReader

class MapDrawer(MapReader):
    def __init__(self, mapPath: str) -> None:
        super().__init__(mapPath)
        
    def drawMap(self):
        