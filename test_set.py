from unittest import TestCase
from set import Set
from tile import Tile

class TestSet(TestCase):
    def test_set_pong(self):
        pong_set = Set(
            tiles = 3*[Tile(
                suit='DRAGON',
                number=1
            )]
        )

        assert pong_set.type == 'PONG'

    def test_set_kong(self):
        kong_set = Set(
            tiles = 4*[Tile(
                suit='WIND',
                number=1
            )]
        )

        assert kong_set.type == 'KONG'

    def test_set_chow(self):
        chow_tiles = [
            Tile(       
                suit='CHARACTER',
                number=2
            ),
            Tile(
                suit='CHARACTER',
                number=4
            ), 
            Tile(
                suit='CHARACTER',
                number=3
            )
        ]

        chow_set = Set(
            tiles = chow_tiles
        )

        assert chow_set.type == 'CHOW'

    def test_set_not_set(self):
        no_set_tiles = [
            Tile(
                suit='CHARACTER',
                number=1
            ),
            Tile(
                suit='BAMBOO',
                number=4
            ), 
            Tile(
                suit='CHARACTER',
                number=3
            )
        ]

        no_set_set = Set(
            tiles = no_set_tiles
        )

        assert no_set_set.type == None