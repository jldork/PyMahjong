from unittest import TestCase
from wall import Wall
from tile import Tile

class WallTest(TestCase):
    def test_wall_initialized_with_all_tiles(self):
        wall = Wall()
        len(wall.tiles) == 144

    def test_wall_can_draw(self):
        wall = Wall()
        first_tile = wall.tiles[0]
        drawn_tile = wall.draw_front()
        assert isinstance(drawn_tile, Tile)
        assert len(wall.tiles) == 143
        assert drawn_tile == first_tile

        last_tile = wall.tiles[-1]
        drawn_tile = wall.draw_back()
        assert isinstance(drawn_tile, Tile)
        assert len(wall.tiles) == 142
        assert drawn_tile != first_tile
        assert drawn_tile == last_tile
