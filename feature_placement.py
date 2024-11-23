""" This file keeps track of features and tiles on the board"""
from copy import deepcopy

from tile import tiles
import copy
import game_settings

class feature_placements:

    def __init__(self):
        self.tiles_on_board = []

    def inital_location(self, l):
        """This is set for the intial placement of
        the start tile with its edges"""
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
                         'r_connected': False,
                         'x_coord': i,
                         'y_coord': j}
                    j_loc = j
                    i_loc = i
        self.tiles_on_board[i_loc][j_loc] = tile


    def add_location(self, x_old,y_old, x_new, y_new, old_side_connected, new_side_connected):
        """This adds a tile in the feature container
        and updates the sides, for tile on board """
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

    def add_tile(self, x_new, y_new, tile_new):
        """This adds a tile to tiles_on_board and sets values to default"""
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
                            'r_connected': False,
                            'x_coord': i,
                            'y_coord': j}

                    self.tiles_on_board[i][j] = tile

    def get_board(self):
            return self.tiles_on_board
    

    def check_feature_completed(self, settings):
        last_placed = settings.placed_tiles[-1][0][1]
        # check all monastery tiles to see if there are 8 surrounding tiles for any of them
        for row in range(len(self.tiles_on_board)):
            for col in range(len(self.tiles_on_board[row])):
                if self.tiles_on_board[row][col] != 0 and str(self.tiles_on_board[row][col]['tile'].get_building()) == "Building.MONASTERY":
                    tile_coords = [row, col]
                    feature_complete = self.check_monastery(tile_coords)
                    if feature_complete:
                        for meeple in settings.get_meeples():
                            if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'] == meeple.get_tile_placed_on():
                                meeple.get_player().get_meeple_score(meeple, self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'], settings, None, None)
                            
        # if placing a tile with a city as a side find all connected tiles and see if city is complete
        if last_placed.check_is_connected() == True and (str(last_placed.get_top()) == "Side.CITY" or str(last_placed.get_left()) == "Side.CITY" or str(last_placed.get_right()) == "Side.CITY" or str(last_placed.get_bottom()) == "Side.CITY"):
            city = [last_placed]
            self.check_city(city, settings)
        if last_placed.check_is_connected() == False and (str(last_placed.get_top()) == "Side.CITY" or str(last_placed.get_left()) == "Side.CITY" or str(last_placed.get_right()) == "Side.CITY" or str(last_placed.get_bottom()) == "Side.CITY"):
            tile_coords = self.get_coords(last_placed)
            cities = [[last_placed], [last_placed], [last_placed], [last_placed]]
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['top']) == "Side.CITY" and tile_coords[0] < len(self.tiles_on_board) - 1 and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] != 0:
                cities[0].append(self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'])
                self.check_city(cities[0], settings)
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['left']) == "Side.CITY" and tile_coords[1] > 0 and self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] != 0:
                cities[1].append(self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['tile'])
                self.check_city(cities[1], settings)
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['right']) == "Side.CITY" and tile_coords[1] < len(self.tiles_on_board[0]) - 1 and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] != 0:
                cities[2].append(self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'])
                self.check_city(cities[2], settings)
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['bottom']) == "Side.CITY" and tile_coords[0] > 0 and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0:
                cities[3].append(self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'])
                self.check_city(cities[3], settings)
        # if placing a tile with a road and without a village, check if that tile completes a feature
        if str(last_placed.get_building()) != "Building.VILLAGE" and (str(last_placed.get_top()) == "Side.ROAD" or str(last_placed.get_left()) == "Side.ROAD" or str(last_placed.get_right()) == "Side.ROAD" or str(last_placed.get_bottom()) == "Side.ROAD"):
            road = [last_placed]
            self.check_road(road, settings)
        # last placed tile has a village on it - check all roads starting at that village
        if str(last_placed.get_building()) == "Building.VILLAGE":
            tile_coords = self.get_coords(last_placed)
            roads = [[last_placed], [last_placed], [last_placed], [last_placed]]
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['top']) == "Side.ROAD" and tile_coords[0] < len(self.tiles_on_board) - 1 and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] != 0:
                roads[0].append(self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'])
                self.check_road(roads[0], settings)
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['left']) == "Side.ROAD" and tile_coords[1] > 0 and self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] != 0:
                roads[1].append(self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['tile'])
                self.check_road(roads[1], settings)
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['right']) == "Side.ROAD" and tile_coords[1] < len(self.tiles_on_board[0]) - 1 and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] != 0:
                roads[2].append(self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'])
                self.check_road(roads[2], settings)
            if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['bottom']) == "Side.ROAD" and tile_coords[0] > 0 and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0:
                roads[3].append(self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'])
                self.check_road(roads[3], settings)
            


    def check_monastery(self, tile_coords):
        # check if monestary is at the edges of the board
        if tile_coords[0] == 0:
            return False
        if tile_coords[0] == len(self.tiles_on_board) - 1:
            return False
        if tile_coords[1] == 0:
            return False
        if tile_coords[1] == len(self.tiles_on_board[0]) - 1:
            return False
        # check 8 surrounding tiles
        if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] == 0:
            return False
        if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] == 0:
            return False
        if self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] == 0:
            return False
        if self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] == 0:
            return False
        if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1] + 1] == 0:
            return False
        if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1] + 1] == 0:
            return False
        if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1] - 1] == 0:
            return False
        if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1] - 1] == 0:
            return False
        return True
    

    def get_coords(self, tile):
        tile_coords = [-1, -1]
        for row in range(len(self.tiles_on_board)):
            for col in range(len(self.tiles_on_board[row])):
                if self.tiles_on_board[row][col] != 0 and self.tiles_on_board[row][col]['tile'] == tile:
                    tile_coords[0] = row
                    tile_coords[1] = col
        return tile_coords
    

    def check_city(self, connected_tiles, settings):
        meeples_on_city = []
        feature_complete = True
        found_connected = False
        num_connected = 0
        while found_connected == False:
            num_connected = len(connected_tiles)
            for tile in connected_tiles:
                tile_coords = self.get_coords(tile)
                if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].check_is_connected() == True:
                    # if there's a connected tile above, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['t_connected'] == True and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] != 0:
                        if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['bottom']) == "Side.CITY":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'])
                    # if tile is not at top of board and there is no connected tile above don't add to list and mark that feature as incomplete
                    else:
                        if tile_coords[0] != len(self.tiles_on_board) - 1 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['top']) == "Side.CITY" and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] == 0:
                            feature_complete = False
                    # if there's a connected tile on right, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['r_connected'] == True and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] != 0:
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['left']) == "Side.CITY":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'])
                    # if tile is not on right side of board and there is no connected tile on right don't add to list and mark feature as incomplete
                    else:
                        if tile_coords[1] != len(self.tiles_on_board[0]) - 1 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['right']) == "Side.CITY" and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] == 0:
                            feature_complete = False
                    # if there's a connected tile on left, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['l_connected'] == True and self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] != 0:
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['right']) == "Side.CITY":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['tile'])
                    # if tile is not on left side of board and there is no connected tile on left don't add to list and mark feature as incomplete
                    else:
                        if tile_coords[1] != 0 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['left']) == "Side.CITY" and self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] == 0:
                            feature_complete = False
                    # if there's a connected tile below, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['b_connected'] == True and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0:
                        if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['top']) == "Side.CITY":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'])
                    # if tile is not at bottom of board and there is no connected tile below don't add to list and mark that feature as incomplete
                    else:
                        if tile_coords[0] != 0 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['bottom']) == "Side.CITY" and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] == 0:
                            feature_complete = False
            if len(connected_tiles) == num_connected:
                found_connected = True
        if feature_complete:
            print("CITY COMPLETE")
            for meeple in settings.get_meeples():
                if meeple.get_tile_placed_on() in connected_tiles and meeple.get_feature_type() == "CITY" and meeple.get_tile_placed_on().check_is_connected() == True:
                    meeples_on_city.append(meeple)
                elif meeple.get_tile_placed_on() in connected_tiles and meeple.get_feature_type() == "CITY" and meeple.get_tile_placed_on().check_is_connected() == False:
                    tile_coords = self.get_coords(meeple.get_tile_placed_on())
                    if meeple.get_tile_placed_on().get_meeple_placed_top() == True:
                        if tile_coords[0] == len(self.tiles_on_board) - 1 or (self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] != 0 and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'] in connected_tiles):
                            meeples_on_city.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_top(False)
                    if meeple.get_tile_placed_on().get_meeple_placed_left() == True:
                        if tile_coords[1] == 0 or (self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] != 0 and self.tiles_on_board[tile_coords[0]][tile_coords[1]  - 1]['tile'] in connected_tiles):
                            meeples_on_city.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_left(False)
                    if meeple.get_tile_placed_on().get_meeple_placed_right() == True:
                        if tile_coords[1] == len(self.tiles_on_board[0]) - 1 or (self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] != 0 and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'] in connected_tiles):
                            meeples_on_city.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_right(False)
                    if meeple.get_tile_placed_on().get_meeple_placed_bottom() == True:
                        if tile_coords[0] == 0 or (self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0 and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'] in connected_tiles):
                            meeples_on_city.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_bottom(False)
            for meeple in meeples_on_city:
                meeple.get_player().get_meeple_score(meeple, None, settings, connected_tiles, meeples_on_city)
        else:
            print("CITY INCOMPLETE")


    def check_road(self, connected_tiles, settings):
        meeples_on_road = []
        feature_complete = True
        found_connected = False
        num_connected = 0
        while found_connected == False:
            num_connected = len(connected_tiles)
            for tile in connected_tiles:
                tile_coords = self.get_coords(tile)
                # if current tile being checked doesn't have a village on it, check all surrounding tiles
                # if it does have a village don't check tiles beyond it
                if str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].get_building()) != "Building.VILLAGE":
                    # if there's a connected tile above, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['t_connected'] == True and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] != 0:
                        if self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['bottom']) == "Side.ROAD":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'])
                    #  if tile is not at top of board and there is no connected tile above don't add to list and mark that feature as incomplete
                    else:
                        if tile_coords[0] != len(self.tiles_on_board) - 1 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['top']) == "Side.ROAD" and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] == 0:
                            feature_complete = False
                    # if there's a connected tile to right, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['r_connected'] == True and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] != 0:
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['left']) == 'Side.ROAD':
                            connected_tiles.append(self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'])
                    #  if tile is not on right side of board and there is no connected tile on right don't add to list and mark feature as incomplete
                    else:
                        if tile_coords[1] != len(self.tiles_on_board[0]) - 1 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['right']) == "Side.ROAD" and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] == 0:
                            feature_complete = False
                    #  if there's a connected tile on left, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['l_connected'] == True and self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] != 0:
                        if self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['right']) == "Side.ROAD":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1]['tile'])
                    # if tile is not on left side of board and there is no connected tile on left don't add to list and mark feature as incomplete
                    else:
                        if tile_coords[1] != 0 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['left']) == "Side.ROAD" and self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] == 0:
                            feature_complete = False
                    #  if there's a connected tile below, add to list of connected tiles
                    if self.tiles_on_board[tile_coords[0]][tile_coords[1]]['b_connected'] == True and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0:
                        if self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0 and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'] not in connected_tiles and str(self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['top']) == "Side.ROAD":
                            connected_tiles.append(self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'])
                    # if tile is not at bottom of board and there is no connected tile below don't add to list and mark that feature as incomplete
                    else:
                        if tile_coords[0] != 0 and str(self.tiles_on_board[tile_coords[0]][tile_coords[1]]['bottom']) == "Side.ROAD" and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] == 0:
                            feature_complete = False
            if len(connected_tiles) == num_connected:
                found_connected = True
        if feature_complete:
            print("ROAD COMPLETE")
            for meeple in settings.get_meeples():
                if meeple.get_tile_placed_on() in connected_tiles and meeple.get_feature_type() == "ROAD" and str(meeple.get_tile_placed_on().get_building()) != "Building.VILLAGE":
                    meeples_on_road.append(meeple)
                elif meeple.get_tile_placed_on() in connected_tiles and meeple.get_feature_type() == "ROAD" and str(meeple.get_tile_placed_on().get_building()) == "Building.VILLAGE":
                    # check where meeple is placed on tile, then check if roads with meeple are placed are in
                    tile_coords = self.get_coords(meeple.get_tile_placed_on())
                    if meeple.get_tile_placed_on().get_meeple_placed_top() == True:
                        if tile_coords[0] == len(self.tiles_on_board) - 1 or (self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]] != 0 and self.tiles_on_board[tile_coords[0] + 1][tile_coords[1]]['tile'] in connected_tiles):
                            meeples_on_road.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_top(False)
                    if meeple.get_tile_placed_on().get_meeple_placed_left() == True:
                        if tile_coords[1] == 0 or (self.tiles_on_board[tile_coords[0]][tile_coords[1] - 1] != 0 and self.tiles_on_board[tile_coords[0]][tile_coords[1]  - 1]['tile'] in connected_tiles):
                            meeples_on_road.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_left(False)
                    if meeple.get_tile_placed_on().get_meeple_placed_right() == True:
                        if tile_coords[1] == len(self.tiles_on_board[0]) - 1 or (self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1] != 0 and self.tiles_on_board[tile_coords[0]][tile_coords[1] + 1]['tile'] in connected_tiles):
                            meeples_on_road.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_right(False)
                    if meeple.get_tile_placed_on().get_meeple_placed_bottom() == True:
                        if tile_coords[0] == 0 or (self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]] != 0 and self.tiles_on_board[tile_coords[0] - 1][tile_coords[1]]['tile'] in connected_tiles):
                            meeples_on_road.append(meeple)
                            self.tiles_on_board[tile_coords[0]][tile_coords[1]]['tile'].set_meeple_placed_bottom(False)
            for meeple in meeples_on_road:
                meeple.get_player().get_meeple_score(meeple, None, settings, connected_tiles, meeples_on_road)
        else:
            print("ROAD INCOMPLETE")