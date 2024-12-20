""" This file is the choose player number view that displays amount of players
    1-4 to play the game carcassonne."""

import arcade
import arcade.gui
from arcade.examples.tetris import colors

import name_view
import game_settings

# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class ChooseView(arcade.View):
    """ View to Open Game"""

    def __init__(self, my_player, game_manager):
        super().__init__()
        # Initialize Background Image
        self.background = arcade.load_texture("images/sky.jpg")
        self.my_player = my_player
        self.game_manager = game_manager
        self.next_sound = arcade.load_sound("images/next.mp3")
        # Initalize manager for container and butttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        red_style = {
            "font_name": "Carolingia",
            "font_size": 25,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.REDWOOD,

            # used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            # also used when hovered
            "border_color_pressed": arcade.color.WHITE,
            "font_color_pressed": arcade.color.RED,
        }
        # creating horizontal boxes to allow
        # user to pick number of players
        self.h_box = (arcade.gui.
                      UIBoxLayout(vertical=False))
        self.one_button = (arcade.gui.
                           UIFlatButton(text="1", width=100,style=red_style))
        self.h_box.add(self.one_button.with_space_around(left=10))
        self.one_button.on_click = self.on_choose_one

        two_button = (arcade.gui.
                      UIFlatButton(text="2", width=100,style=red_style))
        self.h_box.add(two_button.with_space_around(left=10))
        two_button.on_click = self.on_choose_two

        three_button = (arcade.gui.
                        UIFlatButton(text="3", width=100,style=red_style))
        self.h_box.add(three_button.with_space_around(left=10))
        three_button.on_click = self.on_choose_three

        four_button = (arcade.gui.
                       UIFlatButton(text="4", width=100 ,style=red_style))
        self.h_box.add(four_button.with_space_around(left=10))
        four_button.on_click = self.on_choose_four

        # Styling container for buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                child=self.h_box,
                )
        )
        # creating instance of settings
        self.settings = game_settings.game_settings()



    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.STEEL_BLUE)
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
        arcade.draw_text("How Many Players?",
                         self.window.width / 2,
                         self.window.height - 200,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Carolingia")

        self.manager.draw()

    def on_choose_one(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(1)
        self.manager.disable()
        self.next_sound.play()
        name = name_view.NameView(self.settings, self.my_player, self.game_manager)
        self.window.show_view(name)

    def on_choose_two(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(2)
        self.manager.disable()
        self.next_sound.play()
        name = name_view.NameView(self.settings, self.my_player, self.game_manager)
        self.window.show_view(name)

    def on_choose_three(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(3)
        self.manager.disable()
        self.next_sound.play()
        name= name_view.NameView(self.settings, self.my_player, self.game_manager)
        self.window.show_view(name)

    def on_choose_four(self, event):
        """ If the user presses the mouse button, the player count
        will be set. and change view """
        self.settings.set_player_count(4)
        self.manager.disable()
        self.next_sound.play()
        name = name_view.NameView(self.settings, self.my_player, self.game_manager)
        self.window.show_view(name)



