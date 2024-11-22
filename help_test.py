import arcade

class Tab:
    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = False

    def draw(self):
        """ Draw the tab """
        if self.active:
            color = arcade.color.GRAY
        else:
            color = arcade.color.LIGHT_GRAY
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, color)
        arcade.draw_text(self.label, self.x, self.y, arcade.color.BLACK, font_size=12, anchor_x="center", anchor_y="center")

    def is_clicked(self, x, y):
        """ Check if the tab was clicked """
        return (self.x - self.width // 2 < x < self.x + self.width // 2 and
                self.y - self.height // 2 < y < self.y + self.height // 2)

