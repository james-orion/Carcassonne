# Class representing a Carcassonne tile
from enum import Enum
import arcade

class Tile:

    # TODO: Tiles have meeples attatched

    Side = Enum('Side', ['ROAD', 'CITY', 'FIELD'])
    Building = Enum('Building', ['VILLAGE', 'MONASTERY', 'NONE'])

    # Fields representing the area connected on each side of the tile
    # From the options of city, road, field
    # Optionally tile contains monastery or village
    # Each of the fields is a Side
    def __init__(self, top, bottom, left, right, building):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.building = building

    # Getters
    def get_top(self):
        return self.top

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_bottom(self):
        return self.bottom

    def get_building(self):
        return self.building

    # Setters
    def set_top(self, new_top):
        self.top = new_top

    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right

    def set_bottom(self, new_bottom):
        self.bottom = new_bottom

    def set_building(self, new_building):
        self.building = new_building

    # Function to rotate tiles
    def rotate_tile(self):
        temp_top = self.get_top()
        self.set_top(self.get_right())
        self.set_right(self.get_bottom())
        self.set_bottom(self.get_left())
        self.set_left(temp_top)
