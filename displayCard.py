# This file selects cards, randomizes them, and displays them to the screen.  
from CardObject import Card
import random
from PIL import Image, ImageTk
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
        for name in list(cardDict.keys()):
            cardName.append(name)
        random.shuffle(cardName)
        row = 1
        column = 1
        for x in range(len(cardName)):
            image1 = Image.open(cardDict[x].imageName)
            photo = ImageTk.PhotoImage(image1)
            Button(self, text = "", command = cardDict[x].flip, image = photo).grid(row = row, column = column)
            if row % 6 == 0:
                row += 1
            column += 1
            if column % 6 == 0:
                column

            # column = column%6 + 1
