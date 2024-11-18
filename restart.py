""" This file is the help view that displays how to play the game, and how to
    score points for the game carcassonne."""

import arcade
import arcade.gui
import game_view

# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class Restart(arcade.View):
    """ View to show Help View"""

    def __init__(self, curr_tile, curr_meeple, settings, feat, my_player):
        super().__init__()
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        self.settings = settings
        self.feat = feat
        self.my_player = my_player


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        pass


    def on_draw(self):
        """ Draw this view """
        self.clear()
        game = game_view.GameView(self.curr_tile, self.curr_meeple, self.settings, self.feat, self.my_player)
        game.setup()
        self.window.show_view(game)

