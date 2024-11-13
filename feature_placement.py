""" This file keeps track of features and tiles on the board"""
from copy import deepcopy

from tile import tiles
import copy

class feature_placements:

    def __init__(self):
        self.tiles_on_board = []

    def inital_location(self, l):
        """This is set for the intial placement of
        the start tile with its edges"""
        print("This is printing the feature_placementttt: " )
        tile = {}
        j_loc = -1
        i_loc = -1
        # making a deep copy of original matrix so the dict doesn't mess up the origional
        self.tiles_on_board = copy.deepcopy(l)
        for i in range(len(l)):
            for j in range(len(l[i])):
                # find the location of the start tile and update with dict
                if l[i][j] != 0:
                    tile = {'tile': l[i][j],
                         'top': l[i][j].get_top(),
                         'bottom': l[i][j].get_bottom(),
                         'left': l[i][j].get_left(),
                         'right': l[i][j].get_right(),
                         't_connected': False,
                         'b_connected': False,
                         'l_connected': False,
                         'r_connected': False}
                    j_loc = j
                    i_loc = i
        self.tiles_on_board[i_loc][j_loc] = tile
        print(self.tiles_on_board)


    def add_location(self, x_old,y_old, x_new, y_new, old_side_connected, new_side_connected):
        """This adds a tile in the feature container
        and updates the sides, for tile on board """
        print("this is the updated location!")
        # place new tile on the board
        for i in range(len(self.tiles_on_board)):
            for j in range(len(self.tiles_on_board[i])):
                if i == x_old and j == y_old:
                    if old_side_connected in self.tiles_on_board[i][j]:
                        if old_side_connected == "top":
                            self.tiles_on_board[i][j]['t_connected'] = True
                        elif old_side_connected == "bottom":
                            self.tiles_on_board[i][j]['b_connected'] = True
                        elif old_side_connected == "right":
                            self.tiles_on_board[i][j]['r_connected'] = True
                        else:
                            self.tiles_on_board[i][j]['l_connected'] = True
                if i == x_new and j == y_new:
                    if new_side_connected in self.tiles_on_board[i][j]:
                        if new_side_connected == "top":
                            self.tiles_on_board[i][j]['t_connected'] = True
                        elif new_side_connected == "bottom":
                            self.tiles_on_board[i][j]['b_connected'] = True
                        elif new_side_connected == "right":
                            self.tiles_on_board[i][j]['r_connected']= True
                        else:
                            self.tiles_on_board[i][j]['l_connected'] = True
            print(self.tiles_on_board[i])

    def add_tile(self, x_new, y_new, tile_new):
        """This adds a tile to tiles_on_board and sets values to default"""
        print("added tile to feature placement!")
        for i in range(len(self.tiles_on_board)):
            for j in range(len(self.tiles_on_board[i])):
                if i == x_new and j == y_new:
                    tile = {'tile': tile_new,
                            'top': tile_new.get_top(),
                            'bottom': tile_new.get_bottom(),
                            'left': tile_new.get_left(),
                            'right': tile_new.get_right(),
                            't_connected': False,
                            'b_connected': False,
                            'l_connected': False,
                            'r_connected': False}

                    self.tiles_on_board[i][j] = tile

            print(self.tiles_on_board[i])

