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
        #print("This is printing the feature_placementttt: " )
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
        #print(self.tiles_on_board)


    def add_location(self, x_old,y_old, x_new, y_new, old_side_connected, new_side_connected):
        """This adds a tile in the feature container
        and updates the sides, for tile on board """
        #print("this is the updated location!")
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
            #print(self.tiles_on_board[i])

    def add_tile(self, x_new, y_new, tile_new):
        """This adds a tile to tiles_on_board and sets values to default"""
        #print("added tile to feature placement!")
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

            #print(self.tiles_on_board[i])

    def get_board(self):
            return self.tiles_on_board
    
    def check_feature_completed(self, placed_tile):
        tile_coords = [0, 0]
        for row in self.tiles_on_board:
            for col in self.tiles_on_board[row]:
                if self.tiles_on_board[row][col] == placed_tile:
                    tile_coords[0] = row
                    tile_coords[1] = col

        if str(placed_tile.get_building()) == "Building.MONASTERY":
            feature_complete = True
            # check to see if there are 8 tiles surrounding the feature
            # monastery with road?
            if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['t_connected'] == False:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['b_connected'] == False:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['r_connected'] == False:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['l_connected'] == False:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1] + 1] == 0:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1] + 1] == 0:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1] - 1] == 0:
                feature_complete = False
            if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1] - 1] == 0:
                feature_complete = False
            
            if feature_complete:
                pass # score meeple
        # check if city is completed
        if str(placed_tile.get_top()) == "Side.CITY" or str(placed_tile.get_left()) == "Side.CITY" or str(placed_tile.get_right()) == "Side.CITY" or str(placed_tile.get_bottom()) == "Side.CITY":
            feature_complete = True
            found_connected = False
            num_connected = 0
            connected_cities = [placed_tile]
            while found_connected == False:
                num_connected = len(connected_cities)
                for city in connected_cities:
                    tile_coords = [0, 0]
                    for row in self.tiles_on_board:
                        for col in self.tiles_on_board[row]:
                            if self.tiles_on_board[row][col] == city:
                                tile_coords[0] = row
                                tile_coords[1] = col
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['t_connected'] == True: # or at top of board
                        if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] not in connected_cities: # update for tile above
                            connected_cities.append(self.tiles_on_board[tile_coords[0] + 1][[tile_coords[1]]]['tile']) # fix
                    else:
                        if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['top']) == "Side.CITY" and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] == 0: # update for tile above
                            feature_complete = False
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['r_connected'] == True: # or at right end of board
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] not in connected_cities:  # update for tile on right
                            connected_cities.append() # fix
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['l_connected'] == True: # or at left end of board
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1]] not in connected_cities:  # update for tile on left
                            connected_cities.append() # fix
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['b_connected'] == True: # or at bottom of board
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1]] not in connected_cities: # update for tile below
                            connected_cities.append() # fix
                if len(connected_cities) == num_connected:
                    found_connected = True