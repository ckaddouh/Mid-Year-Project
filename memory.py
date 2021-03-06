# This file contains the logistics of the memory game.

from tkinter import *
from CardObject import Card
import random
import time

class Application(Frame):
    def __init__(self, master, call_on_next):
        super(Application, self).__init__(master)
        self.cardDict = {}
        self.suitList = ("C D H S").split()
        self.numberList = ("1 2 3 4 5 6 7 8 9 A J Q K").split()
        self.cardUpList = []
        self.cardGone = PhotoImage(file= "deck_of_cards/gray_block.png")
        self.call_on_selected = call_on_next
        self.selectCards()
        self.grid()

    def selectCards(self):
        allCardsList = []
        self.ImageDict = {}
        self.ButtonDict = {}
        for i in self.suitList:
            for x in self.numberList:
                allCardsList.append(x+i)
        for i in range(12):
            card = random.choice(allCardsList)
            self.cardDict[card + "."] = Card("deck_of_cards/" + card + ".png", self.ImageDict, self.ButtonDict, self.cardDict, self.cardUpList, False)
            self.cardDict[card + "x"] = Card("cards_copy/" + card + "x.png", self.ImageDict, self.ButtonDict, self.cardDict, self.cardUpList, False)
            allCardsList.remove(card)

        self.createWidgets()

    def createWidgets(self):
        Label(self, text = "MEMORY", font="Helvetica 20 bold").grid(row = 0, column = 0, columnspan = 3)
        # self.checkButton.grid(row = 0, column = 6)
        self.cardIDList = list(self.cardDict.keys())
        random.shuffle(self.cardIDList)
        row = 1
        column = 1
        self.cardBack = PhotoImage(file= "deck_of_cards/purple_back.png")
        for cardID in self.cardIDList:
            image1 = PhotoImage(file=self.cardDict[cardID].imageName)
            self.ImageDict[cardID] = image1
            self.ButtonDict[cardID] = Button(self, text="", image=self.cardBack, command= "")
            self.ButtonDict[cardID].grid(row=row, column=column)
            self.ButtonDict[cardID]["command"] = self.cardDict[cardID].show
            if column % 6 == 0 and column != 0:
                row += 1
            column = column % 6 + 1
        self.runGame()

    def allCommandShow(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = self.cardDict[i].show

    def allCommandHide(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = self.cardDict[i].hide

    def allCommandRemove(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = ""

    def runGame(self):
        # length = len(list(self.ButtonDict.keys()))
        Button(self, text="Game Over", command = self.continue_clicked).grid(row=5, column=5)

    def continue_clicked(self):
        self.call_on_selected()