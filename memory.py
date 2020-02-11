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
        self.grid()
        self.selectCards()

    
    def selectCards(self):
        for i in range(12):
            cSuit = random.choice(self.suitList)
            cNumber = random.choice(self.numberList)
            imageName = cSuit + cNumber + ".jpg"
            temporaryCardList = self.cardDict.keys()
            self.cardDict[cSuit+cNumber] = Card(imageName)
            self.cardDict[cSuit+cNumber+"x"]=Card(imageName)
            del(temporaryCardList[cSuit+cNumber])
            
            if i >= len(temporaryCardList):
                break
        self.createWidgets()
    
    def createWidgets(self):
        self.cardIDList = list(self.cardDict.keys())
        random.shuffle(self.cardIDList)
        row = 1
        column = 1
        self.ButtonDict = {}
        self.cardBack = PhotoImage(file = "purple_back.jpg")
        for cardID in self.cardIDList:
            image1 = PhotoImage(file = self.cardDict[cardID].imageName)
            self.ButtonDict[cardID] = Button(self, text = "", image = self.cardBack, command = self.show)
            self.ButtonDict[cardID].grid(row=row, column = column)
            if row % 6 == 0:
                row += 1
            column = column % 6 + 1

    def allCommandShow(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = self.show

    def allCommandHide(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = self.hide

    def allCommandRemove(self):
        for i in list(self.ButtonDict.keys()):
            self.ButtonDict[i]["command"] = None        
        
    def listCardsUp(self):
        self.cardList = []
        for i in list(self.ButtonDict.keys()):
            if self.ButtonDict[i]["image"] != self.cardBack:
                self.cardList += self.ButtonDict[i]
        return self.cardList

    def checkMatch(self):
        while countCardsUp <= 2:
            self.allCommandShow()
        self.allCommandRemove()
        time.delay(2)
        if self.cardList[0] == self.cardList[1]:
            self.cardList[0]["image"] = ""
            self.cardList[1]["image"] = ""
            del(self.ButtonDict[self.cardList[0]])
            del(self.ButtonDict[self.cardList[0]])
        else:
            self.cardList[0]["image"] = self.cardBack
            self.cardList[1]["image"] = self.cardBack
            self.allCommandRemove()

    def runGame(self): 
        while len(list(self.cardDict.keys())) >= 0:
            self.checkMatch()
        Button(self, text = "Game Over")

    def continue_clicked(self):
        self.call_on_selected()