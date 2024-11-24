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

    def __init__(self, top: Side, bottom: Side, left: Side, right: Side, image, building: Building = Building['NONE'], shield = False, is_connected = True):
        """Constructor
                Takes in four Sides of a tile: top, bottom, left, right, and a building
                These are Enums,
                    Side has options, 'ROAD', 'CITY', 'FIELD',
                    Building has options, 'VILLAGE', 'MONASTERY', 'NONE'
                Also has a string representing the image of the tile """
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.building = building
        self.shield = shield
        self.is_connected = is_connected
        self.image = image
        self.meeple_placed_top = False
        self.meeple_placed_left = False
        self.meeple_placed_right = False
        self.meeple_placed_center = False
        self.meeple_placed_bottom = False

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

    def check_is_connected(self):
        """Method to check if the tile has a connected city"""
        return self.is_connected

    def get_image(self):
        """Method to return the image associated with a tile"""
        return self.image

    def get_meeple_placed_top(self):
        """Method to return whether a Meeple is placed on the top of a tile"""
        return self.meeple_placed_top

    def get_meeple_placed_left(self):
        """Method to return whether a Meeple is placed on the left of a tile"""
        return self.meeple_placed_left

    def get_meeple_placed_right(self):
        """Method to return whether a Meeple is placed on the right of a tile"""
        return self.meeple_placed_right

    def get_meeple_placed_center(self):
        """Method to return whether a Meeple is placed on the center of a tile"""
        return self.meeple_placed_center

    def get_meeple_placed_bottom(self):
        """Method to return whether a Meeple is placed on the bottom of a tile"""
        return self.meeple_placed_bottom

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

    def set_image(self, new_image):
        """Method to set the image associated with a tile"""
        self.image = new_image
    
    def set_meeple_placed_top(self, new_placement):
        """Method to place Meeple on top of tile"""
        self.meeple_placed_top = new_placement
    
    def set_meeple_placed_left(self, new_placement):
        """Method to place Meeple on left of tile"""
        self.meeple_placed_left = new_placement
    
    def set_meeple_placed_right(self, new_placement):
        """Method to place Meeple on right of tile"""
        self.meeple_placed_right = new_placement
    
    def set_meeple_placed_center(self, new_placement):
        """Method to place Meeple on center of tile"""
        self.meeple_placed_center = new_placement
    
    def set_meeple_placed_bottom(self, new_placement):
        """Method to place Meeple on bottom of tile"""
        self.meeple_placed_bottom = new_placement

    def copy(self):
        return Tile(top=self.top, left=self.left, bottom=self.bottom, right=self.right,
                    image=self.image, shield=self.shield, building=self.building, is_connected=self.is_connected)

    # Function to rotate tiles
    def rotate_tile(self):
        """Method to rotate a tile one side in a counter-clockwise direction"""
        temp_top = self.get_top()
        self.set_top(self.get_right())  # Top becomes right
        self.set_right(self.get_bottom())  # Right becomes bottom
        self.set_bottom(self.get_left())  # Bottom becomes left
        self.set_left(temp_top)  # Left becomes the original top
# Create tiles for base game

# There are 72 tiles including one start tile

#start not included in list of tiles because it needs to always be the first played, and the tiles list will be shuffled
start = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD'], image = 'images/img4.png') # x1

tiles = []

tiles.append(Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], building = Building['MONASTERY'], image = 'images/img1.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], building = Building['MONASTERY'], image = 'images/img1.png'))

tiles.append(Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], building = Building['MONASTERY'], image = 'images/img2.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], building = Building['MONASTERY'], image = 'images/img2.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], building = Building['MONASTERY'], image = 'images/img2.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], building = Building['MONASTERY'], image = 'images/img2.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['CITY'], shield = True, image = 'images/img3.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD'], image = 'images/img4.png'))
tiles.append( Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD'], image = 'images/img4.png'))
tiles.append( Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD'], image = 'images/img4.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], image = 'images/img5.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], image = 'images/img5.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], image = 'images/img5.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], image = 'images/img5.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], image = 'images/img5.png'))

tiles.append(Tile(top = Side['FIELD'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'images/img6.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'images/img6.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['CITY'], image = 'images/img7.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['CITY'], is_connected = False, image = 'images/img8.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['CITY'], is_connected = False, image = 'images/img8.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['CITY'], is_connected = False, image = 'images/img8.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['FIELD'], bottom = Side['FIELD'], is_connected = False, image = 'images/img9.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['FIELD'], bottom = Side['FIELD'], is_connected = False, image = 'images/img9.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'images/img10.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'images/img10.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'images/img10.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img11.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img11.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img11.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img12.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img12.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img12.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'images/img13.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'images/img13.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], image = 'images/img14.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], image = 'images/img14.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], image = 'images/img14.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], shield = True, image = 'images/img15.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], shield = True, image = 'images/img15.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'images/img16.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'images/img16.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'images/img16.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'images/img17.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], image = 'images/img18.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], image = 'images/img18.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], image = 'images/img18.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['ROAD'], shield = True, image = 'images/img19.png'))
tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['ROAD'], shield = True, image = 'images/img19.png'))

tiles.append(Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['ROAD'], image = 'images/img20.png'))

tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))
tiles.append(Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img21.png'))

tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'images/img22.png'))

tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img23.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img23.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img23.png'))
tiles.append(Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img23.png'))

tiles.append(Tile(top = Side['ROAD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'images/img24.png'))