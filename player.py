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
    def add_meeple(self):
        # Increase meeples count by 1
        self.meeples += 1

    ''' String function to return player status: name, score, and remaining meeples in player's hand '''
    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}, Meeples: {self.meeples}"

''' 
Test for correctness: 
Create a single player with name 'Grace', print initial status, 
add 10 points, remove meeple, add 5 points, remove meeple, 
add 5 points, add meeple, print player final status.
Expect: 
Initial status = Player: Grace, Score: 0, Meeples: 5.
Final Status = Player: Grace, Score: 20, Meeples: 4.
'''
def test_one():
    # Initialize player
    player1 = Player(name= "Grace")
    print("Player initial status...")
    # Print initial player status
    print(player1)
    # Add 10 points
    player1.add_score(10)
    # Remove meeple from hand
    player1.use_meeple()
    # Add 5 points
    player1.add_score(5)
    # Remove meeple from hand
    player1.use_meeple()
    # Add 5 points
    player1.add_score(5)
    # Add meeple to hand
    player1.add_meeple()
    print("Player final status...")
    # Print final player status
    print(player1)
    
#def test_two:
    
    
test_one()
#test_two()