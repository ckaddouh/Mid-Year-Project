# Card Object
class Card():
    def __init__(self, imageName):
        self.imageName = imageName
        self.cardID = self.imageName[0: 2]

    
    def hide(self):
        curCardDict[self]["image"] = 
        curCardDit[self]["command"] = self.show

    def show(self):
        self["image"] = self.imageName
        self["command"] = self.hide