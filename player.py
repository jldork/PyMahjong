from wall import Wall

class Player:
    def __init__(self) -> None:
        self.special_tiles = {
            'SEASON': [],
            'FLOWER': []
        }
        self.direction = None
        self.hand = []
        self.sets = []

    def draw_from_wall(self, wall:Wall, back=False):
        drawn_tile = wall.draw_back() if back else wall.draw_front()
        self.hand += drawn_tile

    def declare_special_tiles(self, wall:Wall):
        starting_hand_length = len(self.hand)

        for i in range(len(self.hand)):
            if self.hand[i].type in ['FLOWER', 'SEASON']:
                special_tile = self.hand.pop(i)
                self.special_tiles[special_tile.type] += special_tile

        while self.hand < starting_hand_length:
            self.draw_from_wall(wall, back=True)

    def declare_set(self):
        




        