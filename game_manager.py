''' This file is used to keep track of the tutorial, 
and make sure that if the tutorial has already been 
displayed in an instance of the game the tutorial will 
not be displayed again.'''

class GameManager:
    def __init__(self):
        # Initialize tutorial state as False
        self.tutorial_seen = False
