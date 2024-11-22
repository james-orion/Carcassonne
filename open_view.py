""" This file is the opening view that displays game title for
    the game carcassonne"""

import arcade
import choose_view
# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class OpenView(arcade.View):
    """ View to Open Game"""
    def __init__(self, my_player, game_manager):
        super().__init__()
        # Initialize Background Image
        self.background = arcade.load_texture("images/screen_savor.jpg")
        self.my_player = my_player
        self.game_manager = game_manager


    def on_show_view(self):
        """ This is run once when we switch to this view """
        # TODO: pick a good background, maybe include image
        arcade.set_background_color(arcade.csscolor.STEEL_BLUE)
        arcade.set_viewport(0,
                            self.window.width,
                            0,
                            self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        # Drawing the background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,
                                      SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      self.background)
        arcade.draw_text("Carcassonne",
                         self.window.width / 2,
                         self.window.height / 2,
                         arcade.color.BLACK,
                         font_size=80,
                         anchor_x="center",
                         font_name="Kenney Future")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the button, start the game.
            and change view"""
        choose = choose_view.ChooseView(self.my_player, self.game_manager)
        self.window.show_view(choose)
