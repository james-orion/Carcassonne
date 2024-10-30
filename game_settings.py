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


    def set_current_round(self, round):
        """ This sets the current round """
        self.current_round = round

    def add_current_players(self, player):
        """ This adds players """
        self.current_players.append(player)

    def set_current_player(self, player):
        """ This sets current player """
        self.current_player = player

    def set_player_count(self, count):
        """ This sets player count"""
        self.player_count = count

    def increment_tile_count(self):
        """ This sets player count"""
        self.tile_count += 1


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



