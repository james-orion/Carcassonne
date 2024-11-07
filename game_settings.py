"""
This file, updates the current game settings

"""
import player

class game_settings:

    def __init__(self):
        self.current_round = 1
        self.current_players = []
        self.player_count = 0
        self.tiles = []
        self.current_player = ""
        self.placed_tiles = []
        self.tile_count = 0
        self.total_rotation = {}
        self.feature_container = []
        self.button_text = "START"
        self.previous_coor_x = -1
        self.previous_coor_y = -1
        self.meeples = []

    def set_current_round(self, round):
        """ This sets the current round """
        self.current_round = round

    def add_current_players(self, player):
        """ This adds players """
        self.current_players.append(player)

    def increment_rotation(self, tile):
        """ This increments the rotation of a tile"""
        # If tile already exists, increment its rotation by 90
        if tile in self.total_rotation:
            self.total_rotation[tile] += 90
        # If tile doesn't exist, add it with an initial rotation to 90
        else:
            self.total_rotation[tile] = 90

    def set_current_player(self, player):
        """ This sets current player """
        self.current_player = player

    def set_player_count(self, count):
        """ This sets player count"""
        self.player_count = count

    def set_button_text(self, text):
        """ This sets the button text"""
        self.button_text = text
        
    def increment_tile_count(self):
        """ This increments to next tile"""
        self.tile_count += 1

    def add_placed_tile(self, tile, x, y):
        """This adds to placed tiles"""
        self.placed_tiles.append((tile, x, y))

    def add_tile_to_list(self, og_tile, tile, side):
        """This adds to tile to list of feature based on the side it is connected to"""
        print("PRINTING SIDE SENT TO FUNCTION", side)
        print("PRINTING OG_TILE SENT TO FUNCTION", og_tile)
        print("PRINTING tile SENT TO FUNCTION", tile)
        if side == self.placed_tiles[0][0][1].top:
            for row in self.feature_list:
                if og_tile in row and "city" in row:
                    row.append(tile)
        elif side == self.placed_tiles[0][0][1].left:
            for row in self.feature_list:
                if og_tile in row and "road" in row:
                    row.append(tile)
        else:
            for row in self.feature_list:
                if og_tile in row and "field" in row:
                    row.append(tile)

    
    def get_rotation_click(self, tile_num):
        """This returns the total rotation on tile"""
        for key, val in self.total_rotation.items():
            print("This is the key", key, "this is its val", val)
            if key == tile_num:
                return val
        return 0

    def get_placed_tiles(self):
        """This returns the placed tiles"""
        return self.placed_tiles

    def get_tile_count(self):
        """"   This returns the current round"""
        return self.tile_count

    def get_current_round(self):
        """"   This returns the current round"""
        return self.current_round

    def get_current_players(self):
        """ This returns the current players"""
        return self.current_players

    def get_player_count(self):
        """"   This returns player count """
        return self.player_count

    def get_current_player(self):
        """"   This returns player count """
        return self.current_player

    def get_current_tiles(self):
        return self.placed_tiles

    def place_tile(self, tile):
        """ Adds a tile to the list of placed tiles"""
        self.placed_tiles.append(tile)

    def add_meeple(self, meeple):
        self.meeples.append(meeple)

    def get_meeples(self):
        return self.meeples