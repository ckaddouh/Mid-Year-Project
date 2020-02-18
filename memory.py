# This file contains the logistics of the memory game.

from tkinter import *
from cardObject import Card
import random
import time

class Application(Frame):
    def __init__(self, master, call_on_next):
        super(Application, self).__init__(master)
        self.cardDict = {}
        self.suitList = ("C D H S").split()
        self.numberList = ("1 2 3 4 5 6 7 8 9 A J Q K").split()
        self.call_on_selected = call_on_next
        self.selectCards()
        self.grid()

<<<<<<< HEAD
    def selectCards(self):
        allCardsList = []
        self.ImageDict = {}
        self.ButtonDict = {}
        for i in self.suitList:
            for x in self.numberList:
                allCardsList.append(x+i)
=======
    
    def selectCards(self):
>>>>>>> 73904c8f7a73a60da707c4b3d79caca7ff6d350c
        for i in range(12):
            card = random.choice(allCardsList)
            self.cardDict[card + "."] = Card("deck_of_cards/" + card + ".png", self.ImageDict, self.ButtonDict)
            self.cardDict[card + "x"] = Card("cards_copy/" + card + "x.png", self.ImageDict, self.ButtonDict)
            allCardsList.remove(card)

        self.createWidgets()
<<<<<<< HEAD

    def createWidgets(self):
        Label(self, text = "MEMORY", font="Helvetica 20 bold").grid(row = 0, column = 3, columnspan = 2)
=======
    
    def createWidgets(self):
>>>>>>> 73904c8f7a73a60da707c4b3d79caca7ff6d350c
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

    def listCardsUp(self):
        self.cardList = []
        for i in list(self.ButtonDict.keys()):
            if self.ButtonDict[i]["image"] == self.cardDict[i].imageName:
                cardList.append(i)
        return cardList

    def checkMatch(self):
        cardUpList = self.listCardsUp()
        while len(cardUpList) < 2:
            self.allCommandShow()
            cardUpList = self.listCardsUp()
            print(cardUpList)
        self.allCommandHide()

        if cardUpList[0] == cardUpList[1][0:2] or cardUpList[0][0:2] == cardUpList[1]:
            cardUpList[0]["image"] = ""
            cardUpList[1]["image"] = ""
            del(self.ButtonDict[cardUpList[0]])
            del(self.ButtonDict[cardUpList[0]])
        else:
            self.ButtonDict[cardUpList[0]]["image"] = self.cardBack
            self.ButtonDict[cardUpList[1]]["image"] = self.cardBack
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
        length = len(list(self.ButtonDict.keys()))
        while length > 0:
            self.checkMatch()
            length = len(list(self.ButtonDict.keys()))
        Button(self, text="Game Over").grid(row=5, column=5)

    def continue_clicked(self):
        self.call_on_selected()