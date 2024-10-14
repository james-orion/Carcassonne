# Class representing a Carcassonne tile
from enum import Enum
import arcade

class Side(Enum):
    ROAD = 1
    CITY = 2
    FIELD = 3

class Building(Enum):
    VILLAGE = 1
    MONASTERY = 2
    NONE = 3

'''Tile Class'''
class Tile:

    # Fields representing the area connected on each side of the tile
    # From the options of city, road, field
    # Optionally tile contains monastery or village
    # Each of the fields is a Side

    def __init__(self, top: Side, bottom: Side, left: Side, right: Side, building: Building = 'NONE', meeple: Meeple = None, shield = False, is_connected = True):
        """Constructor
                Takes in four Sides of a tile: top, bottom, left, right, and a building
                These are Enums,
                    Side has options, 'ROAD', 'CITY', 'FIELD',
                    Building has options, 'VILLAGE', 'MONASTERY', 'NONE'
                Also has a meeple that can be played on the tile """
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.building = building
        self.meeple = meeple
        self.shield = shield
        self.is_connected = is_connected

    # Getters
    def get_top(self):
        """Method to return the top side of a tile"""
        return self.top

    def get_left(self):
        """Method to return the left side of a tile"""
        return self.left

    def get_right(self):
        """Method to return the right side of a tile"""
        return self.right

    def get_bottom(self):
        """Method to return the bottom side of a tile"""
        return self.bottom

    def get_building(self):
        """Method to return the building attached to a tile"""
        return self.building

    def has_shield(self):
        """Method to check if the tile has a shield"""
        return self.shield

    def is_connected(self):
        """Method to check if the tile has a connected city"""
        return self.is_connected

    # Setters
    def set_top(self, new_top: Side):
        """Method to set the value of the top side of a tile"""
        self.top = new_top

    def set_left(self, new_left: Side):
        """Method to set the value of the left side of a tile"""
        self.left = new_left

    def set_right(self, new_right: Side):
        """Method to set the value of the right side of a tile"""
        self.right = new_right

    def set_bottom(self, new_bottom: Side):
        """Method to set the value of the bottom side of a tile"""
        self.bottom = new_bottom

    def set_building(self, new_building: Building):
        """Method to set the value of the building attached to a tile"""
        self.building = new_building

    def add_shield(self):
        """Method to add a shield to the tile"""
        self.shield = True

    def remove_shield(self):
        """Method to remove a shield from the tile"""
        self.shield = False

    def set_connected(self):
        """Method to set a city as connected in a tile"""
        self.is_connected = True

    def not_connected(self):
        """Method to set a city as not connected in a tile"""
        self.is_connected = False

    # Function to rotate tiles
    def rotate_tile(self):
        """Method to rotate a tile one side in a counter-clockwise direction"""
        temp_top = self.get_top()
        self.set_top(self.get_right())
        self.set_right(self.get_bottom())
        self.set_bottom(self.get_left())
        self.set_left(temp_top)

# Create tiles for base game
# There are 72 tiles including one start tile
start = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD']) # x1
monastery_1 = Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], building = Building['MONASTERY']) # x2
monastery_2 = Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], building = Building['MONASTERY']) # x4
city_surrounded = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['CITY'], shield = True) # one of these
top_city_w_road = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD']) # x3
top_city = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD']) # x5
left_right_city_shield = Tile(top = Side['FIELD'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], shield = True) # x2
left_right_city = Tile(top = Side['FIELD'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD']) # x1
top_bottom_city = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['CITY'], is_connected = False) # x3


