""" This file is used to display content for the error message if a player makes an invalid move."""

class HelpfulTips:
    def __init__(self):
        # Define message
        self.message = "You cannot play there.\n\n\n\nIf you are trying to play a tile, it must be placed so that roads connect to roads, cities connect to cities, and fields connect to fields.\n\n\n\nClick anywhere to continue..."
        
    def get_message(self):
        """Return the error message."""
        return self.message
