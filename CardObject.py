# Card Object

from tkinter import *
import random
import time
# from startScreen import Start_screen
# from memory import Application
# from summaryWindow import summary

class Card():
    def __init__(self, imageName, imageDict, buttonDict, cardDict, cardsUp, cleared, cardsGoneList):
        self.ImageDict = imageDict
        self.ButtonDict = buttonDict
        self.imageName = imageName
        self.cardDict = cardDict
        self.cardGone = PhotoImage(file = "deck_of_cards/gray_block.png")
        self.cardBack = PhotoImage(file = "deck_of_cards/purple_back.png")
        self.cardsGone = cardsGoneList
        if "x" in self.imageName:
            self.cardID = self.imageName[11: 14]
        else:
            self.cardID = self.imageName[14: 17]
        self.cardUpList = cardsUp
        self.cleared = cleared

    def hide(self):
        self.ButtonDict[self.cardID]["image"] = self.cardBack
        self.ButtonDict[self.cardID]["command"] = self.show

    def show(self):
        self.ButtonDict[self.cardID]["image"] = self.ImageDict[self.cardID]
        self.checkMatch()

    def allCommandShow(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = self.cardDict[i].show

    def allCommandHide(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = self.cardDict[i].hide

    def listCardsUp(self):
        if self.ButtonDict[self.cardID]["image"] != self.cardBack:
            self.cardUpList.append(self.cardID)

    def checkMatch(self):
        self.listCardsUp()
        if len(self.cardUpList) > 2:
            card1 = self.cardUpList[0]
            card2 = self.cardUpList[1]
            self.cardUpList.clear()

            time.sleep(1)

            if card1[0:2] == card2[0:2] and card1 != card2:
                self.ButtonDict[card1]["image"] = self.cardGone
                self.ButtonDict[card2]["image"] = self.cardGone
                self.cardDict[card1].cleared = True
                self.cardDict[card2].cleared = True
                del(self.ButtonDict[card1])
                del(self.ButtonDict[card2])
            else:
                self.ButtonDict[card1]["image"] = self.cardBack
                self.ButtonDict[card2]["image"] = self.cardBack

            for buttonID in list(self.ButtonDict.keys()):
                self.ButtonDict[buttonID]["image"] = self.cardBack
                if self.cardDict[buttonID].cleared:
                    self.ButtonDict[buttonID]["image"] = self.cardGone
                    self.ButtonDict[buttonID]["command"] = ""