""" This file is the scoreboard view that displays player names and score
    for the game carcassonne."""

import arcade
import arcade.gui
import game_view

# Global Var: Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ScoreboardView(arcade.View):
    """ View to show Scoreboard """

    def __init__(self, curr_tile, curr_meeple, settings):
        super().__init__()
        # Initialize Player From Player Class?
        self.player_list = None
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
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
        arcade.draw_text("Scoreboard",
                         self.window.width / 2 + 30,
                         self.window.height - 60,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")
        # set initial line (x,y)
        name_line = 150
        score_line = 400
        height_line = self.window.height - 150
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



    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If mouse clicked move to board view """
        # reset boolean for moved sprites for game view
        self.curr_tile.set_moved(False)
        self.curr_meeple.set_moved(False)
        # switch to game view
        game = game_view.GameView(self.curr_tile, self.curr_meeple, self.settings)
        game.setup()
        self.window.show_view(game)


