# Class representing a Carcassonne tile
from enum import Enum
import arcade
'''Tile Class'''
class Tile:

    # TODO: Tiles have meeples attatched
    # TODO: check if tiles are connected to each other --- maybe board functionality

    Side = Enum('Side', ['ROAD', 'CITY', 'FIELD'])
    Building = Enum('Building', ['VILLAGE', 'MONASTERY', 'NONE'])

    # Fields representing the area connected on each side of the tile
    # From the options of city, road, field
    # Optionally tile contains monastery or village
    # Each of the fields is a Side
    '''Constructor
        Takes in four Sides of a tile: top, bottom, left, right, and a building
        These are Enums, 
            Side has options, 'ROAD', 'CITY', 'FIELD',
            Building has options, 'VILLAGE', 'MONASTERY', 'NONE'
        Also has a meeple that can be played on the tile
    '''
    def __init__(self, top: Side, bottom: Side, left: Side, right: Side, building: Building, meeple: Meeple = None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.building = building
        self.meeple = meeple

    # Getters
    '''Method to return the top side of a tile'''
    def get_top(self):
        return self.top

    '''Method to return the left side of a tile'''
    def get_left(self):
        return self.left

    '''Method to return the right side of a tile'''
    def get_right(self):
        return self.right

    '''Method to return the bottom side of a tile'''
    def get_bottom(self):
        return self.bottom

    '''Method to return the building attached to a tile'''
    def get_building(self):
        return self.building

    # Setters
    '''Method to set the value of the top side of a tile'''
    def set_top(self, new_top: Side):
        self.top = new_top

    '''Method to set the value of the left side of a tile'''
    def set_left(self, new_left: Side):
        self.left = new_left

    '''Method to set the value of the right side of a tile'''
    def set_right(self, new_right: Side):
        self.right = new_right

    '''Method to set the value of the bottom side of a tile'''
    def set_bottom(self, new_bottom: Side):
        self.bottom = new_bottom

    '''Method to set the value of the building attached to a tile'''
    def set_building(self, new_building: Building):
        self.building = new_building

    # Function to rotate tiles
    '''Method to rotate a tile one side in a counter-clockwise direction'''
    def rotate_tile(self):
        temp_top = self.get_top()
        self.set_top(self.get_right())
        self.set_right(self.get_bottom())
        self.set_bottom(self.get_left())
        self.set_left(temp_top)



