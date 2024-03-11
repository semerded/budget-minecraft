import globals

class BlockBreakingAnimation:
    def __init__(self) -> None:
        self.rect = None
        self.imageNumber = None
        self.active = False   
    
    def setBlockBreakingAnimation(self, *args): # geen pyi file dus: imageNumber, (left, top)
        if len(args) == 2:
            self.active = True
            self.imageNumber = args[0]
            self.rect = args[1]
        else:
            self.active = False
            
        
    def place(self):
        if self.active:
            globals.BLOCK_BREAKING_TEXTURES[self.imageNumber - 1].place(self.rect.x, self.rect.y)
    
    