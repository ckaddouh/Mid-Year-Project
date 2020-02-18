# Card Object

from tkinter import *
import random
# from startScreen import Start_screen
# from memory import Application
# from summaryWindow import summary

class Card():
    def __init__(self, imageName, imageDict, buttonDict):
        self.ImageDict = imageDict
        self.ButtonDict = buttonDict
        self.imageName = imageName
        self.cardBack = PhotoImage(file = "deck_of_cards/purple_back.png")
        if "x" in self.imageName:
            self.cardID = self.imageName[11: 14]
        else:
            self.cardID = self.imageName[14: 17]

    def hide(self):
        self.ButtonDict[self.cardID]["image"] = self.cardBack
        self.ButtonDict[self.cardID]["command"] = self.show

    def show(self):
        self.ButtonDict[self.cardID]["image"] = self.ImageDict[self.cardID]
        self.ButtonDict[self.cardID]["command"] = self.hide
