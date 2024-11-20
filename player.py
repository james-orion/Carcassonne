''' 
    Player Class: player name, score, and meeples in hand
    Grace Kinney
    10/7/2024
'''
import arcade
# Import Meeple Class
from meeple import Meeple

'''
NOTE: might do a list of meeples instead of a count, 
talk with Hack about combining meeple class with player clas
'''

''' Player Class '''
class Player:
    ''' Constructor '''
    def __init__(self, name: str = None, meeple_count: int = 5, ai = False):

        # Set player name to what is entered
        if name is None:
            # If no name is provided, prompt the user for input
            self.name = "Player"
            #self.name = input("Enter the player's name: ")
        else:
            self.name = name
            
        # Initial score set to 0
        self.score = 0
        self.color = None
        
        # Initialize a list of Meeple objects for the player
        self.meeples = [Meeple(self, "red") for i in range(meeple_count)]

        self.ai = ai

#-----------------------------------------------------------------------------------
    ''' Setter Methods '''
    ''' Function to set (add) points to total score '''
    def set_score(self, points: int):
        # Add points to player score
        self.score += points

    """ Function to place a meeple on a tile if available. """
    def use_meeple(self, tile, user_choice, settings):
        for meeple in self.meeples:
            # Check if meeple is in player's hand (not placed)
            if not meeple.is_placed:
                # Place meeple on the tile
                if meeple.place_meeple(tile, user_choice, settings) == True:
                    return True, meeple
                else:
                    return False, None
        # If no meeples are available, print warning message
        # print(f"{self.name}: you have no meeples left to place.")
        return False, None

    """ Function to return a meeple to the player's hand and add points to the player's score. """
    def add_meeple(self, points):
        for meeple in self.meeples:
            # Check if meeple is on the board (placed)
            if meeple.is_placed:
                # Get points from the meeple based on position
                earned_points = meeple.meeple_score()
                # Add the earned points to player's total score 
                self.set_score(earned_points + points)
                return True
        # print(f"{self.name}: No meeples to return.")
        return False
    
    def get_meeple_score(self, scored_meeple, tile, settings, connected_tiles, meeples_on_feature):
        self.set_score(scored_meeple.meeple_score(tile, settings, connected_tiles, meeples_on_feature))

    def set_name(self, name):
        self.name = name

    def set_ai(self):
        self.ai = True
    def default_ai(self):
        self.ai = False
    
    """ Calculate end-of-game points based on meeples still placed. """
    def end_of_game_scoring(self):
        points = 0
        for meeple in self.meeples:
            # Check if meeple is still on the board
            if meeple.is_placed:
                # Add end-of-game points from meeple position 
                # to playe'sr total score
                points += meeple.end_of_game_scoring()
        # Add points to player's total score
        self.set_score(points)

#-----------------------------------------------------------------------------------
    ''' Getter Methods '''
    ''' String function to return player status: name, score, and remaining meeples in player's hand '''
    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}, Meeples in hand: {self.get_meeple_count()}, AI : {self.ai}"
    
    ''' Function to get count of meeples in hand'''
    def get_meeple_count(self):
        # Return the number of meeples that are not placed
        return len([meeple for meeple in self.meeples if not meeple.is_placed])
    
    ''' Function to get player name '''
    def get_name(self):
        return self.name
    
    ''' Function to get player score '''
    def get_score(self):
        return self.score

    ''' Function to get player color '''
    def get_color(self):
        #return self.color
        return self.color

    def set_name(self,name):
        self.name = name
    
    def set_color(self, color):
        self.color = color
        for meeple in self.meeples:
            meeple.set_color(color)

    def is_ai(self):
        return self.ai

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