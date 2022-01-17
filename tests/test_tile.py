from unittest import TestCase
from tile import Tile

class TileTest(TestCase):
    def test_tile_has_suit_and_number(self):
        tile = Tile(suit='DRAGON', number=1)

        assert tile.suit == 'DRAGON'
        assert tile.number == 1
    
    def test_dragon_string_representation(self):
        green_dragon_tile = Tile(suit='DRAGON', number=1)
        assert green_dragon_tile.__repr__() == 'GREEN DRAGON'

        red_dragon_tile = Tile(suit='DRAGON', number=2)
        assert red_dragon_tile.__repr__() == 'RED DRAGON'

        blue_dragon_tile = Tile(suit='DRAGON', number=3)
        assert blue_dragon_tile.__repr__() == 'BLUE DRAGON'

    def test_wind_string_representation(self):
        east_wind_tile = Tile(suit='WIND', number=1)
        assert east_wind_tile.__repr__() == 'EAST WIND'

        south_wind_tile = Tile(suit='WIND', number=2)
        assert south_wind_tile.__repr__() == 'SOUTH WIND'

        west_wind_tile = Tile(suit='WIND', number=3)
        assert west_wind_tile.__repr__() == 'WEST WIND'

        north_wind_tile = Tile(suit='WIND', number=4)
        assert north_wind_tile.__repr__() == 'NORTH WIND'

    def test_wind_string_representation(self):
        east_wind_tile = Tile(suit='WIND', number=1)
        assert east_wind_tile.__repr__() == 'EAST WIND'

        south_wind_tile = Tile(suit='WIND', number=2)
        assert south_wind_tile.__repr__() == 'SOUTH WIND'

        west_wind_tile = Tile(suit='WIND', number=3)
        assert west_wind_tile.__repr__() == 'WEST WIND'

        north_wind_tile = Tile(suit='WIND', number=4)
        assert north_wind_tile.__repr__() == 'NORTH WIND'

    def test_season_string_representation(self):
        spring_tile = Tile(suit='SEASON', number=1)
        assert spring_tile.__repr__() == 'SPRING SEASON'

        summer_tile = Tile(suit='SEASON', number=2)
        assert summer_tile.__repr__() == 'SUMMER SEASON'

        autumn_tile = Tile(suit='SEASON', number=3)
        assert autumn_tile.__repr__() == 'AUTUMN SEASON'

        winter_tile = Tile(suit='SEASON', number=4)
        assert winter_tile.__repr__() == 'WINTER SEASON'

    def test_flower_string_representation(self):
        plum_tile = Tile(suit='FLOWER', number=1)
        assert plum_tile.__repr__() == 'PLUM FLOWER'

        lily_tile = Tile(suit='FLOWER', number=2)
        assert lily_tile.__repr__() == 'LILY FLOWER'

        chrysanthemum_tile = Tile(suit='FLOWER', number=3)
        assert chrysanthemum_tile.__repr__() == 'CHRYSANTHEMUM FLOWER'

        bamboo_tile = Tile(suit='FLOWER', number=4)
        assert bamboo_tile.__repr__() == 'BAMBOO FLOWER'


