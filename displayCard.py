# This file selects cards, randomizes them, and displays them to the screen.  
from CardObject import Card
import random

class Application():
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.cardDict = {}
        self.suitList = ["C", "D", "H", "S"]
        self.numberList = ("1 2 3 4 5 6 7 8 9 A J K Q").split()
        # self.call_on_selected = call_on_next

        self.createWidgets()
        self.grid()

    # Selects 12 cards
    for i in range(12):
        cSuit = random.choice(self.suitList)
        cNumber = random.choice(self.numberList)
        name = cSuit + cNumber + ".jpg"
        if name not in list(cardDict.keys()):
            self.cardDict[name] = Card(name, cSuit, cNumber)
            self.cardDict[name + "x"] = Card(name, cSuit, cNumber)

    # Randomize cards
    self.cardName = []
    for name in list(cardDict.keys()):
        self.cardName.append(name)
    random.shuffle(self.cardName)

    # Importing images
    def createWidgets(self):
        row = 1
        column = 1
        for x in range(self.cardName):
            photo = PhotoImage(file = cardDict[x].imageName)
            Button(root, text = "", command = cardDict[x].flip, image = photo).grid(row = row, column = column)
            if row % 6 == 0:
                row += 1
            column += 1
            if column % 6 == 0:
                column

            # column = column%6 + 1
