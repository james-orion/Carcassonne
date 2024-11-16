""" This file is the help view that displays how to play the game, and how to
    score points for the game carcassonne."""

import arcade
import arcade.gui
import game_view

# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class HelpView(arcade.View):
    """ View to show Help View"""

    def __init__(self, curr_tile, curr_meeple, settings, feat):
        super().__init__()
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        self.settings = settings
        self.feat = feat
        self.page_sound = arcade.load_sound("images/page.mp3")

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
        arcade.draw_text("NEED HELP?",
                         self.window.width / 2 + 30,
                         self.window.height - 60,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If mouse clicked move to board view """
        # reset the moved booleans for the game screen
        self.curr_tile.set_moved(False)
        self.curr_meeple.set_moved(False)
        # sound
        if self.settings.sound_on:
            self.sound_page = self.page_sound.play()
        # switch to game view
        game = game_view.GameView(self.curr_tile, self.curr_meeple, self.settings, self.feat)
        game.setup()
        self.window.show_view(game)
