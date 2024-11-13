""" This file is the choose color view to allow user to select color
    for the game carcassonne."""

import arcade
import arcade.gui
import current_tile
import current_meeple
import choose_view
import game_view
import feature_placement
# Global Var: Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ColorView(arcade.View):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        # Initialize Background Image
        self.background = arcade.load_texture("images/brick.jpeg")
        self.num_players = self.settings.get_player_count()
        self.players = self.settings.get_current_players()
        self.color_list = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN, arcade.color.YELLOW]
        self.color_list_string = ["red", "blue", "green", "yellow"]
        self.available_colors = ["red", "blue", "green", "yellow"]
        self.selected_colors = []
        self.player_list = arcade.SpriteList()
        # create forward and back buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = (arcade.gui.UIBoxLayout(vertical=False))
        back_button = (arcade.gui.UIFlatButton(text="BACK", width=100))
        self.v_box.add(back_button.with_space_around(left=10, right=100))
        back_button.on_click = self.on_back
        next_button = (arcade.gui.UIFlatButton(text="NEXT", width=100))
        self.v_box.add(next_button.with_space_around(left=10))
        next_button.on_click = self.on_click_next
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center", anchor_y="center",align_y=-180, child=self.v_box, style=None))

        # Create sprite lists
        self.player_list = arcade.SpriteList()
        # Start Tile Sprite
        tile = "meeple_sprites/red_meeple.png"
        self.tile_sprite = arcade.Sprite(tile,
                                         .3)
        self.tile_sprite.center_x = 245+0 * 175
        self.tile_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.tile_sprite)
        tile = "meeple_sprites/blue_meeple.png"
        self.tile_sprite = arcade.Sprite(tile,
                                         .3)
        self.tile_sprite.center_x = 245 + 1 * 175
        self.tile_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.tile_sprite)
        tile = "meeple_sprites/green_meeple.png"
        self.tile_sprite = arcade.Sprite(tile,
                                         .3)
        self.tile_sprite.center_x = 245 + 2 * 175
        self.tile_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.tile_sprite)
        tile = "meeple_sprites/yellow_meeple.png"
        self.tile_sprite = arcade.Sprite(tile,
                                         .3)
        self.tile_sprite.center_x = 245 + 3 * 175
        self.tile_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.tile_sprite)

    def on_click(self):
        self.update_text()

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.STEEL_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)


    def on_draw(self):
        """ Draw this view """
        self.clear()
        # Drawing the background image
        arcade.draw_texture_rectangle(1000 / 2,
                                      650 / 2,
                                      1000,
                                      650,
                                      self.background)
        color = arcade.make_transparent_color([240, 255, 255], 100)
        arcade.draw_rectangle_filled(1000/2, 650/2, 1000,
                                     650, color)
        arcade.draw_text("Select Color:", self.window.width / 2, self.window.height - 50, arcade.color.BLACK, font_size=40, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("Use Keys 1-4 to Choose the Corresponding Color", self.window.width / 2, self.window.height - 80, arcade.color.BLACK, font_size=17, anchor_x="center", font_name="Kenney Future")
        num_colors_selected = len(self.selected_colors)
        if num_colors_selected < self.num_players:
            arcade.draw_text(f"{self.settings.current_players[num_colors_selected].name}\'s Choice", self.window.width / 2, self.window.height - 150, arcade.color.BLACK, font_size=20, anchor_x="center", font_name="Kenney Future") # TODO update with actual users
        else:
            arcade.draw_text(f"All Players Have Chosen, Click Next to Start Game", self.window.width / 2, self.window.height - 150, arcade.color.BLACK, font_size=16, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("All Players Must Select a Color Before Clicking Next", self.window.width / 2, SCREEN_HEIGHT // 2 - 270, arcade.color.BLACK, font_size=15, anchor_x="center", font_name="Kenney Future")
        for i, color in enumerate(self.color_list):
            # draw a square for each color
            arcade.draw_text(f"{self.color_list_string[i]}", 245 + i * 175, SCREEN_HEIGHT // 2 + 70, arcade.color.BLACK, 14, anchor_x="center", font_name="Kenney Future")
            #arcade.draw_rectangle_filled(245 + i * 175, SCREEN_HEIGHT // 2, 100, 100, color)

            # if a player has selected a color, show which color they chose
            for j in range(len(self.selected_colors)):
                x_offset = 185 + self.color_list_string.index(self.selected_colors[j]) * 175
                arcade.draw_text(f"{self.settings.current_players[j].name}", x_offset, SCREEN_HEIGHT // 2 - 80, arcade.color.BLACK, 16, font_name="Kenney Future") # TODO replace with actual name

        self.manager.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        # if key 1-4 is pressed, assign the corresponding color to that player
        if key in (arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3, arcade.key.KEY_4) and len(self.selected_colors) < self.num_players:

            color_index = key - arcade.key.KEY_1

            if self.color_list_string[color_index] in self.available_colors:
                player_choice = self.color_list_string[color_index]
                self.available_colors.remove(player_choice)
                self.selected_colors.append(player_choice)

    # undos last color selection, or returns to name selection if no colors have been chosen
    def on_back(self, event):
        if len(self.selected_colors) == 0:
            self.manager.disable()
            choose = choose_view.ChooseView()
            self.window.show_view(choose)
        else:
            last_color_choice = self.selected_colors[-1]
            self.selected_colors.remove(last_color_choice)
            self.available_colors.append(last_color_choice)

    def on_click_next(self, event):
        # TODO randomly assign remaining colors to computer players
        # TODO assign colors to players once list is implemented
        if len(self.selected_colors) == self.num_players:
            for i in range(self.num_players):
                self.players[i].set_color(self.selected_colors[i])
            self.curr_tile = current_tile.current_tile()
            self.curr_meeple = current_meeple.current_meeple()
            self.manager.disable()
            feature = feature_placement.feature_placements()
            game = game_view.GameView(self.curr_tile, self.curr_meeple, self.settings, feature)
            game.setup()
            self.window.show_view(game)

