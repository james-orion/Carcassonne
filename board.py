"""

This file is part of Carcassonne board view


"""
import arcade
import arcade.gui

import current_tile
import current_meeple
import game_settings



# Global Var: Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Global Var: Window Title
SCREEN_TITLE = "Carcassonne"
START = 0
END = 2000
STEP = 50
# Global Var: Sprite Scaling
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_SCORE = 1
SPRITE_SCALING_TILE = 0.3
SPRITE_SCALING_HELP = 1
# Global Var: Text
DEFAULT_LINE_HEIGHT = 45

class GameView(arcade.View):

    def __init__(self, curr_tile, curr_meeple, settings):
        super().__init__()
        # Initialize Background Imgae
        self.background = arcade.load_texture("images/wood.jpg")
        # Initalize sprite lists
        self.player_list = None
        self.scoreboard_list = None
        self.tile_list = None
        self.help_list = None
        # Initalize current meeple and current tile position
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        # Initalize settings
        self.settings = settings


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """

        # Create sprite lists
        self.player_list = arcade.SpriteList()
        self.scoreboard_list = arcade.SpriteList()
        self.tile_list = arcade.SpriteList()
        self.help_list = arcade.SpriteList()
        # Meeple sprite
        img = "images/Meeple.jpg"
        self.player_sprite = arcade.Sprite(img,
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = self.curr_meeple.get_x()
        self.player_sprite.center_y = self.curr_meeple.get_y()
        self.player_list.append(self.player_sprite)
        # Scoreboard Sprite
        scoreboard = ":resources:onscreen_controls/shaded_dark/hamburger.png"
        self.scoreboard_sprite = arcade.Sprite(scoreboard,
                                               SPRITE_SCALING_SCORE)
        self.scoreboard_sprite.center_x = 750
        self.scoreboard_sprite.center_y = 475
        self.scoreboard_list.append(self.scoreboard_sprite)
        # Tile Sprite
        tile = "images/tile.jpg"
        self.tile_sprite = arcade.Sprite(tile,
                                         SPRITE_SCALING_TILE)
        self.tile_sprite.center_x = self.curr_tile.get_x()
        self.tile_sprite.center_y = self.curr_tile.get_y()
        self.tile_list.append(self.tile_sprite)

        # Help Sprite
        help = ":resources:onscreen_controls/shaded_dark/gear.png"
        self.help_sprite = arcade.Sprite(help,
                                         SPRITE_SCALING_HELP)
        self.help_sprite.center_x = 750
        self.help_sprite.center_y = 550
        self.help_list.append(self.help_sprite)


    def on_draw(self):
        """ Render the screen. """
        # Start With a Fresh Screen
        self.clear()
        # Start the Rendering Process
        arcade.start_render()

        # Drawing the background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,
                                      SCREEN_HEIGHT/2,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      self.background)
        # Drawing Sprite Lists
        self.scoreboard_list.draw()
        self.help_list.draw()
        self.tile_list.draw()
        self.player_list.draw()
        # Drawing Text, Need From Player Class?
        start_x = 500
        start_y = 75
        # player.Player.get_name()
        arcade.draw_text("Player 1",
                         start_x,
                         start_y,
                         arcade.color.WHITE,
                         30,
                         font_name="Kenney Future")

        # Drawing Text, For Meeples. Need Meepl count from player?
        start_meeple_x = 10
        start_meeple_y= 50
        arcade.draw_text("# Meeples",
                         start_meeple_x,
                         start_meeple_y,
                         arcade.color.WHITE,
                         12,
                         font_name="Kenney Future")

        # Drawing Text, For Tile. Need Tile From Tile Class?
        start_tile_x = 200
        start_tile_y = 50
        arcade.draw_text("Your Tile",
                         start_tile_x,
                         start_tile_y,
                         arcade.color.WHITE,
                         12,
                         font_name="Kenney Future")



    def on_update(self, delta_time):
        """ All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it. """

        # if tile moved update with new location
        if self.curr_tile.get_moved():
            print("moved")
            print(self.curr_tile.get_x())
            self.tile_sprite.center_x = self.curr_tile.get_x()
            self.tile_sprite.center_y = self.curr_tile.get_y()

        # if meeple moved update with new location
        if self.curr_meeple.get_moved():
            self.tile_sprite.center_x = self.curr_meeple.get_x()
            self.tile_sprite.center_y = self.curr_meeple.get_y()


    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # TODO: use this to resize
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        # Allow Sprite to Move With Mouse
        if self.dragging_sprite:
            self.dragging_sprite.center_x += delta_x
            self.dragging_sprite.center_y += delta_y

        # Allow Sprite to Move With Mouse
        if self.dragging_meeple:
            self.dragging_meeple.center_x += delta_x
            self.dragging_meeple.center_y += delta_y

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        # If Left Button on Mouse Clicked on Tile
        if button == arcade.MOUSE_BUTTON_LEFT:
            clicked_tile = arcade.get_sprites_at_point((x,y),
                                                       self.tile_list)

            clicked_meeple = arcade.get_sprites_at_point((x, y),
                                                         self.player_list)
            new_meeple = arcade.get_sprites_at_point((x, y),
                                                         self.player_list)
            # meeples, allow dragging
            if clicked_meeple:
                self.dragging_meeple = new_meeple[0]

            # Allow dragging to be possible
            if clicked_tile:
                self.dragging_sprite = clicked_tile[0]

    def on_mouse_release(self, x, y, button, key_modifiers):
        """ Called when a user releases a mouse button.  """

        # If Left Mouse Is Relased stop dragging
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging_sprite = None
            self.dragging_meeple = None
            # If scoreboard was clicked then released
            clicked_scoreboard = arcade.get_sprites_at_point((x, y),
                                                       self.scoreboard_list)
            # If help was clicked then released
            clicked_help = arcade.get_sprites_at_point((x, y),
                                                          self.help_list)
            # If help clicked
            if clicked_help:
                # save sprites location
                self.curr_tile.set_moved(True)
                self.curr_tile.set_x(self.tile_sprite.center_x)
                self.curr_tile.set_y(self.tile_sprite.center_y)
                self.curr_meeple.set_moved(True)
                self.curr_meeple.set_x(self.player_sprite.center_x)
                self.curr_meeple.set_y(self.player_sprite.center_y)
                # change view to help screen
                help_view = HelpView(self.curr_tile, self.curr_meeple, self.settings)
                help_view.setup()
                self.window.show_view(help_view)
            # if scoreboard clicked
            if clicked_scoreboard:
                # save sprite locations
                self.curr_tile.set_moved(True)
                self.curr_tile.set_x(self.tile_sprite.center_x)
                self.curr_tile.set_y(self.tile_sprite.center_y)
                self.curr_meeple.set_moved(True)
                self.curr_meeple.set_x(self.player_sprite.center_x)
                self.curr_meeple.set_y(self.player_sprite.center_y)
                # change view to scoreboard
                scoreboard_view = ScoreboardView(self.curr_tile, self.curr_meeple, self.settings)
                scoreboard_view.setup()
                self.window.show_view(scoreboard_view)

class NameView(arcade.View):
    """ View to Open Game"""
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        # create manager to deal with buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.input_field= []
        self.input_field_text = ["Player 1",
                                 "Player 2",
                                 "Player 3",
                                 "Player4"]

        # TODO: call player class, add to the current players
        # self.player_one = player.Player()
        # self.player_two = player.Player()
        # self.player_three = player.Player()
        # self.player_four = player.Player()
        # creating horizontal boxes to allow
        # TODO: add text input for players, call player class
        self.v_box = (arcade.gui.
                      UIBoxLayout())
        back_button = (arcade.gui.
                       UIFlatButton(text="BACK", width=100))
        self.v_box.add(back_button.with_space_around(left=10))
        back_button.on_click = self.on_back
        next_button = (arcade.gui.
                       UIFlatButton(text="NEXT", width=100))
        self.v_box.add(next_button.with_space_around(left=10))
        next_button.on_click = self.on_click_next
        # Create an text input field per player count
        for i in range(self.settings.get_player_count()):
            self.input_field.append(arcade.gui.UIInputText(
                color=arcade.color.DARK_BLUE_GRAY,
                font_size=24,
                width=200,
                text=self.input_field_text[i]))
            self.v_box.add(self.input_field[i].
                           with_space_around(left=10))
        # Styling container for buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                child=self.v_box,
                style=None)
        )

    def update_text(self):
        """" This will update the text Input """
        self.label.text = self.input_field.text
        self.input_field_text = self.label.text

    def on_click(self, event):
        """ This triggers an event from being clicked"""
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
                         self.window.height-50,
                         arcade.color.WHITE,
                         font_size=40,
                         anchor_x="center",
                         font_name="Kenney Future")

        self.manager.draw()
        # Draw input text per players chosen


    def on_back(self, event):
        """ If the user presses button change view to go back to the st
            screen. """
        choose_view = ChooseView()
        self.window.show_view(choose_view)

    def on_click_next(self, event):
        """ If the user presses the  button, start the game. """
        # TODO: create player object and add to settings

        # change screen
        self.curr_tile = current_tile.current_tile()
        self.curr_meeple = current_meeple.current_meeple()
        game_view = GameView(self.curr_tile, self.curr_meeple, self.settings)
        game_view.setup()
        self.window.show_view(game_view)

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
                         self.window.height-200,
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
        name_view = NameView(self.settings)
        self.window.show_view(name_view)

    def on_choose_two(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(2)
        print(self.settings.get_player_count())
        name_view = NameView(self.settings)
        self.window.show_view(name_view)

    def on_choose_three(self, event):
        """ If the user presses the button, the player count
        will be set. and change view"""
        self.settings.set_player_count(3)
        print(self.settings.get_player_count())
        name_view = NameView(self.settings)
        self.window.show_view(name_view)

    def on_choose_four(self, event):
        """ If the user presses the mouse button, the player count
        will be set. and change view """
        self.settings.set_player_count(4)
        print(self.settings.get_player_count())
        name_view = NameView(self.settings)
        self.window.show_view(name_view)


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
        choose_view = ChooseView()
        self.window.show_view(choose_view)

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
                         self.window.width / 2 +  30,
                         self.window.height - 60 ,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")
        # TODO: Player and Numbers maybe in for loop
        # for i in player.player_count
            # arcade.draw_text(player.get_name(), 150,
            #                  self.window.height - 150,
            #                  arcade.color.BLACK,
            #                  font_size=20,
            #                  anchor_x="left",
            #                  font_name="Kenney Future")
            # arcade.draw_text(player.get_score(), 400,
            #                  self.window.height - 150,
            #                  arcade.color.BLACK,
            #                  font_size=20,
            #                  anchor_x="left",
            #                  font_name="Kenney Future")
        arcade.draw_text("Player 1", 150,
                         self.window.height - 150,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="left",
                         font_name="Kenney Future")
        arcade.draw_text("20", 400,
                         self.window.height - 150,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="left",
                         font_name="Kenney Future")
        # Player and Numbers maybe in for loop?
        arcade.draw_text("Player 2", 150,
                         self.window.height - 250,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="left",
                         font_name="Kenney Future")
        arcade.draw_text("30", 400,
                         self.window.height - 250,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="left",
                         font_name="Kenney Future")
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If mouse clicked move to board view """
        # reset boolean for moved sprites for game view
        self.curr_tile.set_moved(False)
        self.curr_meeple.set_moved(False)
        # switch to game view
        game_view = GameView(self.curr_tile, self.curr_meeple, self.settings)
        game_view.setup()
        self.window.show_view(game_view)

class HelpView(arcade.View):
    """ View to show Help View"""

    def __init__(self, curr_tile, curr_meeple, settings):
        super().__init__()
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
        arcade.draw_text("NEED HELP?",
                         self.window.width / 2 +  30,
                         self.window.height - 60 ,
                         arcade.color.BLACK,
                         font_size=50,
                         anchor_x="center",
                         font_name="Kenney Future")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If mouse clicked move to board view """
        # reset the moved booleans for the game screen
        self.curr_tile.set_moved(False)
        self.curr_meeple.set_moved(False)
        # switch to game view
        game_view = GameView(self.curr_tile, self.curr_meeple, self.settings)
        game_view.setup()
        self.window.show_view(game_view)


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = OpenView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
