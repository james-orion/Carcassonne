"""
This file updates the current meeple postion of the game

"""

class current_meeple:

    def __init__(self):
        self.meeple_x = 100
        self.meeple_y = 100
        self.moved = False

    def set_x(self, x):
        """ This sets the curent tile placement"""
        self.meeple_x = x

    def set_y(self, y):
        """ This sets the current tile placement"""
        self.meeple_y = y

    def set_moved(self, moved):
        """ This sets the moved boolean"""
        self.moved = moved

    def get_x(self):
        """"   This returns the current tile placement x"""
        return self.meeple_x

    def get_y(self):
        """ This returns the current tile placement y"""
        return self.meeple_y

    def get_moved(self):
        """"   This returns the moved boolean """
        return self.moved




