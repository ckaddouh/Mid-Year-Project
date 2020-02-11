# Card Object
class Card():
    def __init__(self, imageName):
        self.imageName = imageName
        self.cardID = self.imageName[0: 2]

    
    def hide(self):
        self.ButtonDict[self]["image"] = self.cardBack
        self.ButtonDict[self]["command"] = self.show

    def show(self):
        self.ButtonDict[self]["image"] = self.imageName
        self.ButtonDict[self]["command"] = self.hide