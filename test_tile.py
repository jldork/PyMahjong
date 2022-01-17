from unittest import TestCase
from tile import TILES

class TileTest(TestCase):
    def test_tile_counts_are_correct(self):
        assert len(TILES) == 144

        for suit in ['BAMBOO', 'CHARACTER', 'DOT']:
            assert len([
                tile for tile in TILES if tile.suit == suit
            ]) == 36

        assert len([
            tile for tile in TILES if tile.suit == 'DRAGON'
        ]) == 12

        assert len([
            tile for tile in TILES if tile.suit == 'WIND'
        ]) == 16
