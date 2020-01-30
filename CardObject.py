# Card Object

class Card():
    def __init__(self, imageName):
        self.imageName = imageName
        cardID = self.imageName[0: 2]
        self.cardID = cardID
    
    def flip(self):
        
