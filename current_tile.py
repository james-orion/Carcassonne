"""
This file, updates the current tile placement of the game

"""

class current_tile:

    def __init__(self):
        self.tile_x = 200
        self.tile_y = 100
        self.moved = False

    def set_x(self, x):
        """ This sets the curent tile placement"""
        self.tile_x = x


    def set_y(self, y):
        """ This sets the current tile placement"""
        self.tile_y = y

    def set_moved(self, moved):
        """ This sets the moved boolean"""
        self.moved = moved

    def get_x(self):
        """"   This returns the current tile placement x"""
        return self.tile_x

    def get_y(self):
        """ This returns the current tile placement y"""
        return self.tile_y

    def get_moved(self):
        """"   This returns the moved boolean """
        return self.moved




