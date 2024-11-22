# tutorial.py

class Tutorial:
    def __init__(self):
        self.messages = [
            "Welcome to Carcassonne!\n\n\n\nClick 'CONTINUE' to go through a quick tutorial.",
            "This is the help guide.\n\nYou can click here to learn more about the rules of the game, and get helpful tips!",
            "This is the scoreboard, where you can view your score as well as your opponents' scores.",
            "Use these buttons to adjust sound and turn off background music.",
            "To take your turn, draw a tile from here.",
            "To place your tile, click and drag the tile on the board, and place it where you would like.\n\nNote: You are able to rotate the tile by clicking your trackpad with two fingers.",
            "Place a meeple to claim a road, city, or monestary and earn points!\n\nTo learn more about how points are earned, please refer to the Help Guide.",
            "Finish your movement when you're done placing the tile and have claimed an area with one of your meeples, if you choose to do so.\n\nNote: Once the game has been started, this button will say 'Done'."
        ]

    def get_message(self, step):
        return self.messages[step] if step < len(self.messages) else None

    def get_total_steps(self):
        return len(self.messages)
