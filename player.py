''' 
    Player Class: player name, score, and meeples in hand
    Grace Kinney
    10/7/2024
'''
import arcade


''' Player Class '''
class Player:
    ''' Constructor '''
    def __init__(self, name: str, meeples: int = 5):

        # Set player name to what is entered 
        self.name = name
        # Initial score set to 0
        self.score = 0
        # Default number of meeples set to 5
        self.meeples = meeples

    ''' Function to add points to total score '''
    def add_score(self, points: int):
        #
        self.score += points

    ''' Function to reduce remaining meeples in player's hand '''
    def use_meeple(self):
        # Check if there are meeples remaining in hand
        if self.meeples > 0:
            # If meeples, reduce number by 1
            self.meeples -= 1
        # If there are no meeples in hand, print no more
        else:
            print(f"{self.name} has no meeples left to use!")

    ''' Function to increase number of meeples in player's hand '''
    def return_meeple(self):
        # Increase meeples count by 1
        self.meeples += 1

    ''' Function to return player status: name, score, and remaining meeples in player's hand '''
    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}, Meeples: {self.meeples}"

if __name__=="__main__":
    