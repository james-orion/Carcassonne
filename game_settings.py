"""
This file, updates the current tile placement of the game

"""

class game_settings:

    def __init__(self):
        self.current_round = 0
        self.current_players = []
        self.player_count = 0

    def set_current_round(self, round):
        """ This sets the curent round """
        self.current_round= round


    def add_current_players(self, player):
        """ This adds players """
        self.current_players.append(player)

    def set_player_count(self, count):
        """ This sets player count"""
        self.player_count = count

    def get_current_round(self):
        """"   This returns the current round"""
        return self.current_round

    def get_current_players(self):
        """ This returns the current players"""
        return self.current_players

    def get_player_count(self):
        """"   This returns player count """
        return self.player_count




