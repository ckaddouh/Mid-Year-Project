# This file selects cards, randomizes them, and displays them to the screen.  
from CardObject import Card
import random
from tkinter import *

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
    

    # Importing images
    def createWidgets(self):
        cardName = []
        for name in list(self.cardDict.keys()):
            cardName.append(name)
        random.shuffle(cardName)
        row = 1
        column = 1
        for x in range(len(cardName)):
            cardBack = PhotoImage(file = "purple_back.jpg")
            image1 = PhotoImage(file = self.cardDict[x].imageName)
            self.curCard = Button(self, text = "", command = self.cardDict[x].hide, image = photo)
            self.curCard.grid(row = row, column = column)
            if row % 6 == 0:
                row += 1
            # if column % 6 == 0:
            #     column = 1
            # column += 1
        
            column = column%6 + 1
            if len(self.cardDict) <= 0:
                self.summary.get()

    def checkMatch(self, card1, card2):'
        if card1.cardID == card2.cardID:
            del(self.cardDict[card1])
            del(self.cardDict[card2])
        else:
            card1.hide()
            card2.hide()