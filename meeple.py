# Meeple Class
# Stores information about meeples, such as what player
# they belong to, what color they are, whether or not they
# have been placed, etc. It will also count the points a
# meeple earns once a feature is completed, and how many
# points are won at the end of the game.

# TODO validate placement for roads and citites
# TODO implement in game scoring for roads and cities
# TODO implement end of game scoring for all features

class Meeple:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_placed = False
        self.feature_type = None
        self.meeple_sprite = None
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
            
        if self.validate_placement(tile, settings):
            # update Meeple's sprite and placement boolean
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
            return True
        else:
            self.feature_type = None
            return False

    
    # validates that user's placement of Meeple is allowed
    # if returns True, store placement of Meeple on tile
    # if return False, prompt user to choose again
    def validate_placement(self, tile, settings):
        # TODO finish implementing - iterate through list of tiles in feature,
        # if there is a Meeple alreay placed, don't allow user to place another;
        # if there isn't a Meeple placed anywhere on the feature, allow user to
        # place one

        # if placing as highwayman, make sure only meeple on stretch of road
        if self.feature_type == "ROAD":
            # TODO handle tiles with villages in center (img 12, 23, 24)
            connected_tiles = self.find_connected_tiles(tile, settings)
            roads_on_tile = 0
            for tile in connected_tiles:
                if str(tile.get_top()) == "Side.ROAD" and tile.get_meeple_placed_top() == True:
                    return False
                elif str(tile.get_left()) == "Side.ROAD" and tile.get_meeple_placed_left() == True:
                    return False
                if str(tile.get_right()) == "Side.ROAD" and tile.get_meeple_placed_right() == True:
                    return False
                if str(tile.get_bottom()) == "Side.ROAD" and tile.get_meeple_placed_bottom() == True:
                    return False
        # if placing as knight, make sure only meeple in city
        elif self.feature_type == "CITY":
            connected_tiles = self.find_connected_tiles(tile, settings)
            for tile in connected_tiles:
                if str(tile.get_top()) == "Side.CITY" and tile.get_meeple_placed_top() == True:
                    return False
                elif str(tile.get_left()) == "Side.CITY" and tile.get_meeple_placed_left() == True:
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


    def find_connected_tiles(self, tile, settings):
        # TODO fix bug with tiles placed on edges
        game_tiles = settings.feature_container
        game_board_height = len(game_tiles) - 1
        game_board_width = len(game_tiles[0]) - 1
        tile_coords = []
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


    # determines how many points a Meeple scores once a feature is completed
    def meeple_score(self, settings):
        """meeples = settings.get_meeples()
        for meeple in meeples:
            if self == meeple:
                print("THIS WORKS")
            else:
                print("Nope")"""
        points = 0
        # TODO find some way to check if feature is completed, then iterate
        # through list of tiles to determine total number of points
        # NEED TO SET FALSE FOR MEEPLE_PLACED_X IN TILE CLASS

        # calculate points won by meeple in feature
        if self.feature_type == "ROAD":
            # points = number of tiles in the complete road
            pass
        elif self.feature_type == "CITY":
            # points = 2 per each tile in city, extra 2 if tile with coat of arms
            pass
        else:
            # 9 points for a monastery
            points = 9

        # unplace and reset meeple
        self.is_placed = False
        self.feature_type = None
        self.meeple_sprite = None
        self.x_coord = None
        self.y_coord = None
        return points
    

    # determines how many points a Meeple scores for an incomplete feature 
    # at the end of the game
    def end_of_game_scoring(self):
        # NEED TO SET FALSE FOR MEEPLE_PLACED_X IN TILE CLASS
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
        return points
    

    # getter methods

    # returns Meeple's name
    def get_name(self):
        return self.name
    

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
    

    # setter methods

    # sets Meeple's name
    def set_name(self, name):
        self.name = name
    

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