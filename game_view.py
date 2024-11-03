""" This file is the game view that is iteractive to allow user to move tiles
    and meeples on a board for the game carcassonne."""

import arcade
import arcade.gui
import scoreboard_view
import help_view
import tile
import random

# Global Var: Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
START = 0
END = 2000
STEP = 50
# Global Var: Sprite Scaling
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_SCORE = 1
SPRITE_SCALING_TILE = 0.5
SPRITE_SCALING_HELP = 1
# Global Var: Text
DEFAULT_LINE_HEIGHT = 45
ROW_COUNT = 6
COLUMN_COUNT = 6
MARGIN = 5
WIDTH = 60
HEIGHT = 60
BOARD_X = 400
BOARD_Y = 400

class GameView(arcade.View):

    def __init__(self, curr_tile, curr_meeple, settings):
        super().__init__()
        # Initialize Background Image
        self.background = arcade.load_texture("images/wood.jpg")
        # Initalize sprite lists
        self.player_list = None
        self.scoreboard_list = None
        self.tile_list = None
        self.help_list = None
        # Initalize current meeple and current tile position
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        # create done button
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # creating horizontal box
        self.h_box = (arcade.gui.
                      UIBoxLayout(vertical=False))
        self.done_button = (arcade.gui.
                           UIFlatButton(text="DONE", width=100))
        # add box to manager
        self.h_box.add(self.done_button.with_space_around( top=400))
        # create event for done
        self.done_button.on_click = self.on_done
        # Styling container for button
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.h_box,
                style=None)
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                child=self.h_box,
                style=None)
        )
        # Initalize settings
        self.settings = settings
        self.start_tile = tile.start
        self.tile_list = tile.tiles
        # load the tiles into settings for first round
        if settings.current_round == 1:
            # count keeps track of tile ID
            count = 0
            for i in self.tile_list:
                self.settings.tiles.append((count,i))
                count+=1
            # shuffle list
            random.shuffle(self.settings.tiles)

        # Add tile grid
        self.grid_sprite_list = arcade.SpriteList()

        # This will be a two-dimensional grid of sprites to mirror the two
        # dimensional grid of numbers. This points to the SAME sprites that are
        # in grid_sprite_list, just in a 2d manner.
        self.grid_sprites = []

        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        # Create a list of solid-color sprites to represent each grid location
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN) + 200
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN) + 150
                #TODO: Update this when a tile is placed.
                sprite_color = arcade.make_transparent_color([0,0,0], 100)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, sprite_color)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)



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

        # Start Tile Sprite
        tile = self.start_tile.image
        self.tile_sprite = arcade.Sprite(tile,
                                         SPRITE_SCALING_TILE)
        self.tile_sprite.center_x = SCREEN_WIDTH/2
        self.tile_sprite.center_y = SCREEN_HEIGHT/2
        self.tile_list.append(self.tile_sprite)

        # if first round add start tile to placed tile
        if self.settings.current_round == 1:
            self.settings.add_placed_tile((99,self.start_tile), SCREEN_WIDTH/2,
                                           SCREEN_HEIGHT/2)

        # Keep location of placed tile sprites
        for item in self.settings.placed_tiles:
            object = item[0][1]
            tile = object.image
            self.tile_sprite = arcade.Sprite(tile,
                                             SPRITE_SCALING_TILE)
            self.tile_sprite.center_x = item[1]
            self.tile_sprite.center_y = item[2]
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
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,
                                      SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      self.background)
        # Drawing Sprite Lists
        self.grid_sprite_list.draw()
        self.scoreboard_list.draw()
        self.help_list.draw()
        self.tile_list.draw()
        self.player_list.draw()
        # Drawing Button
        self.manager.draw()
        # Drawing Text, Need From Player Class?
        start_x = 500
        start_y = 75
        # Player text from player class
        arcade.draw_text(self.settings.get_current_player().name+"'s Turn",
                         start_x,
                         start_y,
                         arcade.color.WHITE,
                         20,
                         font_name="Kenney Future")


        # Drawing Text, For Meeples.
        start_meeple_x = 10
        start_meeple_y = 50
        arcade.draw_text("# Meeples",
                         start_meeple_x,
                         start_meeple_y,
                         arcade.color.WHITE,
                         12,
                         font_name="Kenney Future")

        # Drawing Text, For Tile.
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
            self.tile_sprite.center_x = self.curr_tile.get_x()
            self.tile_sprite.center_y = self.curr_tile.get_y()

        # if meeple moved update with new location
        if self.curr_meeple.get_moved():
            self.tile_sprite.center_x = self.curr_meeple.get_x()
            self.tile_sprite.center_y = self.curr_meeple.get_y()

    def on_done(self, event):
        """ If the user presses the button, the logic will
        be checked, the round will increment if player 4 is
        current player, otherwise it will increment next
        player
        """
        # get player count for indexing
        count = self.settings.get_player_count() - 1
        # if the last player to go, increment current round
        if self.settings.get_current_player() == self.settings.current_players[count]:
            round = self.settings.get_current_round() + 1
            self.settings.set_current_round(round)

        # get current player
        current_player = self.settings.get_current_player()
        # increment player to next player in the list
        for player in range(len(self.settings.current_players)):
            if current_player == self.settings.current_players[player]:
                # if current player is last in list, current player is first
                if current_player == self.settings.current_players[-1]:
                    current_player = self.settings.current_players[0]
                    self.settings.set_current_player(current_player)
                else:
                    # increment to next player in list
                    current_player = self.settings.current_players[player+1]
                    self.settings.set_current_player(current_player)
                    break

        # change tile to next tile in list,
        # TODO: add a random incremnt, this is just to see it if works
        self.curr_tile.set_moved(False)
        self.curr_tile.set_y(100)
        self.curr_tile.set_x(200)
        tile = self.settings.tiles[self.settings.tile_count][1].image
        self.tile_sprite = arcade.Sprite(tile,
                                      SPRITE_SCALING_TILE)
        self.tile_sprite.center_x = self.curr_tile.get_x()
        self.tile_sprite.center_y = self.curr_tile.get_y()
        self.tile_list.append(self.tile_sprite)
        self.settings.increment_tile_count()
        # TODO: validate if tile is in valid spot
        if self.settings.tile_count != 0:
            # add placed tile to placed_tile list in settings
            self.settings.add_placed_tile(self.settings.tiles[self.settings.tile_count - 1],
                                          self.tile_sprite.center_x, self.tile_sprite.center_y)


    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # TODO: use this to resize
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        # Allow Sprite to Move With Mouse
        try:
            if self.dragging_sprite:
                self.dragging_sprite.center_x += delta_x
                self.dragging_sprite.center_y += delta_y
        except AttributeError:
            pass

        # Allow Sprite to Move With Mouse
        try:
            if self.dragging_meeple:
                self.dragging_meeple.center_x += delta_x
                self.dragging_meeple.center_y += delta_y
        except AttributeError:
            pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        # If Left Button on Mouse Clicked on Tile
        if button == arcade.MOUSE_BUTTON_LEFT:
            clicked_tile = arcade.get_sprites_at_point((x, y),
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
                # if current tile is clicked and is the newest tile, dragging is possible
                if clicked_tile[0] == self.tile_list[-1]:
                    self.dragging_sprite = clicked_tile[0]

        if button == arcade.MOUSE_BUTTON_RIGHT:
            clicked_tile = arcade.get_sprites_at_point((x, y)
                                                       ,self.tile_list)
            if clicked_tile:
                # if current tile is clicked and is the newest tile, rotating is possible
                if clicked_tile[0] == self.tile_list[-1]:
                    self.rotating_tile = clicked_tile[0]



    def on_mouse_release(self, x, y, button, key_modifiers):
        """ Called when a user releases a mouse button.  """

        # If Left Mouse is Released stop dragging
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging_sprite = None
            self.dragging_meeple = None

            # Snaps tiles into grid
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    # If the tile being dragged overlaps a certain amount with a
                    # square in the grid it is snapped into place
                    if (self.grid_sprites[i][j].collides_with_point
                        ([self.tile_sprite.center_x, self.tile_sprite.center_y])):
                        self.tile_sprite.center_x = self.grid_sprites[i][j].center_x
                        self.tile_sprite.center_y = self.grid_sprites[i][j].center_y

            # If scoreboard was clicked then released
            clicked_scoreboard = arcade.get_sprites_at_point((x, y),
                                                             self.scoreboard_list)
            # If help was clicked then released
            clicked_help = arcade.get_sprites_at_point((x, y),
                                                       self.help_list)
            # If help clicked
            if clicked_help:
                # create new list to updat placed sprites
                new_list = []
                # save sprites location
                self.curr_tile.set_moved(True)
                self.curr_tile.set_x(self.tile_sprite.center_x)
                self.curr_tile.set_y(self.tile_sprite.center_y)
                # update the placed tiles, with new coordinates
                for item in self.settings.placed_tiles:
                    if item == self.settings.placed_tiles[-1]:
                        new_list.append((item[0],self.curr_tile.get_x(),self.curr_tile.get_y()))
                    else:
                        new_list.append(item)
                self.settings.placed_tiles = new_list
                self.curr_meeple.set_moved(True)
                self.curr_meeple.set_x(self.player_sprite.center_x)
                self.curr_meeple.set_y(self.player_sprite.center_y)
                # change view to help screen
                help = help_view.HelpView(self.curr_tile, self.curr_meeple, self.settings)
                help.setup()
                self.window.show_view(help)
            # if scoreboard clicked
            if clicked_scoreboard:
                new_list = []
                # save sprite locations
                self.curr_tile.set_moved(True)
                self.curr_tile.set_x(self.tile_sprite.center_x)
                self.curr_tile.set_y(self.tile_sprite.center_y)
                # update the placed tiles, with new coordinates
                for item in self.settings.placed_tiles:
                    if item == self.settings.placed_tiles[-1]:
                        new_list.append((item[0], self.curr_tile.get_x(), self.curr_tile.get_y()))
                    else:
                        new_list.append(item)
                self.curr_meeple.set_moved(True)
                self.curr_meeple.set_x(self.player_sprite.center_x)
                self.curr_meeple.set_y(self.player_sprite.center_y)
                # change view to scoreboard
                scoreboard = scoreboard_view.ScoreboardView(self.curr_tile, self.curr_meeple, self.settings)
                scoreboard.setup()
                self.window.show_view(scoreboard)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            # If the right mouse button is clicked then unclicked, rotate tile
            # TODO: validate that only the current tile can be rotated/moved
            if self.rotating_tile:
                self.rotating_tile.change_angle = True
                self.rotating_tile.angle = 90 + self.rotating_tile.angle
                self.curr_tile.tile.rotate_tile()
