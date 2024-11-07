"""
This file updates the current meeple postion of the game

"""

class current_meeple:

    def __init__(self):
        self.meeple_x = 100
        self.meeple_y = 100
        self.moved = False
        self.image = None

    def set_x(self, x):
        """ This sets the curent meeple placement"""
        self.meeple_x = x

    def set_y(self, y):
        """ This sets the current meeple placement"""
        self.meeple_y = y

    def set_moved(self, moved):
        """ This sets the moved boolean"""
        self.moved = moved

    def set_meeple_image(self, meeple_image):
        """This sets the current meeple image"""
        self.meeple_image = meeple_image

    def get_x(self):
        """"   This returns the current meeple placement x"""
        return self.meeple_x

    def get_y(self):
        """ This returns the current meeple placement y"""
        return self.meeple_y

    def get_moved(self):
        """"   This returns the meeple boolean """
        return self.moved

    def get_meeple_image(self):
        """This returns the current meeple image"""
        return self.meeple_image


