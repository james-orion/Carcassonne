""" This file is the name view that displays text fields to allow players
    enter names for the game carcassonne."""

import arcade
import arcade.gui
from arcade import draw_texture_rectangle, draw_rectangle_filled

import game_settings
import choose_view
import player
import color_view
# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
class NameView(arcade.View):
    """ View to Open Game"""

    def __init__(self, settings, my_player):
        super().__init__()
        self.settings = settings
        # Initialize Background Image
        self.background = arcade.load_texture("images/castle.jpeg")
        self.my_player = my_player
        self.next_sound = arcade.load_sound("images/next.mp3")
        # create manager to deal with buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.input_field = []
        self.input_field_text = ["Player 1",
                                 "Player 2",
                                 "Player 3",
                                 "Player4"]
        # set game to True for name validation
        self.game = True
        # set max input to size 11
        self.max = 11
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
                text_color=arcade.color.BLACK,
                font_size=24,
                width=200,
                text=self.input_field_text[i],
                style=None))
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
        print("hi")
        self.update_text()

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.STEEL_BLUE)
        arcade.set_viewport(0,
                            self.window.width,
                            0,
                            self.window.height)

    def on_update(self, delta_time: float):
        """ This method checks input length """
        for input_field in self.input_field:
            # Limit the length of text to the maximum allowed
            if len(input_field.text) > self.max:
                input_field.text = input_field.text[:self.max-1]

    def on_draw(self):
        """ Draw this view """
        self.clear()
        # Drawing the background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,
                                      SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      self.background)
        arcade.draw_text("Enter Names",
                         self.window.width / 2,
                         self.window.height - 100,
                         arcade.color.BLACK,
                         font_size=40,
                         anchor_x="center",
                         font_name="Kenney Future")
        color = arcade.make_transparent_color([240, 255, 255], 150)
        arcade.draw_rectangle_filled(self.v_box.center_x, self.v_box.center_y, self.v_box.width+50,
                                               self.v_box.height+50, color)

        self.manager.draw()

        text_height = 150
        self.game = True
        # check to see length of input larger than 0
        for i in range(len(self.input_field)):
            if len(self.input_field[i].text) < 1:
                arcade.draw_text(f"Player {i + 1}, Enter Name",
                                 self.window.width / 2, self.window.height - text_height,
                                 arcade.color.BLACK, font_size=20, anchor_x="center",
                                 font_name="Kenney Future")
                self.game = False
                text_height += 50
                break

            # can't have duplicate names
            for j in range(i + 1, len(self.input_field)):
                if self.input_field[i].text == self.input_field[j].text:
                    arcade.draw_text("Name's Must Be Different",
                                     self.window.width / 2, self.window.height - text_height,
                                     arcade.color.BLACK, font_size=20, anchor_x="center",
                                     font_name="Kenney Future")
                    self.game = False
                    text_height += 50
                    break


    def on_back(self, event):
        """ If the user presses button change view to go back to the st
            screen. """
        self.manager.disable()
        self.next_sound.play()
        choose = choose_view.ChooseView(self.my_player)
        self.window.show_view(choose)

    def on_click_next(self, event):
        """ If the user presses the  button, start the game. """

        if self.game == True:
            # Add players to settings
            for i in range(self.settings.get_player_count()):
                p = player.Player()
                p.set_name(self.input_field[i].text)
                self.settings.add_current_players(p)
                if i == 0:
                    self.settings.set_current_player(p)
            self.manager.disable()
            self.next_sound.play()
            game_view = color_view.ColorView(self.settings, self.my_player)
            self.window.show_view(game_view)


