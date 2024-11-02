""" This file is the main file to play the game carcassonne."""

import arcade
import arcade.gui
import open_view
# Global Var: Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Global Var: Window Title
SCREEN_TITLE = "Carcassonne"


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = open_view.OpenView()
    window.show_view(start_view)
    arcade.run()

main()