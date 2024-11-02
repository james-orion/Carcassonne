""" This file is the name view that displays text fields to allow players
    enter names for the game carcassonne."""

import arcade
import arcade.gui
import game_settings
import choose_view
import player
import color_view

class NameView(arcade.View):
    """ View to Open Game"""

    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        # create manager to deal with buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.input_field = []
        self.input_field_text = ["Player 1",
                                 "Player 2",
                                 "Player 3",
                                 "Player4"]

        # creating horizontal boxes to allow
        self.h_box = (arcade.gui.
                      UIBoxLayout(vertical=False))
        self.v_box = (arcade.gui.
                      UIBoxLayout())
        back_button = (arcade.gui.
                       UIFlatButton(text="BACK", width=100))
        self.h_box.add(back_button.with_space_around(right=200))
        back_button.on_click = self.on_back
        next_button = (arcade.gui.
                       UIFlatButton(text="NEXT", width=100))
        self.h_box.add(next_button.with_space_around(left=200))
        next_button.on_click = self.on_click_next
        # Create an text input field per player count
        for i in range(self.settings.get_player_count()):
            self.input_field.append(arcade.gui.UIInputText(
                color=arcade.color.DARK_BLUE_GRAY,
                font_size=24,
                width=200,
                text=self.input_field_text[i]))
            self.v_box.add(self.input_field[i].
                           with_space_around(bottom=20))
        # Styling container for buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                child=self.v_box,
                style=None)
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.h_box,
                style=None)
        )

    def update_text(self):
        """" This will update the text Input """
        self.label.text = self.input_field.text
        self.input_field_text = self.label.text


    def on_click(self, event):
        """ This triggers text to be updated from
                being clicked"""
        self.update_text()

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
        arcade.draw_text("Enter Names",
                         self.window.width / 2,
                         self.window.height - 50,
                         arcade.color.WHITE,
                         font_size=40,
                         anchor_x="center",
                         font_name="Kenney Future")

        self.manager.draw()
        # Draw input text per players chosen

    def on_back(self, event):
        """ If the user presses button change view to go back to the st
            screen. """
        choose = choose_view.ChooseView()
        self.window.show_view(choose)

    def on_click_next(self, event):
        """ If the user presses the  button, start the game. """

        # Add players to settings
        for i in range(self.settings.get_player_count()):
            p = player.Player()
            p.set_name(self.input_field[i].text)
            self.settings.add_current_players(p)
            if i == 0:
                self.settings.set_current_player(p)
        self.manager.disable()
        game_view = color_view.ColorView(self.settings)
        self.window.show_view(game_view)

