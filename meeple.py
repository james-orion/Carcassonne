# Meeple Class
# Stores information about meeples, such as what player
# they belong to, what color they are, whether or not they
# have been placed, etc. It will also count the points a
# meeple earns once a feature is completed, and how many
# points are won at the end of the game.

# TODO validate placement for roads
# TODO implement in game scoring for roads and cities
# TODO implement end of game scoring for all features

import feature_placement

class Meeple:
    def __init__(self, player, color):
        self.player = player
        self.color = color
        self.is_placed = False
        self.feature_type = None
        self.meeple_sprite = None
        self.tile_placed_on = None
        self.x_coord = None
        self.y_coord = None

    
    # place Meeple on game board and store information about where it was placed
    def place_meeple(self, tile, user_choice, settings):
        # record feature type Meeple was placed on
        temp_feature_type = ""
        if user_choice == "TOP":
            if str(tile.get_top()) == "Side.FIELD":
                return False
            else:
                temp_feature_type = str(tile.get_top())
        elif user_choice == "LEFT":
            if str(tile.get_left()) == "Side.FIELD":
                return False
            else:
                temp_feature_type = str(tile.get_left())
        elif user_choice == "RIGHT":
            if str(tile.get_right()) == "Side.FIELD":
                return False
            else:
                temp_feature_type = str(tile.get_right())
        elif user_choice == "BOTTOM":
            if str(tile.get_bottom()) == "Side.FIELD":
                return False
            else:
                temp_feature_type = str(tile.get_bottom())
        else:
            if str(tile.get_building()) == "Building.NONE":
                return False
            else:
                temp_feature_type = str(tile.get_building())
        self.feature_type = temp_feature_type.split(".")[1]
        if self.validate_placement(tile, settings, user_choice):
            # update Meeple's sprite and placement booleans for tile and meeple
            if user_choice == "TOP":
                tile.set_meeple_placed_top(True)
            elif user_choice == "LEFT":
                tile.set_meeple_placed_left(True)
            elif user_choice == "RIGHT":
                tile.set_meeple_placed_right(True)
            elif user_choice == "BOTTOM":
                tile.set_meeple_placed_bottom(True)
            else:
                tile.set_meeple_placed_center(True)
            self.is_placed = True
            self.meeple_sprite = "meeple_sprites/" + self.color + "_meeple.png"
            self.tile_placed_on = tile
            return True
        else:
            self.feature_type = None
            return False

    
    # validates that user's placement of Meeple is allowed
    # if returns True, store placement of Meeple on tile
    # if return False, prompt user to choose again
    def validate_placement(self, tile, settings, user_choice):
        # if placing as highwayman, make sure only meeple on stretch of road
        # TODO fix isssue with meepls on tiles with villages
        if self.feature_type == "ROAD":
            road = [tile]
            if self.find_connected_road_tiles(road, settings, user_choice) == False:
                return False
        # if placing as knight, make sure only meeple in city
        # TODO fix issues with unconnected city tiles
        elif self.feature_type == "CITY":
            connected_tiles = self.find_connected_city_tiles(tile, settings)
            for tile in connected_tiles:
                if str(tile.get_top()) == "Side.CITY" and tile.get_meeple_placed_top() == True:
                    return False
                if str(tile.get_left()) == "Side.CITY" and tile.get_meeple_placed_left() == True:
                    return False
                if str(tile.get_right()) == "Side.CITY" and tile.get_meeple_placed_right() == True:
                    return False
                if str(tile.get_bottom()) == "Side.CITY" and tile.get_meeple_placed_bottom() == True:
                    return False     
        # if placing as monk/nun, make sure only meeple in monestary
        elif self.feature_type == "MONASTERY":
            if tile.get_meeple_placed_center() == True:
                return False
        return True


    def find_connected_road_tiles(self, connected_tiles, settings, user_choice):
        game_tiles = settings.feature_container
        game_board_height = len(game_tiles) - 1
        game_board_width = len(game_tiles[0]) - 1
        found_connected = False
        num_connected = 0
        if str(connected_tiles[0].get_building()) == "Building.VILLAGE":
            tile_coords = self.get_coords(connected_tiles[0], game_tiles)
            if user_choice == "TOP":
                print(game_tiles[tile_coords[0] + 1][tile_coords[1]])
                if tile_coords[0] + 1 < game_board_height and game_tiles[tile_coords[0] + 1][tile_coords[1]] != 0:
                    connected_tiles.append(game_tiles[tile_coords[0] + 1][tile_coords[1]])
            elif user_choice == "LEFT":
                print(game_tiles[tile_coords[0]][tile_coords[1] - 1])
                if tile_coords[1] - 1 > 0 and game_tiles[tile_coords[0]][tile_coords[1] - 1] != 0:
                    connected_tiles.append(game_tiles[tile_coords[0]][tile_coords[1] - 1])
            elif user_choice == "RIGHT":
                print(game_tiles[tile_coords[0]][tile_coords[1] + 1])
                if tile_coords[1] + 1 < game_board_width and game_tiles[tile_coords[0]][tile_coords[1] + 1] != 0:
                    connected_tiles.append(game_tiles[tile_coords[0]][tile_coords[1] + 1])
            else :
                print(game_tiles[tile_coords[0] - 1][tile_coords[1]])
                if tile_coords[0] - 1 > 0 and game_tiles[tile_coords[0] - 1][tile_coords[1]] != 0:
                    connected_tiles.append(game_tiles[tile_coords[0] - 1][tile_coords[1]])
        while found_connected == False:
            num_connected = len(connected_tiles)
            for tile in connected_tiles:
                tile_coords = self.get_coords(tile, game_tiles)
                if str(tile.get_building()) != "Building.VILLAGE":
                    if tile_coords[0] - 1 >= 0 and game_tiles[tile_coords[0] - 1][tile_coords[1]] != 0:
                        if (str(tile.get_bottom()) == "Side.ROAD") and (str(game_tiles[tile_coords[0] - 1][tile_coords[1]].get_top()) == "Side.ROAD") and game_tiles[tile_coords[0] - 1][tile_coords[1]] not in connected_tiles:
                            connected_tiles.append(game_tiles[tile_coords[0] - 1][tile_coords[1]])
                            print("ADDED TILE BELOW")
                        if game_tiles[tile_coords[0] - 1][tile_coords[1]].get_meeple_placed_top() == True:
                            return False
                    if tile_coords[1] + 1 <= game_board_width and game_tiles[tile_coords[0]][tile_coords[1] + 1] != 0:
                        if (str(tile.get_right()) == "Side.ROAD") and (str(game_tiles[tile_coords[0]][tile_coords[1] + 1].get_left()) == "Side.ROAD") and game_tiles[tile_coords[0]][tile_coords[1] + 1] not in connected_tiles:
                            connected_tiles.append(game_tiles[tile_coords[0]][tile_coords[1] + 1])
                            print("ADDED TILE RIGHT")
                        if game_tiles[tile_coords[0]][tile_coords[1] + 1].get_meeple_placed_left() == True:
                            return False
                    if tile_coords[1] - 1 >= 0 and game_tiles[tile_coords[0]][tile_coords[1] - 1] != 0:
                        if (str(tile.get_left()) == "Side.ROAD") and (str(game_tiles[tile_coords[0]][tile_coords[1] - 1].get_right()) == "Side.ROAD") and game_tiles[tile_coords[0]][tile_coords[1] - 1] not in connected_tiles:
                            connected_tiles.append(game_tiles[tile_coords[0]][tile_coords[1] - 1])
                            print("ADDED TILE LEFT")
                        if game_tiles[tile_coords[0]][tile_coords[1] - 1].get_meeple_placed_right() == True:
                            return False
                    if tile_coords[0] + 1 <= game_board_height and game_tiles[tile_coords[0] + 1][tile_coords[1]] != 0:
                        if (str(tile.get_top()) == "Side.ROAD") and (str(game_tiles[tile_coords[0] + 1][tile_coords[1]].get_bottom()) == "Side.ROAD") and game_tiles[tile_coords[0] + 1][tile_coords[1]] not in connected_tiles:
                            connected_tiles.append(game_tiles[tile_coords[0] + 1][tile_coords[1]])
                            print("ADDED TILE ABOVE")
                            print(game_tiles[tile_coords[0] + 1][tile_coords[1]].get_meeple_placed_bottom())
                        if game_tiles[tile_coords[0] + 1][tile_coords[1]].get_meeple_placed_bottom() == True:
                            return False
            if num_connected == len(connected_tiles):
                found_connected = True
        for tile in connected_tiles:
                if str(tile.get_building) != "Building.VILLAGE":
                    if str(tile.get_top()) == "Side.ROAD" and tile.get_meeple_placed_top() == True:
                        return False
                    if str(tile.get_left()) == "Side.ROAD" and tile.get_meeple_placed_left() == True:
                        return False
                    if str(tile.get_right()) == "Side.ROAD" and tile.get_meeple_placed_right() == True:
                        return False
                    if str(tile.get_bottom()) == "Side.ROAD" and tile.get_meeple_placed_bottom() == True:
                        return False   
        return True


    def find_connected_city_tiles(self, tile, settings):
        game_tiles = settings.feature_container
        game_board_height = len(game_tiles) - 1
        game_board_width = len(game_tiles[0]) - 1
        connected_tiles = []
        found_connected = False
        num_connected = 0
        tile_coords = [0, 0]
        connected_tiles.append(tile)
        while found_connected == False:
            num_connected = len(connected_tiles)
            for tile in connected_tiles:
                for i in range(len(game_tiles)):
                    for j in range(len(game_tiles[i])):
                        if tile == game_tiles[i][j]:
                            tile_coords[0] = i
                            tile_coords[1] = j
                if (tile_coords[0] - 1 >= 0):
                    if (game_tiles[tile_coords[0] - 1][tile_coords[1]] != 0) and (str(tile.get_bottom()) == "Side." + self.feature_type) and (str(game_tiles[tile_coords[0] - 1][tile_coords[1]].get_top()) == "Side." + self.feature_type) and game_tiles[tile_coords[0] - 1][tile_coords[1]] not in connected_tiles:
                        connected_tiles.append(game_tiles[tile_coords[0] - 1][tile_coords[1]])
                if (tile_coords[1] + 1 <= game_board_width):
                    if (game_tiles[tile_coords[0]][tile_coords[1] + 1] != 0) and (str(tile.get_right()) == "Side." + self.feature_type) and (str(game_tiles[tile_coords[0]][tile_coords[1] + 1].get_left()) == "Side." + self.feature_type) and game_tiles[tile_coords[0]][tile_coords[1] + 1] not in connected_tiles:
                        connected_tiles.append(game_tiles[tile_coords[0]][tile_coords[1] + 1])
                if (tile_coords[1] - 1 >= 0):
                    if (game_tiles[tile_coords[0]][tile_coords[1] - 1] != 0) and (str(tile.get_left()) == "Side." + self.feature_type) and (str(game_tiles[tile_coords[0]][tile_coords[1] - 1].get_right()) == "Side." + self.feature_type) and game_tiles[tile_coords[0]][tile_coords[1] - 1] not in connected_tiles:
                        connected_tiles.append(game_tiles[tile_coords[0]][tile_coords[1] - 1])
                if (tile_coords[0] + 1 <= game_board_height):
                    if (game_tiles[tile_coords[0] + 1][tile_coords[1]] != 0) and (str(tile.get_top()) == "Side." + self.feature_type) and (str(game_tiles[tile_coords[0] + 1][tile_coords[1]].get_bottom()) == "Side." + self.feature_type) and game_tiles[tile_coords[0] + 1][tile_coords[1]] not in connected_tiles:
                        connected_tiles.append(game_tiles[tile_coords[0] + 1][tile_coords[1]])
            if num_connected == len(connected_tiles):
                found_connected = True
        return connected_tiles
    

    def get_coords(self, tile, game_tiles):
        tile_coords = [-1, -1]
        for i in range(len(game_tiles)):
                    for j in range(len(game_tiles[i])):
                        if tile == game_tiles[i][j]:
                            tile_coords[0] = i
                            tile_coords[1] = j
        return tile_coords


    # determines how many points a Meeple scores once a feature is completed
    def meeple_score(self, tile, settings, connected_tiles):
        points = 0
        num_meeples = 0

        # calculate points won by meeple in feature
        if self.feature_type == "ROAD":
            # points = number of tiles in the complete road
            # TODO also check whether a meeple of the same color is placed on any of these road tiles so their points don't get counted twice
            # TODO don't unplace meeples that are on village tiles but on different roads
            for tile in connected_tiles:
                points += 1
                if tile.get_meeple_placed_top() == True and str(tile.get_top()) == "Side.ROAD":
                    tile.set_meeple_placed_top(False)
                if tile.get_meeple_placed_left() == True and str(tile.get_left()) == "Side.ROAD":
                    tile.set_meeple_placed_left(False)
                if tile.get_meeple_placed_right() == True and str(tile.get_right()) == "Side.ROAD":
                    tile.set_meeple_placed_right(False)
                if tile.get_meeple_placed_bottom() == True and str(tile.get_bottom()) == "Side.ROAD":
                    tile.set_meeple_placed_bottom(False)
        elif self.feature_type == "CITY":
            # points = 2 per each tile in city, extra 2 if tile with coat of arms
            # TODO also check whether a meeple of the same color is placed on any of these city tiles so their points don't get counted twice
            for tile in connected_tiles:
                if tile.has_shield():
                    points += 4
                else:
                    points += 2
                if tile.get_meeple_placed_top() == True and str(tile.get_top()) == "Side.CITY":
                    tile.set_meeple_placed_top(False)
                if tile.get_meeple_placed_left() == True and str(tile.get_left()) == "Side.CITY":
                    tile.set_meeple_placed_left(False)
                if tile.get_meeple_placed_right() == True and str(tile.get_right()) == "Side.CITY":
                    tile.set_meeple_placed_right(False)
                if tile.get_meeple_placed_bottom() == True and str(tile.get_bottom()) == "Side.CITY":
                    tile.set_meeple_placed_bottom(False)
        else:
            # 9 points for a monastery
            tile.set_meeple_placed_center(False)
            points = 9

        # TODO fix issue where the wrong meeple is taken off of the board
        # unplace and reset meeple
        settings.get_meeples().remove(self)
        self.is_placed = False
        self.feature_type = None
        self.meeple_sprite = None
        self.x_coord = None
        self.y_coord = None
        self.tile_placed_on = None
        return points
    

    # determines how many points a Meeple scores for an incomplete feature 
    # at the end of the game
    def end_of_game_scoring(self):
        # TODO NEED TO SET FALSE FOR MEEPLE_PLACED_X IN TILE CLASS
        points = 0
        # determine of feature is partially complete
        if self.feature_type == "ROAD":
            # points = number of tiles in the partial road
            pass
        elif self.feature_type == "CITY":
            # points = 1 per each tile in partial city, extra 1 if tile with coat of arms
            pass
        else:
            # points = number of tiles surrounding monestary + 1 for monestary itself
            pass

        # unplace and reset meeple
        self.is_placed = False
        self.feature_type = None
        self.meeple_sprite = None
        self.x_coord = None
        self.y_coord = None
        self.tile_placed_on = None
        return points
    

    # getter methods

    # returns Meeple's player
    def get_player(self):
        return self.player
    

    # returns color of Meeple
    def get_color(self):
        return self.color
    

    # returns whether or not Meeple is placed
    def get_is_placed(self):
        return self.is_placed
    

    # returns feature Meeple is placed on
    def get_feature_type(self):
        return self.feature_type
    

    # returns Meeple's sprite
    def get_meeple_sprite(self):
        return self.meeple_sprite
    

    def get_x_coord(self):
        return self.x_coord
    

    def get_y_coord(self):
        return self.y_coord
    

    def get_tile_placed_on(self):
        return self.tile_placed_on
    

    # setter methods

    # sets Meeple's player
    def set_player(self, player):
        self.player = player
    

    # sets color of Meeple
    def set_color(self, color):
        self.color = color
    

    # sets whether or not Meeple is placed
    def set_is_placed(self, is_placed):
        self.is_placed = is_placed
    

    # sets feature Meeple is placed on
    def set_feature_type(self, feature_type):
        self.feature_type = feature_type
    

    # set Meeple's sprite
    def set_meeple_sprite(self, meeple_sprite):
        self.meeple_sprite = meeple_sprite
    

    def set_x_coord(self, x_coord):
        self.x_coord = x_coord


    def set_y_coord(self, y_coord):
        self.y_coord = y_coord


    def set_tile_placed_on(self, tile):
        self.tile_placed_on = tile


# test cases
# test constructor and getter methods
def test_one():
    test_meeple = Meeple("Jack", "m1", "red")
    if test_meeple.get_player() != "Jack":
        return "FAILED get_player"
    if test_meeple.get_name() != "m1":
        return "FAILED get_name"
    if test_meeple.get_color() != "red":
        return "FAILED get_color"
    if test_meeple.get_is_placed() != False:
        return "FAILED get_is_placed"
    if test_meeple.get_feature_type() != None:
        return "FAILED get_feature_type"
    if test_meeple.get_orientation() != None:
        return "FAILED get_orientation"
    return "PASSED"


# test place_meeple function
def test_two():
    test_meeple_1 = Meeple("Jack", "m1", "red")
    # manually sets feautre type until implemented
    test_meeple_1.set_feature_type("field")
    test_tile = None
    user_selection = None
    test_meeple_1.place_meeple(test_tile, user_selection)
    if test_meeple_1.get_is_placed() != True:
        return "FAILED doesn't update placement boolean"
    if test_meeple_1.get_orientation() != "horizontal":
        return "FAILED doesn't update horizontal orientation"
    
    test_meeple_2 = Meeple("Jack", "m2", "red")
    test_meeple_2.set_feature_type("road")
    test_meeple_2.place_meeple(test_tile, user_selection)
    if test_meeple_2.get_is_placed() != True:
        return "FAILED doesn't update placement boolean"
    if test_meeple_2.get_orientation() != "vertical":
        return "FAILED doesn't update vertical orientation"
    return "PASSED"


# test current Meeple scoring
def test_three():
    test_meeple = Meeple("Jack", "m1", "red")
    # manually set feature again
    test_meeple.set_feature_type("monestary")
    test_tile = None
    user_selection = None
    test_meeple.place_meeple(test_tile, user_selection)
    if test_meeple.meeple_score() != 9:
        return "FAILED scoring failed"
    if test_meeple.get_is_placed() != False:
        return "FAILED is_placed boolean not updated"
    if test_meeple.get_feature_type() != None:
        return "FAILED feature_type not updated"
    if test_meeple.get_orientation() != None:
        return "FAILED orientation not updated"
    return "PASSED"


# tests Meeple sprites
def test_four():
    test_meeple_1 = Meeple("Jack", "m1", "red")
    # manually set feature type
    test_meeple_1.set_feature_type("city")
    test_tile = None
    user_selection = None
    test_meeple_1.place_meeple(test_tile, user_selection)
    if test_meeple_1.get_meeple_sprite() != "\"/meeple_sprites/red_sprite.png\"":
        return "FAILED incorrect file path for vertical sprite"
    
    test_meeple_2 = Meeple("Jack", "m2", "red")
    test_meeple_2.set_feature_type("field")
    test_meeple_2.place_meeple(test_tile, user_selection)
    if test_meeple_2.get_meeple_sprite() != "\"/meeple_sprites/red_horizontal_sprite.png\"":
        return "FAILED incorrect file path for horizontal sprite"
    return "PASSED"


if __name__ == "__main__":
    print("test one: ", test_one())
    print("test two: ", test_two())
    print("test three: ", test_three())
    print("test four: ", test_four())