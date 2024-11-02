""" This file is the choose player number view that displays amount of players
    1-4 to play the game carcassonne."""

import arcade
import arcade.gui
import name_view
import game_settings



class ChooseView(arcade.View):
    """ View to Open Game"""

    def __init__(self):
        super().__init__()
        # Initalize manager for container and butttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # creating horizontal boxes to allow
        # user to pick number of players
        self.h_box = (arcade.gui.
                      UIBoxLayout(vertical=False))
        self.one_button = (arcade.gui.
                           UIFlatButton(text="1", width=100))
        self.h_box.add(self.one_button.with_space_around(left=10))
        self.one_button.on_click = self.on_choose_one

        two_button = (arcade.gui.
                      UIFlatButton(text="2", width=100))
        self.h_box.add(two_button.with_space_around(left=10))
        two_button.on_click = self.on_choose_two

        three_button = (arcade.gui.
                        UIFlatButton(text="3", width=100))
        self.h_box.add(three_button.with_space_around(left=10))
        three_button.on_click = self.on_choose_three

        four_button = (arcade.gui.
                       UIFlatButton(text="4", width=100))
        self.h_box.add(four_button.with_space_around(left=10))
        four_button.on_click = self.on_choose_four

        # Styling container for buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                child=self.h_box,
                style=None)
        )
        # creating instance of settings
        self.settings = game_settings.game_settings()

    def on_show_view(self):
        """ This is run once when we switch to this view """
        # TODO: pick a color scheme maybe add images
        arcade.set_background_color(arcade.csscolor.STEEL_BLUE)
        arcade.set_viewport(0,
                            self.window.width,
                            0,
                            self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("How Many Players?",
                         self.window.width / 2,
                         self.window.height - 200,
                         arcade.color.WHITE,
                         font_size=40,
                         anchor_x="center",
                         font_name="Kenney Future")

        self.manager.draw()

    def on_choose_one(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(1)
        print(self.settings.get_player_count())
        name = name_view.NameView(self.settings)
        self.window.show_view(name)

    def on_choose_two(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(2)
        print(self.settings.get_player_count())
        name = name_view.NameView(self.settings)
        self.window.show_view(name)

    def on_choose_three(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(3)
        print(self.settings.get_player_count())
        name= name_view.NameView(self.settings)
        self.window.show_view(name)

    def on_choose_four(self, event):
        """ If the user presses the mouse button, the player count
        will be set. and change view """
        self.settings.set_player_count(4)
        print(self.settings.get_player_count())
        name = name_view.NameView(self.settings)
        self.window.show_view(name)

