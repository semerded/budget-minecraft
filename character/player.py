from character.baseCharacter import BaseCharacter
import pygameAddons.pygameaddons as game

class Player(BaseCharacter):
    def __init__(self, hp, texturePath: str) -> None:
        super().__init__(hp, texturePath)
  