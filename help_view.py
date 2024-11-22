import arcade
import arcade.color
import arcade.color
import arcade.gui
import game_view
from arcade.gui import UIFlatButton, UIBoxLayout
from PIL import Image

#import matplotlib.pyplot as plt
#import cv2

# Global Var: Screen Size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

#TODO: add correct images for each tab content --> for examples, maybe just play the game a few times and take screenshots to use in content

#TODO: change background to grass, or something more carcassonne-y --> realistic looking background

#TODO: make keywords in content for each tab as a link that has a pop-up for 
#      visual examples of tiles? If too challenging, just have static examples 
#      at bottom of window


class HelpView(arcade.View):
    """ View to show help content """

    def __init__(self, curr_tile, curr_meeple, settings, feat, my_player, game_manager):
        super().__init__()
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        self.settings = settings
        self.feat = feat
        self.my_player = my_player
        self.game_manager = game_manager
        self.content = {
            "How to Win": "The goal of Carcassonne is to score the most points by creating completed cities, roads, monasteries, and fields with tiles and meeples (player pieces). Points are awarded throughout the game and at the end based on the size and completion of each feature.",
            "Main Features": "Tiles: Each tile may contain features like roads, cities, and monasteries.\n\nMeeples: Used to claim a feature and earn points as the tiles surrounding your meeple are placed.\n\nScoreboard: Used to keep track of each player’s score.",
            "Gameplay Overview": "1.) Draw a Tile: The current player draws a tile.\n\n2.) Place the Tile: Place the tile adjacent to an existing tile, matching the edges so that roads connect to roads, cities to cities, or so the farmland your meeple has claimed grows.\n\n3.) Place a Meeple: You may place a meeple on a feature of any tile if that feature is unclaimed.\n\n4.) Score Features: Completed features are scored immediately, and meeples on those features are returned to the player. You will see your score increase as your features are complete.",
            "Feature Scoring": "Cities: Score 2 points per tile when completed. If the city tile has a shield, you score an extra 2 points per sheid tile. For example: if you have 4 tiles in your completed city, you will earn 8 points. If your completed city has 4 tiles, and one of the tiles has a shield, you earn 10 points total. If your city is incomplete at the end of the game, you score 1 point per connected city tile.\n\nRoads: Score 1 point per tile when completed. Incomplete roads at the end of the game are also 1 point per connected road tile.\n\nMonasteries: Score 9 points when the monastery tile is completely surrounded by 8 tiles. If your monastery is incomplete by the end of the same, you score 1 point per adjacent tile.",
            "Completing Features": "A feature is completed when it has no open edges...\n\nCities: Enclosed by walls with no gaps.\n\nRoads: Ends meet another road, a city, or loop back on itself.\n\nMonasteries: Surrounded by 8 tiles. Scoring occurs immediately after a monastery is complete, and any meeples on the completed feature are returned to the player.",
            "End of Game": "The game ends when all tiles have been placed. Players then score any remaining incomplete features:\n\nIncomplete Cities & Roads: Score 1 point per tile.\n\nMonasteries: Score 1 point per adjacent tile.\n\nThe player with the most points wins the game.",
            "Tips and Strategy": "Balance Your Meeples: Use meeples wisely since you have a limited number, it is best to plan ahead and keep track of where your opponents have placed their meeples.\n\nBlock Opponents: Place tiles that make it hard for opponents to complete high-scoring features."
        }
        self.image_dict = {
            # Good
            "How to Win": "images/carcassonne_logo.jpg",
            # Good
            "Main Features": "images/features.png", 
            # Good
            "Gameplay Overview": "images/gameplay_overview.png",
            # Good
            "Feature Scoring": "images/completed_city_with_meeple.png",
            # Good
            "Completing Features": "images/completing_features.png",
            # Good
            "End of Game": "images/end_of_game.png",
            # Good
            "Tips and Strategy": "images/meeples.png",
        }
        self.current_content_key = list(self.content.keys())[0]
        self.ui_manager = arcade.gui.UIManager()
        self.button_list = []

    def setup(self):
        """ Set up the UI elements for the help view. """
        #Navbar layout
        navbar_layout = UIBoxLayout(vertical=False)
        
        # Button dimensions
        button_width = 142.85
        button_height = 80

        '''
        # Calculate the number of rows based on total button count and buttons per row
        total_button_count = len(self.content)
        rows = (total_button_count // max_buttons_per_row) + (total_button_count % max_buttons_per_row > 0)
        '''
        
        # Button Styling
        button_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 14,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": arcade.color.WHITE,
            "bg_color": arcade.color.BLACK,

            # used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            "border_color_pressed": arcade.color.BLACK,
            "font_color_pressed": arcade.color.WHITE,
        }
        

        # Create buttons for each content key and place them in rows
        for index, key in enumerate(self.content.keys()):
            button = arcade.gui.UIFlatButton(
                text=key,
                width=button_width,
                height=button_height, 
                style=button_style
            )
            button.on_click = self.create_button_callback(key)
            navbar_layout.add(button)
            
            self.ui_manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="left",
                    anchor_y="top",
                    child=navbar_layout,  
                    align_x=0,
                    align_y=0
                )
            )

    def create_button_callback(self, key):
        """ Create a callback function for each button to update displayed content. """
        def callback(event):
            self.current_content_key = key
        return callback

    def on_show_view(self):
        """ This is run once when we switch to this view. """
        self.background = arcade.load_texture("images/nature_background_2.png")
        #arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.setup()  # Set up buttons only once when view is shown
        self.ui_manager.enable()

    def on_draw(self):
        """ Draw this view. """
        self.clear()
        # Draw the background image
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                    SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Title for Help View - Use the current tab's key as the title
        arcade.draw_text(self.current_content_key,
                        self.window.width / 2 + 30,
                        self.window.height - 150,
                        arcade.color.BLACK,
                        font_size=35,
                        anchor_x="center",
                        font_name="Kenney Future")

        # Display the content for each help type
        content_text = self.content[self.current_content_key]
        arcade.draw_text(content_text,
                        100, SCREEN_HEIGHT / 2,
                        arcade.color.BLACK,
                        font_size=14,
                        anchor_x="left",
                        anchor_y="center", font_name=("calibri", "arial"),
                        multiline=True, width=650)
        
        # Display image for each help type
        content_image = arcade.load_texture(self.image_dict[self.current_content_key])
        arcade.draw_texture_rectangle(
            500, 100,
            content_image.width,
            content_image.height,
            content_image
        )

        # Draw all UI elements managed by the UI Manager (buttons)
        self.ui_manager.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        """ Handle clicks outside the buttons to close the help view. """
        # Check if the click was outside the navbar area
        if y < SCREEN_HEIGHT - 80:
            # Close help view and open game view
            self.curr_tile.set_moved(False)
            self.curr_meeple.set_moved(False)
            game = game_view.GameView(self.curr_tile, self.curr_meeple, self.settings, self.feat, self.my_player, self.game_manager)
            game.setup()
            self.window.show_view(game)

    def on_hide_view(self):
        """ Disable UI elements when hiding this view. """
        self.ui_manager.disable()
