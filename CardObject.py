# Card Object
class Card():
    def __init__(self, imageName, number, suit):
        self.imageName = imageName
        cardID = self.imageName[0: 2]
        self.cardID = cardID
        self.number = number
        self.suit = suit
    
    def flip(self, curShow, curHid):
    