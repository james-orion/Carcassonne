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
        self.meeple_placed_current_round = False
        self.sound_on = True
        self.music_on = True
        self.done_pressed = False
        self.meeple_screen = False
        self.ai = False

        self.ai_valid = False


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

    def reset_rotation(self, tile):
        """ This sets the rotation of a tile"""
        # If tile already exists, increment its rotation by 90
        if tile in self.total_rotation:
            self.total_rotation[tile] = 0

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

    def get_rotation_click(self, tile_num):
        """This returns the total rotation on tile"""
        for key, val in self.total_rotation.items():
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
    
    def get_meeple_placed_current_round(self):
        return self.meeple_placed_current_round
    
    def set_meeple_placed_current_round(self, is_placed):
        self.meeple_placed_current_round = is_placed

    def add_ai_players(self,name):
        for i in range(4 - self.player_count-1):
            self.current_players.append(player.Player(name, ai = True))