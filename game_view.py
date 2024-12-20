""" This file is the game view that is iteractive to allow user to move tiles
    and meeples on a board for the game carcassonne."""

import arcade
import arcade.gui
import scoreboard_view
import help_view
import tile
import meeple_placement_view
import random
import end_view
import meeple
import time

from helpful_tips import HelpfulTips
from tutorial import Tutorial

# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
START = 0
END = 2000
STEP = 50
# Global Var: Sprite Scaling
SPRITE_SCALING_PLAYER_VERTICAL = 0.05
SPRITE_SCALING_PLAYER_HORIZONTAL = 0.1
SPRITE_SCALING_SCORE = 1
SPRITE_SCALING_TILE = 0.5
SPRITE_SCALING_HELP = 1
# Global Var: Text
DEFAULT_LINE_HEIGHT = 45
ROW_COUNT = 7
COLUMN_COUNT = 11
TOTAL_TILES = 72
MARGIN = 5
WIDTH = 60
HEIGHT = 60
BOARD_X = 400
BOARD_Y = 400

class GameView(arcade.View):

    def __init__(self, curr_tile, curr_meeple, settings, feature, my_player, game_manager):
        super().__init__()
        # initialize helpful tips
        self.helpful_tips = HelpfulTips()
        # Initialize the flag to track if a popup is active
        self.show_popup_flag = False
        # Variable to hold the popup message
        self.popup_message = ""
        # Initialize the flag to track if a tutorial is active
        self.show_tutorial_flag = False
        # Variable to hold the popup message
        self.tutorial_message = ""
        # Initialize the tutorial
        self.tutorial = Tutorial()
        # Initialize tutorial steps tracker
        self.tutorial_step = 0
        # Check if the user is in tutorial mode
        self.tutorial_active = True
        # Check if tutorial has already been shown
        self.tutorial_seen = False
        # Initialize Background Image
        self.background = arcade.load_texture("images/wood.jpg")
        self.buttons = []
        # your tile text
        self.tile_text = ["", "Your Tile"]
        self.text_for_tile = self.tile_text[0]
        # new player text
        self.new_player = ""
        self.new_player_turn = False
        # inialize sounds
        self.error_sound = arcade.load_sound("images/wrong.mp3")
        self.correct_sound = arcade.load_sound("images/correct.mp3")
        self.drop_sound = arcade.load_sound("images/drop.mp3")
        self.page_sound = arcade.load_sound("images/page.mp3")
        # Initalize sprite lists
        self.player_list = None
        self.scoreboard_list = None
        self.tile_list = None
        self.help_list = None
        self.sound_list = None
        self.music_list = None
        self.ai_list = None
        self.my_player = my_player
        self.game_manager = game_manager
        self.buttons = []
        # your tile text
        self.tile_text = ["", "Your Tile"]
        self.text_for_tile = self.tile_text[0]
        # new player text
        self.new_player = ""
        self.new_player_turn = False
        # Initalize settings
        self.settings = settings
        self.start_tile = tile.start
        self.tile_list = tile.tiles
        self.feat = feature
        self.count = 0
        # Initalize current meeple and current tile position
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        # create done button
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # Placeholder for message box
        self.message_box = None
        # creating horizontal box
        self.h_box = (arcade.gui.
                      UIBoxLayout(vertical=False))
        self.done_button = (arcade.gui.
                           UIFlatButton(text=self.settings.button_text, width=100,style={"font_name":"Carolingia"}))
        self.place_meeple_button = ((arcade.gui.
                           UIFlatButton(text="PLACE MEEPLE", width=150,style={"font_name":"Carolingia"})))
        # add box to manager
        self.h_box.add(self.done_button.with_space_around( top=550, left=50))
        # create event for done
        self.done_button.on_click = self.on_done
        self.place_meeple_button.on_click = self.on_place_meeple
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
        self.place_meeple_button_active = False
        # load the tiles into settings for first round
        if settings.tile_count == 0:
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
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN) + 75
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN) + 125
                sprite_color = arcade.make_transparent_color([0,0,0], 100)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, sprite_color)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

        self.rotating_tile = None


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """

        # Only show tutorial if it hasn't been seen
        if not self.game_manager.tutorial_seen:
            self.show_tutorial_flag = True
            self.tutorial_active = True
            self.tutorial_step = 0
            self.tutorial_message = self.tutorial.get_message(self.tutorial_step)

        if self.game_manager.tutorial_seen:
            # Skip tutorial if already seen
            self.show_tutorial_flag = False
            self.tutorial_active = False

        # Create sprite lists
        self.player_list = arcade.SpriteList()
        self.scoreboard_list = arcade.SpriteList()
        self.tile_list = arcade.SpriteList()
        self.help_list = arcade.SpriteList()
        self.sound_list = arcade.SpriteList()
        self.music_list = arcade.SpriteList()
        self.ai_list = arcade.SpriteList()
        # Meeple sprite
        for meeple in self.settings.get_meeples():
            img = meeple.get_meeple_sprite()
            if len(img) > 32:
                self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER_HORIZONTAL)
            else:
                self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER_VERTICAL)
            self.player_sprite.center_x = meeple.x_coord
            self.player_sprite.center_y = meeple.y_coord
            self.player_list.append(self.player_sprite)
        # Scoreboard Sprite
        scoreboard = ":resources:onscreen_controls/shaded_dark/hamburger.png"
        self.scoreboard_sprite = arcade.Sprite(scoreboard,
                                               SPRITE_SCALING_HELP)
        self.scoreboard_sprite.center_x = 950
        self.scoreboard_sprite.center_y = 515
        self.scoreboard_list.append(self.scoreboard_sprite)

        # Sound
        self.sound = ":resources:onscreen_controls/shaded_dark/sound_on.png"
        self.sound_sprite = arcade.Sprite(self.sound,
                                               SPRITE_SCALING_HELP)
        self.sound_sprite.center_x = 950
        self.sound_sprite.center_y = 420
        self.sound_list.append(self.sound_sprite)

        # Sound
        self.music = ":resources:onscreen_controls/shaded_dark/music_on.png"
        self.music_sprite = arcade.Sprite(self.music,
                                          SPRITE_SCALING_HELP)
        self.music_sprite.center_x = 950
        self.music_sprite.center_y = 330
        self.music_list.append(self.music_sprite)

        # Start Tile Sprite
        tile = self.start_tile.image
        self.tile_sprite = arcade.Sprite(tile,
                                         SPRITE_SCALING_TILE)
        self.tile_sprite.center_x = self.grid_sprites[3][5].center_x
        self.tile_sprite.center_y = self.grid_sprites[3][5].center_y
        self.tile_list.append(self.tile_sprite)

        # if first round add start tile to placed tile
        if len(self.settings.placed_tiles) == 0:

            self.settings.add_placed_tile((99,self.start_tile), SCREEN_WIDTH/2,
                                           SCREEN_HEIGHT/2)

            # creates a matrix matching the grid with a 1 if there is a tile there and 0 if not
            grid_placements = []
            for i in range(len(self.grid_sprites)):
                grid_placements.append([])
                for j in range(len(self.grid_sprites[i])):
                    grid_placements[i].append(0)
            self.settings.feature_container = grid_placements

       # Keep location of placed tile sprites
        for i,item in enumerate(self.settings.placed_tiles[1:],1):
            object = item[0][1]
            tile = object.image
            self.tile_sprite = arcade.Sprite(tile,
                                             SPRITE_SCALING_TILE)
            self.tile_sprite.center_x = item[1]
            self.tile_sprite.center_y = item[2]
            self.tile_sprite.angle = self.settings.get_rotation_click(self.settings.placed_tiles[i][0][0])
            self.tile_list.append(self.tile_sprite)


        # Help Sprite
        help = ":resources:onscreen_controls/shaded_dark/gear.png"
        self.help_sprite = arcade.Sprite(help,
                                         SPRITE_SCALING_HELP)
        self.help_sprite.center_x = 950
        self.help_sprite.center_y = 600
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

        # banner draw
        color = arcade.make_transparent_color([240, 255, 255], 150)
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 50, SCREEN_WIDTH,

                                     125, color)

        # Drawing Sprite Lists
        self.grid_sprite_list.draw()
        self.scoreboard_list.draw()
        self.help_list.draw()
        self.tile_list.draw()
        self.player_list.draw()
        self.sound_list.draw()
        self.music_list.draw()

        # Drawing Button
        self.manager.draw()
        # Drawing Text, from settings round #
        start_x= 50
        start_y = 600
        # Player text from player class
        arcade.draw_text("ROUND " + str(self.settings.get_current_round()) ,
                         start_x,
                         start_y,
                         arcade.color.WHITE,
                         30,
                         font_name="Carolingia")
        # Drawing Text, Need From Player Class
        start_x = 700
        start_y = 50
        # text size based on player name len
        text_size = 20
        if len(self.settings.current_player.name) > 9:
            text_size = 16
        # Player text from player class
        arcade.draw_text(self.settings.get_current_player().name+"'s Turn",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         text_size,
                         font_name="Kenney Future")

        arcade.draw_text("Meeples: "+str(self.settings.current_player.get_meeple_count()),
                         start_x,
                         start_y - 20,
                         arcade.color.BLACK,
                         22,
                         font_name="Kenney Future")

        # Drawing Text, For Tile.
        start_tile_x = 200
        arcade.draw_text(self.text_for_tile,
                         start_tile_x,
                         start_y-20,
                         arcade.color.BLACK,
                         22,
                         font_name="Carolingia")
        if self.settings.ai:
            j = 1
            for i in range(4-self.settings.player_count):
                j += 1 
                arcade.draw_rectangle_outline(self.tile_list[-j].center_x, self.tile_list[-j].center_y, 50, 50,
                                          arcade.color.DEEP_MAGENTA, 3)
            j = 0
        if self.new_player_turn:
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 10, SCREEN_WIDTH,
                                     125, arcade.make_transparent_color([240, 255, 255], 150))

        arcade.draw_text(self.new_player,
                         50,
                         SCREEN_HEIGHT/2,
                         arcade.color.BLACK,
                         40,
                         font_name="Kenney Future")



        # Display the popup if show_popup_flag is True
        if self.show_popup_flag:
            # Dimensions for the popup
            popup_width = 600
            popup_height = 350
            popup_x = SCREEN_WIDTH / 2
            popup_y = SCREEN_HEIGHT / 2

            # Draw red background
            arcade.draw_rectangle_filled(popup_x, popup_y, popup_width, popup_height, arcade.color.KU_CRIMSON)

            # Draw a white border around the background
            arcade.draw_rectangle_outline(popup_x, popup_y, popup_width, popup_height, arcade.color.WHITE, 3)

            # Draw the message text in white
            arcade.draw_text(self.popup_message,
                            # Adjust text position, x-axis
                            popup_x - (popup_width / 2) + 10,
                            # Adjust text position, y-axis
                            popup_y + 120,
                            arcade.color.WHITE,
                            18,
                            # Add padding
                            width=popup_width - 20,
                            align="center")

        # Display the tutorial message if show_tutorial_flag is True
        if self.show_tutorial_flag and not self.tutorial_seen:
            # Dimensions for the popup
            popup_width = 600
            popup_height = 350
            popup_x = SCREEN_WIDTH / 2
            popup_y = SCREEN_HEIGHT / 2

            # Draw purple background for tutorial
            arcade.draw_rectangle_filled(popup_x, popup_y, popup_width, popup_height, arcade.color.PURPLE)

            # Draw a white border around the background
            arcade.draw_rectangle_outline(popup_x, popup_y, popup_width, popup_height, arcade.color.WHITE, 3)

            # Draw the message text in white
            arcade.draw_text(self.tutorial_message,
                            # Adjust text position, x-axis
                            popup_x - (popup_width / 2) + 10,
                            # Adjust text position, y-axis
                            popup_y + 120,
                            arcade.color.WHITE,
                            18,
                            # Add padding
                            width=popup_width - 20,
                            align="center")

            # Add "Continue" button if tutorial is active
            if self.tutorial_active:
                continue_button_x = popup_x - 80
                continue_button_y = popup_y - 100
                button_width = 160
                button_height = 40

                arcade.draw_text("Continue",
                                continue_button_x,
                                continue_button_y,
                                arcade.color.WHITE,
                                20,
                                font_name="Kenney Future")

                '''# Draw "Skip" button 
                skip_button_x = popup_x - 175  
                skip_button_y = continue_button_y
                arcade.draw_text("Skip", 
                                 skip_button_x, 
                                 skip_button_y, 
                                 arcade.color.WHITE, 
                                 20, 
                                 font_name="Kenney Future")'''


            # Highlight specific tutorial areas based on tutorial step
            if self.tutorial_active:
                if self.tutorial_step == 0:
                    pass
                elif self.tutorial_step == 1:
                    # Highlight help guide area, done
                    arcade.draw_rectangle_outline(950, 600, 80, 80, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 2:
                    # Highlight scoreboard area, done
                    arcade.draw_rectangle_outline(950, 515, 80, 80, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 3:
                    # Highlight sound and music area, done
                    arcade.draw_rectangle_outline(950, 370, 80, 175, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 4:
                    # Highlight pick tile area, done
                    arcade.draw_rectangle_outline(270, 60, 180, 90, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 5:
                    # Highlight board area, done
                    arcade.draw_rectangle_outline(440, 365, 800, 520, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 6:
                    # Highlight done area, done
                    arcade.draw_rectangle_outline(525, 50, 140, 80, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 7:
                    # Highlight meeple area, done
                    arcade.draw_rectangle_outline(525, 50, 140, 80, arcade.color.YELLOW, 3)
                elif self.tutorial_step == 8:
                    # Highlight place meeple area, done
                    arcade.draw_rectangle_outline(585, 50, 140, 80, arcade.color.YELLOW, 3)
            pass

    def on_update(self, delta_time):
        """ All the logic to move"""
        # change button from start to done
        if self.done_button.text != self.settings.button_text:
            self.done_button.text = self.settings.button_text

        # if tile moved update with new location
        if self.curr_tile.get_moved():
            self.tile_sprite.center_x = self.curr_tile.get_x()
            self.tile_sprite.center_y = self.curr_tile.get_y()

        # change you tile text
        if self.settings.button_text != "START":
            if self.tile_sprite.center_x  == 250 and self.tile_sprite.center_y == 75:
                self.text_for_tile = self.tile_text[1]
            else:
                self.text_for_tile = self.tile_text[0]

        if self.settings.ai:
            self.count += 1

        if self.new_player_turn or self.settings.ai:
            self.new_player = self.settings.current_player.name +" It's Your Turn"
            self.count += 1
        else:
            self.new_player = ""

        if self.settings.sound_on:
            self.sound_sprite.image = ":resources:onscreen_controls/shaded_dark/sound_off.png"


        if self.count != 0 and self.count % 50 == 0 and not self.settings.ai:
            self.new_player_turn = False
            self.count = 0

        if self.count != 0 and self.count == 100  and self.settings.ai:
            self.count = 0
            self.settings.ai = False


    def on_done(self, event, ai=False):
        """ If the user presses the button, the logic will
        be checked, the round will increment if player 4 is
        current player, otherwise it will increment next
        player
        """
        # if button is start then display the new button
        if self.settings.button_text == "START":
            # change tile to next tile in list,
            self.curr_tile.set_moved(False)
            self.curr_tile.set_y(75)
            self.curr_tile.set_x(250)
            tile = self.settings.tiles[self.settings.tile_count][1].image
            self.tile_sprite = arcade.Sprite(tile,
                                             SPRITE_SCALING_TILE)
            self.tile_sprite.center_x = self.curr_tile.get_x()
            self.tile_sprite.center_y = self.curr_tile.get_y()
            self.tile_list.append(self.tile_sprite)
            # add placed tile to placed_tile list in settings
            self.settings.add_placed_tile(self.settings.tiles[self.settings.tile_count],
                                          self.tile_sprite.center_x, self.tile_sprite.center_y)
            self.settings.increment_tile_count()
            self.settings.set_button_text("DONE")
            self.setup()
            self.new_player_turn = True

        else:
            neighbors = [
                # up
                (self.settings.previous_coor_x + 1, self.settings.previous_coor_y),
                # down
                (self.settings.previous_coor_x - 1, self.settings.previous_coor_y),
                # left
                (self.settings.previous_coor_x, self.settings.previous_coor_y - 1),
                # right
                (self.settings.previous_coor_x, self.settings.previous_coor_y + 1)
            ]
            done_valid = self.validate_placement(neighbors, self.settings.placed_tiles[-1][0][1])
            if done_valid:
                if self.place_meeple_button_active and self.settings.done_pressed:
                    if not self.settings.meeple_screen:
                        self.delete_place_meeple_button()
                    self.place_meeple_button_active = False
                    self.settings.done_pressed = False
                    self.settings.meeple_screen = False
                    self.feat.check_feature_completed(self.settings)
                    # create correct sound
                    if self.settings.sound_on:
                        arcade.play_sound(self.correct_sound, 1, 1, False, .5)
                    # reset meeple placement variables
                    self.settings.set_meeple_placed_current_round(False)
                    # set coordinates back to -1 for next tile
                    self.settings.previous_coor_x = -1
                    self.settings.previous_coor_y = -1
                    # get player count for indexing
                    # if the last player to go, increment current round
                    if self.settings.get_current_player() == self.settings.current_players[3]:
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
                                self.new_player_turn = True
                            else:
                                # increment to next player in list
                                current_player = self.settings.current_players[player + 1]
                                self.settings.set_current_player(current_player)
                                self.new_player_turn = True
                                break

                    # update_tiles
                    new_list = []
                    # save sprite locations
                    self.curr_tile.set_x(self.tile_sprite.center_x)
                    self.curr_tile.set_y(self.tile_sprite.center_y)
                    # update the placed tiles, with new coordinates
                    for item in self.settings.placed_tiles:
                        if item == self.settings.placed_tiles[-1]:
                            new_list.append((item[0], self.curr_tile.get_x(), self.curr_tile.get_y()))
                        else:
                            new_list.append(item)
                    self.settings.placed_tiles = new_list

                    # change tile to next tile in list,
                    self.curr_tile.set_moved(False)
                    self.curr_tile.set_y(75)
                    self.curr_tile.set_x(250)
                    tile = self.settings.tiles[self.settings.tile_count][1].image
                    self.tile_sprite = arcade.Sprite(tile,
                                                     SPRITE_SCALING_TILE)
                    self.tile_sprite.center_x = self.curr_tile.get_x()
                    self.tile_sprite.center_y = self.curr_tile.get_y()
                    self.tile_list.append(self.tile_sprite)

                    # add placed tile to placed_tile list in settings
                    self.settings.add_placed_tile(self.settings.tiles[self.settings.tile_count],
                                                  self.tile_sprite.center_x, self.tile_sprite.center_y)
                    self.settings.increment_tile_count()
                    self.on_new_tile()

                    # increment turns -- update the board
                    if current_player.is_ai():
                        self.on_ai_turn(current_player)

                else:
                    if self.settings.current_player.ai:
                        self.feat.check_feature_completed(self.settings)
                        # create correct sound
                        if self.settings.sound_on:
                            arcade.play_sound(self.correct_sound, 1, 1, False, .5)
                        #play ai meeple
                        index = random.randint(0, 4)
                        meeple_coor_x = self.grid_sprites[self.settings.previous_coor_x][self.settings.previous_coor_y].center_x
                        meeple_coor_y = self.grid_sprites[self.settings.previous_coor_x][self.settings.previous_coor_y].center_y
                        self.ai_place_meeple(index, self.settings.current_player, meeple_coor_x, meeple_coor_y)
                        # reset meeple placement variables
                        self.settings.set_meeple_placed_current_round(False)
                        # set coordinates back to -1 for next tile
                        self.settings.previous_coor_x = -1
                        self.settings.previous_coor_y = -1
                        # get player count for indexing
                        # count = self.settings.get_player_count() - 1
                        # if the last player to go, increment current round
                        if self.settings.get_current_player() == self.settings.current_players[3]:
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
                                    self.new_player_turn = True
                                else:
                                    # increment to next player in list
                                    current_player = self.settings.current_players[player + 1]
                                    self.settings.set_current_player(current_player)
                                    self.new_player_turn = True
                                    break

                        # update_tiles
                        new_list = []
                        # save sprite locations
                        self.curr_tile.set_x(self.tile_sprite.center_x)
                        self.curr_tile.set_y(self.tile_sprite.center_y)
                        # update the placed tiles, with new coordinates
                        for item in self.settings.placed_tiles:
                            if item == self.settings.placed_tiles[-1]:
                                new_list.append((item[0], self.curr_tile.get_x(), self.curr_tile.get_y()))
                            else:
                                new_list.append(item)
                        self.settings.placed_tiles = new_list

                        # change tile to next tile in list,
                        self.curr_tile.set_moved(False)
                        self.curr_tile.set_y(75)
                        self.curr_tile.set_x(250)
                        tile = self.settings.tiles[self.settings.tile_count][1].image
                        self.tile_sprite = arcade.Sprite(tile,
                                                         SPRITE_SCALING_TILE)
                        self.tile_sprite.center_x = self.curr_tile.get_x()
                        self.tile_sprite.center_y = self.curr_tile.get_y()
                        self.tile_list.append(self.tile_sprite)
                        # add placed tile to placed_tile list in settings
                        self.settings.add_placed_tile(self.settings.tiles[self.settings.tile_count],
                                                      self.tile_sprite.center_x, self.tile_sprite.center_y)
                        self.settings.increment_tile_count()
                        self.on_new_tile()
                        self.settings.prev_ai = False

                         # increment turns -- update the board
                        if current_player.is_ai():
                            self.on_ai_turn(current_player)
                            self.setup()
                    else:
                        self.settings.done_pressed = True
                        self.add_place_meeple_button()
            else:
                if self.settings.sound_on:
                    self.sound = self.error_sound.play()
                # set error message
                message = self.helpful_tips.get_message()
                # show error message
                self.show_popup(message)


    def show_popup(self, message):
        '''
        Show a popup error message, dismiss popup by clicking anywhere.
        '''
        # Check if flag is active
        if not self.show_popup_flag:
            # Set the message to be displayed
            self.popup_message = message
            # Mark popup as active
            self.show_popup_flag = True

    def show_tutorial_window(self):
        '''
        Display a tutorial popup for new players. Click "Continue" to proceed to the next step.
        '''
        # Check if flad is active
        if self.tutorial_active:
            # Fetch the tutorial message based on the current step
            self.tutorial_message = self.tutorial.get_message(self.tutorial_step)

    def delete_place_meeple_button(self):
        """Remove the Place Meeple button from the layout."""
        if self.place_meeple_button_active:
            self.h_box.remove(self.h_box.children[-1])
            self.place_meeple_button_active = False

    def add_place_meeple_button(self):
        """Add the Place Meeple button back to the layout."""
        if not self.place_meeple_button_active:
            # Re-add the button to the layout
            self.h_box.add(self.place_meeple_button.with_space_around(top=550, left=10))
            self.place_meeple_button_active = True

    def on_place_meeple(self, event):
        if len(self.settings.get_placed_tiles()) > 1 and self.settings.get_meeple_placed_current_round() == False:
            # create new list to update placed sprites
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
            # change view to help screen
            new_view = meeple_placement_view.MeeplePlacementView(self.curr_tile, self.curr_meeple, self.settings, self.tile_sprite, self.feat, self.my_player, self.game_manager)
            self.window.show_view(new_view)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        # Allow Sprite to Move With Mouse
        try:
            if self.dragging_sprite:
                self.dragging_sprite.center_x += delta_x
                self.dragging_sprite.center_y += delta_y

        except AttributeError:
            pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
         # Check if the tutorial is active
        if self.show_tutorial_flag and self.tutorial_active and not self.tutorial_seen:
            # Coordinates for the "Continue" button
            popup_x = SCREEN_WIDTH / 2
            popup_y = SCREEN_HEIGHT / 2
            continue_button_x = popup_x - 80
            continue_button_y = popup_y - 120
            button_width = 160
            button_height = 80

            # Check if the user clicked within the "Continue" button area
            if (continue_button_x <= x <= continue_button_x + button_width
                    and continue_button_y <= y <= continue_button_y + button_height):
                # Proceed to the next tutorial step
                self.tutorial_step += 1
                if self.tutorial_step >= self.tutorial.get_total_steps():
                    # End the tutorial
                    self.show_tutorial_flag = False
                    self.tutorial_active = False
                    # Mark tutorial as seen
                    self.game_manager.tutorial_seen = True
                else:
                    # Show next tutorial step
                    self.show_tutorial_window()
                return
        # If clicked outside the "Continue" button, skip the tutorial
        else:
            # End the tutorial and mark it as seen
            self.show_tutorial_flag = False
            self.tutorial_active = False
            self.game_manager.tutorial_seen = True


        # If Left Button on Mouse Clicked on Tile
        if button == arcade.MOUSE_BUTTON_LEFT:
            clicked_tile = arcade.get_sprites_at_point((x, y),
                                                          self.tile_list)

            new_meeple = arcade.get_sprites_at_point((x, y),
                                                     self.player_list)

            # Allow dragging to be possible
            if clicked_tile:
                # if current tile is clicked and is the newest tile, dragging is possible
                if (clicked_tile[0] == self.tile_list[-1] and
                        clicked_tile[0] != self.tile_list[0] and
                        not self.settings.meeple_placed_current_round):
                    self.dragging_sprite = clicked_tile[0]

            # Check if the popup is visible, if so dismiss it
            if self.show_popup_flag:
                # Dismiss the popup
                self.show_popup_flag = False

            # Check if the tutorial popup is visible, if so dismiss it
            if self.show_tutorial_flag:
                # Dismiss the popup
                self.show_tutorial_flag = False

        if button == arcade.MOUSE_BUTTON_RIGHT:
            clicked_tile = arcade.get_sprites_at_point((x, y),
                                                       self.tile_list)
            if clicked_tile:
                # if current tile is clicked and is the newest tile, rotating is possible
                if (clicked_tile[0] == self.tile_list[-1] and
                        clicked_tile[0] != self.tile_list[0]):
                    self.rotating_tile = clicked_tile[0]

    def on_mouse_release(self, x, y, button, key_modifiers):
        """ Called when a user releases a mouse button.  """

        # If Left Mouse is Released stop dragging
        if button == arcade.MOUSE_BUTTON_LEFT:
            try:
                # if new sprite is on tile already placed then move to start
                if self.dragging_sprite.collides_with_list(self.tile_list):
                    self.dragging_sprite.center_x = 250
                    self.dragging_sprite.center_y = 75
                    if self.settings.sound_on:
                        self.wrong_place = self.error_sound.play()

            except AttributeError:
                pass
            self.dragging_sprite = None
            self.dragging_meeple = None


            # if tile in matrix set current position to moved, by passing first tile
            if self.settings.placed_tiles[-1][0][1] != self.settings.placed_tiles[0][0][1]:
                for row in self.settings.feature_container:
                    if self.settings.placed_tiles[-1][0][1] in row:
                        self.settings.feature_container[self.settings.previous_coor_x][self.settings.previous_coor_y] = 0
                        self.settings.previous_coor_x = -1
                        self.settings.previous_coor_y = -1
                        break

            # Snaps tiles into grid
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    # If the tile being dragged overlaps a certain amount with a
                    # square in the grid it is snapped into place
                    if (self.grid_sprites[i][j].collides_with_point
                        ([self.tile_sprite.center_x, self.tile_sprite.center_y])):
                        self.tile_sprite.center_x = self.grid_sprites[i][j].center_x
                        self.tile_sprite.center_y = self.grid_sprites[i][j].center_y
                        if self.settings.sound_on:
                            self.sound_drop = self.drop_sound.play()
                        # update postion in matrix for start tile
                        if self.settings.placed_tiles[-1][0][1] == self.settings.placed_tiles[0][0][1]:
                            self.settings.feature_container[i][j] = self.settings.placed_tiles[-1][0][1]
                            self.feat.inital_location(self.settings.feature_container)
                        # update position of new tile into the matrix, with coordiantes
                        else:
                            if self.settings.previous_coor_x == -1:
                                self.settings.feature_container[i][j] = self.settings.placed_tiles[-1][0][1]
                                self.settings.previous_coor_x = i
                                self.settings.previous_coor_y = j

            # If scoreboard was clicked then released
            clicked_scoreboard = arcade.get_sprites_at_point((x, y),
                                                             self.scoreboard_list)
            # If help was clicked then released
            clicked_help = arcade.get_sprites_at_point((x, y),
                                                       self.help_list)

            clicked_sound = arcade.get_sprites_at_point((x, y),
                                                             self.sound_list)

            clicked_music = arcade.get_sprites_at_point((x, y),
                                                        self.music_list)

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
                # sound
                if self.settings.sound_on:
                    self.sound_page = self.page_sound.play()
                # change view to help screen
                help = help_view.HelpView(self.curr_tile, self.curr_meeple, self.settings, self.feat, self.my_player, self.game_manager)
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
                self.settings.placed_tiles = new_list
                # sound
                if self.settings.sound_on:
                    self.sound_page = self.page_sound.play()
                if self.settings.sound_on:
                    self.sound_page = self.page_sound.play()
                # change view to scoreboard
                scoreboard = scoreboard_view.ScoreboardView(self.curr_tile, self.curr_meeple, self.settings, self.feat, self.my_player, self.game_manager)
                scoreboard.setup()
                self.window.show_view(scoreboard)

            if clicked_sound:
                if self.settings.sound_on:
                     self.settings.sound_on = False
                else:
                    self.settings.sound_on = True

            if clicked_music:
                if self.settings.music_on:
                     self.settings.music_on = False
                     self.my_player.pause()

                else:
                    self.settings.music_on = True
                    self.my_player.play()

        if button == arcade.MOUSE_BUTTON_RIGHT:
            # If the right mouse button is clicked then unclicked, rotate tile
            if self.rotating_tile:
                self.rotating_tile.angle = 90 + self.rotating_tile.angle
                self.settings.increment_rotation(self.settings.placed_tiles[-1][0][0])
                self.settings.placed_tiles[-1][0][1].rotate_tile()
                if self.settings.sound_on:
                    self.sound_drop = self.drop_sound.play()


    def on_new_tile(self):
        can_place = False
        validation_tile = self.settings.placed_tiles[-1][0][1].copy()
        for i in range(len(self.settings.feature_container)):
            for j in range(len(self.settings.feature_container[i])):
                for k in range (4):
                    if self.settings.feature_container[i][j] == 0:
                        # validates the placement of the current tile at spot (i,j) in the grid
                        neighbors = [
                            #up
                            (i+1, j),
                            #down
                            (i-1, j),
                            #left
                            (i, j-1),
                            #right
                            (i, j+1)
                        ]
                        if self.validate_placement(neighbors, validation_tile, False):
                            can_place = True
                        #rotates the tile and repeats validation
                        validation_tile.rotate_tile()
        if can_place == False:
            # if there are more tiles in tile list
            if len(self.settings.placed_tiles) <= len(self.settings.tiles):
                self.tile_sprite.kill()
                self.curr_tile.set_moved(False)
                self.curr_tile.set_y(75)
                self.curr_tile.set_x(200)
                tile = self.settings.tiles[self.settings.tile_count][1].image
                self.tile_sprite = arcade.Sprite(tile,
                                                 SPRITE_SCALING_TILE)
                self.tile_sprite.center_x = self.curr_tile.get_x()
                self.tile_sprite.center_y = self.curr_tile.get_y()
                self.tile_list.append(self.tile_sprite)
                self.settings.add_placed_tile(self.settings.tiles[self.settings.tile_count],
                                              self.tile_sprite.center_x, self.tile_sprite.center_y)
                self.settings.increment_tile_count()
                #if AI player, and cannot play a tile, ends the game, triggers scoring and end screen
                if self.settings.prev_ai:
                    # end of game scoring for meeples
                    meeple_list = self.settings.get_meeples()
                    for meeple in self.settings.get_meeples():
                        meeple.end_of_game_scoring(self.settings, meeple_list)
                    endview = end_view.EndView(self.settings)
                    self.window.show_view(endview)
                self.on_new_tile()
            else:
                # end of game scoring for meeples
                meeple_list = self.settings.get_meeples()
                for meeple in self.settings.get_meeples():
                    meeple.end_of_game_scoring(self.settings, meeple_list)
                endview = end_view.EndView(self.settings)
                self.window.show_view(endview)

    def validate_placement(self, neighbors, curr_tile, is_placing=True):
        """This function validates that a placment can be placed, if valid
        it sends the tiles that are neighboring to feature_placemnts, returns bool"""
        # boolean if you can place tile
        done_valid = False
        # get neighbor coordinates
        right_neighbor = neighbors[3]
        left_neighbor = neighbors[2]
        top_neighbor = neighbors[0]
        bottom_neighbor = neighbors[1]
        has_neighbor = False
        check_tile_features = []
        # check if there is a neighboring tile
        for x, y in neighbors:
            # check if the coordinate is within the bounds of the matrix
            if 0 <= x < ROW_COUNT and 0 <= y < COLUMN_COUNT:
                if self.settings.feature_container[x][y] != 0:
                    if (x, y) == right_neighbor:
                        neighbor_x = right_neighbor[0]
                        neighbor_y = right_neighbor[1]
                        side = "right"
                    elif (x, y) == left_neighbor:
                        neighbor_x = left_neighbor[0]
                        neighbor_y = left_neighbor[1]
                        side = "left"
                    elif (x, y) == top_neighbor:
                        neighbor_x = top_neighbor[0]
                        neighbor_y = top_neighbor[1]
                        side = "top"
                    elif (x, y) == bottom_neighbor:
                        neighbor_x = bottom_neighbor[0]
                        neighbor_y = bottom_neighbor[1]
                        side = "bottom"
                    has_neighbor = True
                    check_tile_features.append((neighbor_x, neighbor_y, side))
        if check_tile_features != []:
            # check if neighboring tile has the same feature where it connects
            count_valid = 0
            for tile in check_tile_features:
                if tile[2] == "left":
                    if (self.settings.feature_container[tile[0]][tile[1]].right ==
                            curr_tile.left):
                        count_valid += 1

                if tile[2] == "right":
                    if (self.settings.feature_container[tile[0]][tile[1]].left ==
                            curr_tile.right):
                        count_valid += 1

                if tile[2] == "top":
                    if (self.settings.feature_container[tile[0]][tile[1]].bottom ==
                            curr_tile.top):
                        count_valid += 1

                if tile[2] == "bottom":
                    if (self.settings.feature_container[tile[0]][tile[1]].top ==
                            curr_tile.bottom):
                        count_valid += 1
            if count_valid == len(check_tile_features):
                done_valid = True
                self.rotating_tile = None
                if is_placing:
                    self.feat.add_tile(self.settings.previous_coor_x,
                                       self.settings.previous_coor_y,
                                       self.settings.placed_tiles[-1][0][1])

                    if check_tile_features != []:
                        for tile in check_tile_features:
                            if tile[2] == "left":
                                self.feat.add_location(tile[0],
                                                       tile[1],
                                                       self.settings.previous_coor_x,
                                                       self.settings.previous_coor_y,
                                                       "right",
                                                       "left")

                            if tile[2] == "right":
                                self.feat.add_location(tile[0],
                                                       tile[1],
                                                       self.settings.previous_coor_x,
                                                       self.settings.previous_coor_y,
                                                       "left",
                                                       "right")

                            if tile[2] == "top":
                                self.feat.add_location(tile[0],
                                                       tile[1],
                                                       self.settings.previous_coor_x,
                                                       self.settings.previous_coor_y,
                                                       "bottom",
                                                       "top")

                            if tile[2] == "bottom":
                                self.feat.add_location(tile[0],
                                                       tile[1],
                                                       self.settings.previous_coor_x,
                                                       self.settings.previous_coor_y,
                                                       "top",
                                                       "bottom")


        return done_valid

    def on_ai_turn(self, player):
        """ Randomly chooses an available space on the board to place their tile"""
        can_place = False
        while can_place == False:
            rand_x = random.randint(0, 6)
            rand_y = random.randint(0, 10)
            if self.settings.feature_container[rand_x][rand_y] == 0:
                neighbors = [(rand_x + 1, rand_y), (rand_x - 1, rand_y), (rand_x, rand_y - 1), (rand_x, rand_y + 1)]
                for k in range(4):
                    if self.validate_placement(neighbors, self.settings.placed_tiles[-1][0][1]):
                        can_place = True
                        self.tile_list[-1].center_x = self.grid_sprites[rand_x][rand_y].center_x
                        self.tile_list[-1].center_y = self.grid_sprites[rand_x][rand_y].center_y
                        self.settings.feature_container[rand_x][rand_y] = self.settings.placed_tiles[-1][0][1]
                        self.settings.previous_coor_x = rand_x
                        self.settings.previous_coor_y = rand_y
                        self.settings.ai = True
                        self.settings.prev_ai = True
                        self.ai_list.append(self.tile_list[-1])
                        self.feat.add_tile(rand_x, rand_y, self.settings.placed_tiles[-1][0][1])
                        self.curr_tile.set_moved(False)
                        self.on_done(0)
                        return
                    else:
                        self.settings.placed_tiles[-1][0][1].rotate_tile()
                        self.tile_list[-1].angle = self.tile_list[-1].angle + 90
                        self.settings.increment_rotation(self.settings.placed_tiles[-1][0][0])
                    self.settings.reset_rotation(self.settings.placed_tiles[-1][0][1])

    def ai_place_meeple(self, index, player, tile_x, tile_y):
        """This randomly places a meeple for the ai if it can, it will"""
        results = player.use_meeple(self.settings.placed_tiles[-1][0][1], index, self.settings)
        valid_placement = results[0]
        current_meeple = results[1]
        meeple_coord_mods = [0,0]
        if index == 0:
            meeple_coord_mods = [0, 15]
        elif index == 1:
            meeple_coord_mods = [-15, 0]
        elif index == 2:
            meeple_coord_mods = [15, 0]
        elif index == 3:
            meeple_coord_mods = [0, 0]
        elif index == 4:
            meeple_coord_mods = [0, -15]
        if valid_placement:
            self.settings.set_meeple_placed_current_round(True)
            # set coordinates for placed Meeple
            tile_x_coord = tile_x
            tile_y_coord = tile_y
            new_meeple_coord_x = tile_x_coord + meeple_coord_mods[0]
            new_meeple_coord_y = tile_y_coord + meeple_coord_mods[1]
            current_meeple.set_x_coord(new_meeple_coord_x)
            current_meeple.set_y_coord(new_meeple_coord_y)
            # update sprite
            self.settings.add_meeple(current_meeple)