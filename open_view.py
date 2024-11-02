""" This file is the opening view that displays game title for
    the game carcassonne"""

import arcade
import choose_view

class OpenView(arcade.View):
    """ View to Open Game"""

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
        arcade.draw_text("Carcassonne",
                         self.window.width / 2,
                         self.window.height / 2,
                         arcade.color.WHITE,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the button, start the game.
            and change view"""
        choose = choose_view.ChooseView()
        self.window.show_view(choose)
