from tile import Tile

STANDARD_TILES = 4*([
    Tile(suit=suit, number=number) 
    for suit in ['BAMBOO', 'DOT', 'CHARACTER']
    for number in range(1,10)
] + [
    Tile(suit='WIND', number=number)
    for number in range(1,5)
] + [
    Tile(suit='DRAGON', number=number)
    for number in range(1,4)
]) + [
    Tile(suit=suit, number=number)
    for suit in ['SEASON', 'FLOWER']   
    for number in range(1,5)
]

class Wall:
    def __init__(self, tiles=STANDARD_TILES):
        self.tiles = tiles

    def shuffle(self):
        """Also known as 'washing' tiles"""
        shuffled_tiles = self.tiles
        self.tiles = shuffled_tiles

    def draw_front(self) -> Tile:
        """Draw from the front for standard draw"""
        return self.tiles.pop(0)

    def draw_back(self) -> Tile:
        """Draw from the back, in the case of seasons and flowers"""
        return self.tiles.pop(-1)



    

