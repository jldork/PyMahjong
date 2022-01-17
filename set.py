from typing import List
from tile import Tile

class Set:
    def __init__(self, tiles=List[Tile], visible=False):
        self.tiles = tiles
        self.suits = set([tile.suit for tile in self.tiles])
        self.numbers = set([tile.number for tile in self.tiles])
        self.type = self.check_type()
        self.visible = visible

    def check_pong(self) -> bool:
        return (
            len(self.suits) == 1 
            and 
            len(self.numbers) == 1 
            and 
            len(self.tiles) == 3
        )

    def check_kong(self) -> bool:
        return (
            len(self.suits) == 1 
            and 
            len(self.numbers) == 1 
            and 
            len(self.tiles) == 4
        )

    def check_chow(self) -> bool:
        return (
            len(self.suits) == 1 
            and 
            self.numbers in [
                set([x,x+1,x+2]) for x in range(1,8)
            ]
        )

    def check_type(self) -> str:
        if self.check_pong():
            return 'PONG'
        elif self.check_kong():
            return 'KONG'
        elif self.check_chow():
            return 'CHOW'