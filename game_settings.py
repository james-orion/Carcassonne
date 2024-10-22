"""
This file, updates the current game settings

"""

class game_settings:

    def __init__(self):
        self.current_round = 0
        self.current_players = []
        self.player_count = 0

    def set_current_round(self, round):
        """ This sets the curent tile placement"""
        self.current_round= round


    def add_current_players(self, player):
        """ This adds"""
        self.current_players.append(player)

    def set_player_count(self, count):
        """ This sets the moved boolean"""
        self.player_count = count

    def get_current_round(self):
        """"   This returns the current tile placement x"""
        return self.current_round

    def get_current_players(self):
        """ This returns the current tile placement y"""
        return self.current_players

    def get_player_count(self):
        """"   This returns the moved boolean """
        return self.player_count




