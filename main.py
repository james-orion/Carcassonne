""" This file is the main file to play the game carcassonne."""

import arcade
import arcade.gui
import open_view


# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
# Global Var: Window Title
SCREEN_TITLE = "Carcassonne"


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    civ_music = arcade.load_sound("images/civ_open.mp3", streaming=True)
    my_player= civ_music.play(.2, -1, True)
    start_view = open_view.OpenView(my_player)
    window.show_view(start_view)
    arcade.run()

main()