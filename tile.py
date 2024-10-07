# Class representing a Carcassonne tile
from enum import Enum

class Tile:

    # TODO: Create a side enum representing what is on a side, ie. road, city, field
    # TODO: create optional field of a tile for "special building" ie monastery or village

    Side = Enum('Side', ['ROAD', 'CITY', 'FIELD'])

    # Fields representing the area connected on each side of the tile
    # From the options of city, road, field
    # Optionally tile contains monastery or village
    # Each of the fields is a Side
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    # Function to rotate tiles
    def rotate_tile(self):
        temp_top = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = temp_top

