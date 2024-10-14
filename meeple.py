class Meeple:
    def __init__(self, player, color):
        self.plyer = player
        self.color = color
        isPlaced = False
        featureType = None
        orientation = None

        
    def placeMeeple(self, tile):
        # validate location of meeple
        if self.validatePlacement():
            # place meeple and save type of feature it was placed on
            # remove from player's supply
            self.isPlaced = True
            self.featureType = None # replace with feature type of tile
            if self.featureType == "field":
                self.orientation = "horizontal"
            else:
                self.orientation = "vertical"
            # store location on game board

    
    def validatePlacement():
        # if placing as highwayman, make sure only meeple on stretch of road
        # if placing as knight, make sure only meeple in city
        # if placing as monk/nun, make sure only meeple in monestary
        # if placing farmer, make sure on field
        return True


    def meepleScore(self):
        points = 0
        # find some way to check if feature is completed
        # calculate points won by meeple in feature
        if self.featureType == "road":
            # points = number of tiles in the complete road
            pass
        elif self.featureType == "city":
            # points = 2 per each tile in city, extra 2 if tile with coat of arms
            pass
        elif self.featureType == "monestary":
            points = 9
        else:
            pass

        # unplace and reset meeple
        self.isPlaced = False
        self.featureType = None
        # return meeple to supply
        return points
    

    def endOfGameScoring(self):
        points = 0
        # determine of feature is partially complete
        if self.featureType == "road":
            # points = number of tiles in the partial road
            pass
        elif self.featureType == "city":
            # points = 1 per each tile in partial city, extra 1 if tile with coat of arms
            pass
        elif self.featureType == "monestary":
            # points = number of tiles surrounding monestary + 1
            pass
        else:
            # points = 3 points per completed city the field is touching
            pass

        # unplace and reset meeple
        self.isPlaced = False
        self.featureType = None
        # return meeple to supply
        return points


if __name__ == "__main__":
    meeples = [Meeple("player", "red") for i in range(8)]
    print(meeples)

# functionality:
# store list of meeples in player class
# end of game storing

# potential issues:
# tiles where meeples can't be placed