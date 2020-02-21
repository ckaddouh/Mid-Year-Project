# This file contains the logistics of the memory game and interacts with the card object.

from tkinter import *
from CardObject import Card
import random

# Define a class Application which creates a screen and sets initial values for dictionaries, lists, and images.
class Application(Frame):
    def __init__(self, master, call_on_next):
        super(Application, self).__init__(master)
        self.ImageDict = {}
        self.ButtonDict = {}
        self.cardDict = {}
        self.cardUpList = []
        self.cardGone = PhotoImage(file= "deck_of_cards/gray_block.png")
        self.cardBack = PhotoImage(file= "deck_of_cards/purple_back.png")
        self.cardsGoneList = []

        # Sets call_on_selected to a function which will pull up the next screen on the command of a button and formats the UI.
        self.call_on_selected = call_on_next
        self.selectCards()
        self.grid()

    # A function which selects 12 random cards and duplicates them.
    def selectCards(self):
        allCardsList = []

        for i in ("C D H S").split():
            for x in ("1 2 3 4 5 6 7 8 9 A J Q K").split():
                allCardsList.append(x+i)
        for i in range(12):
            card = random.choice(allCardsList)
            # These are placed in a dictionary which a key of their cardID and a value of a Card object.
            # The copy has an additional "x" added on to its cardID.
            self.cardDict[card + "."] = Card("deck_of_cards/" + card + ".png", self.ImageDict, self.ButtonDict, self.cardDict, self.cardUpList, False)
            self.cardDict[card + "x"] = Card("cards_copy/" + card + "x.png", self.ImageDict, self.ButtonDict, self.cardDict, self.cardUpList, False)
            allCardsList.remove(card)
        # Once the dictionary is randomly created, run createWidgets().
        self.createWidgets()

    # A function which adds labels and buttons to the screen, which specifically creates a 4 x 6 grid of card objects.
    def createWidgets(self):
        # Create a title at the top of the screen and randomize the keys of the card dictionary.
        Label(self, text = "MEMORY", font="Helvetica 20 bold").grid(row = 0, column = 3, columnspan = 2)
        self.cardIDList = list(self.cardDict.keys())
        random.shuffle(self.cardIDList)
        row = 1
        column = 1
        # Run through every key of the dictionary and load its image based on attributes of its object.
        for cardID in self.cardIDList:
            image1 = PhotoImage(file=self.cardDict[cardID].imageName)
            # Add this image to an image dictionary which has a key of cardID and a value of the images.
            self.ImageDict[cardID] = image1
            # Add this button to a button dictionary, and set its command to show when clicked.
            self.ButtonDict[cardID] = Button(self, text="", image=self.cardBack, command= "")
            self.ButtonDict[cardID].grid(row=row, column=column)
            self.ButtonDict[cardID]["command"] = self.cardDict[cardID].show
            # Format the cards in a 4 x 6 grid.
            if column % 6 == 0 and column != 0:
                row += 1
            column = column % 6 + 1
        # Create a button which calls the next screen.
        Button(self, text="Game Over", command=self.continue_clicked).grid(row=5, column=5)

    # Call the next screen as defined in screenManager.py.
    def continue_clicked(self):
        self.call_on_selected()