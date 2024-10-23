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

#start not included in list of tiles because it needs to always be the first played, and the tiles list will be shuffled
start = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD'], image = 'img4.png') # x1

tiles = []

monastery_road = Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], building = Building['MONASTERY'], image = 'img1.png') # x2

tiles.append(monastery_road)
tiles.append(monastery_road)

monastery = Tile(top = Side['FIELD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], building = Building['MONASTERY'], image = 'img2.png') # x4

tiles.append(monastery)
tiles.append(monastery)
tiles.append(monastery)
tiles.append(monastery)

city_surrounded = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['CITY'], shield = True, image = 'img3.png') # one of these

tiles.append(city_surrounded)

top_city_w_road = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['FIELD'], image = 'img4.png') # x3

tiles.append(top_city_w_road)
tiles.append(top_city_w_road)
tiles.append(top_city_w_road)

top_city = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['FIELD'], image = 'img5.png') # x5

tiles.append(top_city)
tiles.append(top_city)
tiles.append(top_city)
tiles.append(top_city)
tiles.append(top_city)

left_right_city_shield = Tile(top = Side['FIELD'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'img6.png') # x2

tiles.append(left_right_city_shield)
tiles.append(left_right_city_shield)

left_right_city = Tile(top = Side['FIELD'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], image = 'img7.png') # x1

tiles.append(left_right_city)

top_bottom_city = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['CITY'], is_connected = False, image = 'img9.png') # x3

tiles.append(top_bottom_city)
tiles.append(top_bottom_city)
tiles.append(top_bottom_city)

top_left_city = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['FIELD'], bottom = Side['FIELD'], is_connected = False, image = 'img10.png') # x2

tiles.append(top_left_city)
tiles.append(top_left_city)

top_city_right_road = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'img11.png') # x3

tiles.append(top_city_right_road)
tiles.append(top_city_right_road)
tiles.append(top_city_right_road)

top_city_left_road = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'img12.png') # x3

tiles.append(top_city_left_road)
tiles.append(top_city_left_road)
tiles.append(top_city_left_road)

top_city_village = Tile(top = Side['CITY'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'img13.png') # x3

tiles.append(top_city_village)
tiles.append(top_city_village)
tiles.append(top_city_village)

top_right_city_shield = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'img14.png') # x2

tiles.append(top_right_city_shield)
tiles.append(top_right_city_shield)

top_right_city = Tile(top = Side['CITY'], left = Side['FIELD'], right = Side['CITY'], bottom = Side['FIELD'], image = 'img15.png') # x3

tiles.append(top_right_city)
tiles.append(top_right_city)
tiles.append(top_right_city)

top_left_city_shield_road = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], shield = True, image = 'img16.png') # x2

tiles.append(top_left_city_shield_road)
tiles.append(top_left_city_shield_road)

top_left_city_road =  Tile(top = Side['CITY'], left = Side['CITY'], right = Side['ROAD'], bottom = Side['ROAD'], image = 'img17.png') # x3

tiles.append(top_left_city_road)
tiles.append(top_left_city_road)
tiles.append(top_left_city_road)

top_left_right_city_shield = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], shield = True, image = 'img18.png') # x1

tiles.append(top_left_right_city_shield)

top_left_right_city = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['FIELD'], image = 'img19.png') # x3

tiles.append(top_left_right_city)
tiles.append(top_left_right_city)
tiles.append(top_left_right_city)

top_left_right_city_road_shield = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['ROAD'], shield = True, image = 'img20.png') # x2

tiles.append(top_left_right_city_road_shield)
tiles.append(top_left_right_city_road_shield)

top_left_right_city_road = Tile(top = Side['CITY'], left = Side['CITY'], right = Side['CITY'], bottom = Side['ROAD'], image = 'img21.png') # x1

tiles.append(top_left_right_city_road)

top_bottom_road = Tile(top = Side['ROAD'], left = Side['FIELD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'img22.png') # x8

tiles.append(top_bottom_road)
tiles.append(top_bottom_road)
tiles.append(top_bottom_road)
tiles.append(top_bottom_road)
tiles.append(top_bottom_road)
tiles.append(top_bottom_road)
tiles.append(top_bottom_road)
tiles.append(top_bottom_road)

left_bottom_road = Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['FIELD'], bottom = Side['ROAD'], image = 'img23.png') # x9

tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)
tiles.append(left_bottom_road)

left_right_bottom_village = Tile(top = Side['FIELD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'img24.png') # x4

tiles.append(left_right_bottom_village)
tiles.append(left_right_bottom_village)
tiles.append(left_right_bottom_village)
tiles.append(left_right_bottom_village)

village = Tile(top = Side['ROAD'], left = Side['ROAD'], right = Side['ROAD'], bottom = Side['ROAD'], building = Building['VILLAGE'], image = 'img25.png') # x1

tiles.append(village)

