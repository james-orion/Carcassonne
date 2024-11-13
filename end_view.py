"""This file represents the view of the end screen of the game --- displays the winner and ends the game"""

import arcade
import arcade.gui
from player import Player

# Global Variables: screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class EndView(arcade.View):
    """ View to show Scoreboard """

    def __init__(self, settings):
        super().__init__()
        self.settings = settings

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        pass

    def on_show_view(self):
        """ This is run once when we switch to this view """
        self.background = arcade.load_texture("images/notepad.jpg.png")
        arcade.set_viewport(0,
                            self.window.width,
                            0,
                            self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,
                                      SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      self.background)
        # Title for Score board
        arcade.draw_text("The game is over!",
                         self.window.width / 2 + 30,
                         self.window.height - 75,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")

        # set initial line (x,y)
        name_line = 250
        score_line = 550
        height_line = self.window.height - 400
        # for each player, print name and score
        for player in self.settings.current_players:
            arcade.draw_text(player.name, name_line,
                         height_line,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="left",
                         font_name="Kenney Future")
            arcade.draw_text(player.score, score_line,
                         height_line,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="left",
                         font_name="Kenney Future")
            # increment line height
            height_line -= 60

        arcade.draw_text("The winner is: ",
                         self.window.width / 2 + 30,
                         self.window.height - 150,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")
        winning_player = Player()
        winning_player.score = 0
        for player in self.settings.current_players:
            if player.score >= winning_player.score:
                winning_player = player
        arcade.draw_text(winning_player.name,
                         self.window.width / 2 + 30,
                         self.window.height - 250,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")