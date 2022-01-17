class Tile:
    def __init__(self, suit:str, number:int):
        self.suit = suit
        self.number = number

    def __repr__(self) -> str:
        mapping = {
            'SEASON': ['SPRING', 'SUMMER', 'AUTUMN', 'WINTER'],
            'FLOWER': ['PLUM', 'LILY', 'CHRYSANTHEMUM', 'BAMBOO'],
            'WIND': ['EAST', 'SOUTH', 'WEST', 'NORTH'],
            'DRAGON': ['GREEN', 'RED', 'BLUE']
        }
        if self.suit in ['BAMBOO', 'DOT', 'CHARACTER']:
            return f'{self.suit}: {self.number}'
        else:
            return f'{mapping.get(self.suit)[self.number - 1]} {self.suit}'