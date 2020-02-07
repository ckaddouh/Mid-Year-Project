# This file contains the logistics of the memory game. 

from tkinter import *
from CardObject import Card
import random
import time

class Application():
    def __init__(self, master, call_on_next):
        super(Application, self).__init__(master)
        self.cardDict = {}
        self.suitList = ("C D H S").split()
        self.numberList = ("1 2 3 4 5 6 7 8 9 A J Q K").split()
        self.call_on_selected = call_on_next
        self.selectCards()
    
    def selectCards():
        for i in range(12):
            cSuit = random.choice(self.suitList)
            cNumber = random.choice(self.numberList)
            imageName = cSuit + cNumber + ".jpg"
            temporaryCardList = self.cardDict.keys()
            if imageName not in list(temporaryCardList):
                self.cardDict[cSuit+cNumber] = Card(imageName)
                self.cardDict[cSuit+cNumber+"x"]=Card(imageName)
                del(temporaryCardList[cSuit+cNumber])


    def continue_clicked(self):
        self.call_on_selected()


