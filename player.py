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

#-----------------------------------------------------------------------------------
    ''' Setter Methods '''
    ''' Function to set (add) points to total score '''
    def set_score(self, points: int):
        # Add points to player score
        self.score += points

    ''' Function to reduce remaining meeples in player's hand, set value to -1 '''
    def use_meeple(self):
        # Check if there are meeples remaining in hand
        if self.meeples > 0:
            # If meeples, reduce number by 1
            self.meeples -= 1
        # If there are no meeples in hand, print warning message
        else:
            print(f"{self.name}: you have no meeples in hand to use, all are in play.")

    ''' Function to increase number of meeples in player's hand, set value to +1 '''
    def add_meeple(self):
        # Check if the total count of meeples in hand is less than or equal to 4
        if self.meeples <= 4:
            # If there is room for another meeple, ncrease meeples count by 1
            self.meeples += 1
        # If all meeples are in hand, print warning message
        else: 
            print(f"{self.name}: all meeples are in your hand, cannot add more.")

#-----------------------------------------------------------------------------------
    ''' Getter Methods '''
    ''' String function to return player status: name, score, and remaining meeples in player's hand '''
    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}, Meeples in hand: {self.meeples}"
    
    ''' Function to get count of meeples in hand'''
    def get_meeple_count(self):
        return self.meeples
    
    ''' Function to get player name '''
    def get_name(self):
        return self.name
    
    ''' Function to get player score '''
    def get_score(self):
        return self.score

#-----------------------------------------------------------------------------------
'''
Test for setter methods.
Expect: 
For adding score = Player: Grace, Score: 10, Meeples in hand: 5
For removing meeple = Player: Grace, Score: 10, Meeples in hand: 4
For setting (adding) meeple = Player: Grace, Score: 10, Meeples in hand: 5
'''
def test_one():
    # Instantiate player
    player1 = Player(name= "Grace")
    # Print player status
    print(player1)
    # Set score to 10
    player1.set_score(10)
    # Print status to check value correctly set
    print(player1)
    # Remove meeple from hand, set total meeples count to -1
    player1.use_meeple()
    # Print status to check value correctly set
    print(player1)
    # Add meeple to hand, set total meeples count to +1
    player1.add_meeple()
    # Print status to check value correctly set
    print(player1)
    
'''
Test for getter methods.
Expect: 
Player name = Grace
Player score = 0
Player meeples in hand = 5
Player: Grace, Score: 0, Meeples in hand: 5
'''
def test_two():
    # Instantiate player
    player1 = Player(name= "Grace")
    # Print player 1 name
    print("Player 1 name: ", player1.get_name())
    # Print player 1 score
    print("Player 1 score: ", player1.get_score())
    # Print player 1 meeples in hand
    print("Player 1 meeples in hand:", player1.get_meeple_count())
    # Print player status
    print(player1)
    
''' 
Test if warning message for full-hand meeples is working.
Expect: 
Grace, all meeples are in your hand, cannot add more.
'''
def test_three():
    # Instantiate player
    player1 = Player(name= "Grace")
    # Try adding additional meeple to hand
    player1.add_meeple()
    
''' 
Test if warning message for no more meeples in hand is working.
Expect:
Player: Grace, Score: 0, Meeples in hand: 0
Grace: you have no meeples in hand to use, all are in play.
'''
def test_four():
    # Instantiate player
    player1 = Player(name= "Grace")
    # Loop through range 5 to remove all meeples from hand
    for i in range(5):
        player1.use_meeple()
    # Print player status
    print(player1)
    # Try removing additional meeple
    player1.use_meeple()
  
''' 
Single player simulation: 
Create a single player with name 'Grace', print initial status, 
add 10 points, remove meeple, add 5 points, remove meeple, 
add 5 points, add meeple, print player final status.
Expect: 
Initial Status = Player: Grace, Score: 0, Meeples in hand: 5.
Final Status = Player: Grace, Score: 20, Meeples in hand: 4.
'''
def test_five():
    # Instantiate player
    player1 = Player(name= "Grace")
    print("Player initial status...")
    # Print initial player status
    print(player1)
    # Add 10 points
    player1.set_score(10)
    # Remove meeple from hand
    player1.use_meeple()
    # Add 5 points
    player1.set_score(5)
    # Remove meeple from hand
    player1.use_meeple()
    # Add 5 points
    player1.set_score(5)
    # Add meeple to hand
    player1.add_meeple()
    print("Player final status...")
    # Print final player status
    print(player1)
    
''' 
Multiple players simulation: 
Create a two players with name 'Grace' and 'Sansa', print initial statuses, 
add 10 points to Grace, remove meeple from Grace, add 5 points to Sansa, 
remove meeple from Grace, print each player's final status. 
Expect: 
Initial Status Grace = Player: Grace, Score: 0, Meeples in hand: 5.
Initial Status Sansa = Player: Sansa, Score: 0, Meeples in hand: 5.
Final Status Grace = Player: Grace, Score: 10, Meeples in hand: 4.
Final Status Sansa= Player: Sansa, Score: 5, Meeples in hand: 4.
'''
def test_six():
    # Instantiate players
    player1 = Player(name= "Grace")
    player2 = Player(name= "Sansa")
    # Print players initial status
    print("Player 1 initial status...")
    print(player1)
    print("Player 2 initial status...")
    print(player2)
    # Divider for better understanding of initial and final statuses
    print("---------------------------------------")
    # Remove meeple from Grace's hand
    player1.use_meeple()
    # Add score to Grace
    player1.set_score(10)
    # Remove meeple from Sansa'a hand
    player2.use_meeple()
    # Add score to Sansa
    player2.set_score(5)
    #Print players final status
    print("Player 1 final status...")
    print(player1)
    print("Player 2 final status...")
    print(player2)
    
    
''' Test Cases '''
#test_one()
#test_two()
#test_three()
#test_four()
#test_five()
#test_six()