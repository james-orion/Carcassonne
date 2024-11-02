# pass in tile itself instead of just tile sprite
class MeeplePlacementView(arcade.View):
    def __init__(self, curr_tile, curr_meeple, settings, tile):
        super().__init__()
        self.player = settings.current_player
        self.curr_tile = curr_tile
        self.curr_meeple = curr_meeple
        self.settings = settings
        self.tile_image = tile
        self.background = arcade.load_texture("images/wood.jpg")
        self.has_choosen = False
        self.valid_placement = True
        self.choice_coordinates = None

        # create confirm and cancel buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.h_box = (arcade.gui.UIBoxLayout(vertical=False))
        cancel_button = (arcade.gui.UIFlatButton(text="CANCEL", width=100))
        self.h_box.add(cancel_button.with_space_around(right=100))
        cancel_button.on_click = self.on_cancel
        confirm_button = (arcade.gui.UIFlatButton(text="CONFIRM", width=110))
        self.h_box.add(confirm_button.with_space_around(left=100))
        confirm_button.on_click = self.on_confirm
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center", anchor_y="center",align_y=-180, child=self.h_box, style=None))

    def on_show_view(self): # necessary?
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        box_width = int((SCREEN_WIDTH) * 0.75)
        box_height = int((SCREEN_HEIGHT) * 0.75)
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, box_width, box_height, arcade.color.STEEL_BLUE)
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT // 2, 275, 275, arcade.color.WHITE) # TODO replace with tile photo
        self.tile_image.scale = 2.5
        self.tile_image.center_x = SCREEN_WIDTH // 2 - 125
        self.tile_image.center_y = SCREEN_HEIGHT // 2
        self.tile_image.draw()
        arcade.draw_text("Meeple Location:", self.window.width / 2 + 150, self.window.height - 150, arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("Use Keys 1 - 5 to Choose", self.window.width / 2 + 150, self.window.height - 175, arcade.color.WHITE, font_size=10, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("1. TOP", self.window.width / 2 + 150, self.window.height - 225, arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("2. LEFT SIDE", self.window.width / 2 + 150, self.window.height - 275, arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("3. RIGHT SIDE", self.window.width / 2 + 150, self.window.height - 325, arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("4. CENTER", self.window.width / 2 + 150, self.window.height - 375, arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("5. BOTTOM", self.window.width / 2 + 150, self.window.height - 425, arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        if self.has_choosen:
            arcade.draw_circle_filled(self.choice_coordinates[0], self.choice_coordinates[1], 20, arcade.color.RED) # TODO replace with user's color
        self.manager.draw()
        if self.valid_placement == False:
            arcade.draw_text("Meeple Placement is Invlaid, Please Try Again",  self.window.width // 2, self.window.height // 2 + 185, arcade.color.WHITE, font_size=12, anchor_x="center", font_name="Kenney Future")


    def on_key_press(self, key, modifiers):
        if key in (arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3, arcade.key.KEY_4, arcade.key.KEY_5):
            placement_choice = key - arcade.key.KEY_1
            self.has_choosen = True
            if placement_choice == 0:
                self.choice_coordinates = [SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT // 2 + 100]
            elif placement_choice == 1:
                self.choice_coordinates = [SCREEN_WIDTH // 2 - 225, SCREEN_HEIGHT // 2]
            elif placement_choice == 2:
                self.choice_coordinates = [SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT // 2]
            elif placement_choice == 3:
                self.choice_coordinates = [SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT // 2]
            elif placement_choice == 4:
                self.choice_coordinates = [SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT // 2 - 100]

    def on_cancel(self, event):
        # return to GameView as it was previously
        self.curr_tile.set_moved(False)
        self.curr_meeple.set_moved(False)
        # switch to game view
        game_view = GameView(self.curr_tile, self.curr_meeple, self.settings)
        game_view.setup()
        self.window.show_view(game_view)

    def on_confirm(self, event):
        # check whether Meeple placement is valid
        # if placement is valid, place Meeple and return to GameView
        # if invalid, prompt user to replace Meeple
        '''
        if self.player.use_meeple(___):
            place meeple
            return to game
        else:
            self.valid_placement = False
        '''
        pass
