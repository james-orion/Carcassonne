# Meeple Class
# Stores information about meeples, such as what player
# they belong to, what color they are, whether or not they
# have been placed, etc. It will also count the points a
# meeple earns once a feature is completed, and how many
# points are won at the end of the game.

import arcade, player

class Meeple:
    def __init__(self, player, name, color):
        self.player = player
        self.name = name
        self.color = color
        self.is_placed = False
        self.feature_type = None
        self.orientation = None
        self.meeple_sprite = None

    
    # place Meeple on game board and store information about where it was placed
    def place_meeple(self, tile):
        # TODO validate location of meeple on tile - placed in center or one of the edges?
        #self.feature_type = None TODO feature type is same as location of Meeple on tile
        if self.validate_placement(tile):
            self.is_placed = True
            # TODO determine what feature on tile Meeple is placed on
            # self.feature_type = 
            if self.feature_type == "field":
                self.orientation = "horizontal"
                self.meeple_sprite = "\"/meeple_sprites/" + self.color + "_horizontal_sprite.png\""
            else:
                self.orientation = "vertical"
                self.meeple_sprite = "\"/meeple_sprites/" + self.color + "_sprite.png\""
            # TODO store location on game board and update tile it's placed on
            return True

    
    # validates that user's placement of Meeple is allowed
    def validate_placement(self, tile):
        # TODO finish implementing - iterate through list of tiles in feature,
        # if there is a Meeple alreay placed, don't allow user to place another;
        # if there isn't a Meeple placed anywhere on the feature, allow user to
        # place one

        # if placing as highwayman, make sure only meeple on stretch of road
        if self.feature_type == "road":
            pass
        # if placing as knight, make sure only meeple in city
        if self.feature_type == "city":
            pass
        # if placing as monk/nun, make sure only meeple in monestary
        if self.feature_type == "monestary":
            pass
        # if placing farmer, make sure only Meeple on field
        else:
            pass
        return True


    # determines how many points a Meeple scores once a feature is completed
    def meeple_score(self):
        points = 0
        # TODO find some way to check if feature is completed, then iterate
        # through list of tiles to determine total number of points

        # calculate points won by meeple in feature
        if self.feature_type == "road":
            # points = number of tiles in the complete road
            pass
        elif self.feature_type == "city":
            # points = 2 per each tile in city, extra 2 if tile with coat of arms
            pass
        elif self.feature_type == "monestary":
            points = 9
        else:
            return 0

        # unplace and reset meeple
        self.is_placed = False
        self.feature_type = None
        self.orientation = None
        return points
    

    # determines how many points a Meeple scores for an incomplete feature or 
    # for a field at the end of the game
    def end_of_game_scoring(self):
        points = 0
        # determine of feature is partially complete
        if self.feature_type == "road":
            # points = number of tiles in the partial road
            pass
        elif self.feature_type == "city":
            # points = 1 per each tile in partial city, extra 1 if tile with coat of arms
            pass
        elif self.feature_type == "monestary":
            # points = number of tiles surrounding monestary + 1 for monestary itself
            pass
        else:
            # points = 3 points per completed city the field is touching
            pass

        # unplace and reset meeple
        self.is_placed = False
        self.feature_type = None
        self.orientation = None
        return points
    

    # getter methods
    
    # returns player that Meeple belongs to
    def get_player(self):
        return self.player


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
    

    # returns orientation of Meeple
    def get_orientation(self):
        return self.orientation
    

    # returns Meeple's sprite
    def get_meeple_sprite(self):
        return self.meeple_sprite
    

    # setter methods
    # sets players Meeple blongs to
    def set_player(self, player):
        self.player = player


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
    

    # sets orientation of Meeple
    def set_orientation(self, orientation):
        self.orientation = orientation
    

    # set Meeple's sprite
    def set_meeple_sprite(self, meeple_sprite):
        self.meeple_sprite = meeple_sprite
    

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
    test_meeple_1.place_meeple(test_tile)
    if test_meeple_1.get_is_placed() != True:
        return "FAILED doesn't update placement boolean"
    if test_meeple_1.get_orientation() != "horizontal":
        return "FAILED doesn't update horizontal orientation"
    
    test_meeple_2 = Meeple("Jack", "m2", "red")
    test_meeple_2.set_feature_type("road")
    test_tile = None
    test_meeple_2.place_meeple(test_tile)
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
    test_meeple.place_meeple(test_tile)
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
    # TODO finish implementing horizontal sprite
    test_meeple_1 = Meeple("Jack", "m1", "red")
    # manually set feature type
    test_meeple_1.set_feature_type("city")
    test_tile = None
    test_meeple_1.place_meeple(test_tile)
    if test_meeple_1.get_meeple_sprite() != "\"/meeple_sprites/red_sprite.png\"":
        return "FAILED incorrect file path for vertical sprite"
    
    test_meeple_2 = Meeple("Jack", "m2", "red")
    test_meeple_2.set_feature_type("field")
    test_meeple_2.place_meeple(test_tile)
    if test_meeple_2.get_meeple_sprite() != "\"/meeple_sprites/red_horizontal_sprite.png\"":
        return "FAILED incorrect file path for horizontal sprite"
    return "PASSED"


if __name__ == "__main__":
    print("test one: ", test_one())
    print("test two: ", test_two())
    print("test three: ", test_three())
    print("test four: ", test_four())