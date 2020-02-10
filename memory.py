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

    
    def selectCards():
        for i in range(12):
            cSuit = random.choice(self.suitList)
            cNumber = random.choice(self.numberList)
            imageName = cSuit + cNumber + ".jpg"
            temporaryCardList = self.cardDict.keys()
            self.cardDict[cSuit+cNumber] = Card(imageName))
            self.cardDict[cSuit+cNumber+"x"]=Card(imageName)
            del(temporaryCardList[cSuit+cNumber])
            
            if i >= len(temporaryCardList):
                break
        self.createWidgets()
    
    def createWidgets():
        self.cardIDList = list(self.cardDict.keys())
        random.shuffle(cardIDList)
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
        cardList = []
        for i in list(self.ButtonDict.keys()):
            if self.ButtonDict[i]["image"] != self.cardBack:
                cardList += self.ButonDict[i]
        return cardList

    def game(self):
        while countCardsUp <= 2:
            self.allCommandShow()
        self.allCommandRemove()
        time.delay(2)
        if cardList[0] == cardList[1]:
            cardList[0]["image"] = ""
            cardList[1]["image"] = ""
            del(self.ButtonDict[cardList[0]])
            del(self.ButtonDict[cardList[0]])
        else:
            self.allCommandRemove()

        if len(list(self.cardDict.keys())) <= 0:
            gameOver = True


    def continue_clicked(self):
        self.call_on_selected()