# Card Object which allows the cards to flip and checks if they are matching.

from tkinter import *
import time

# Define a class card with attributes of an image name, dictionaries of images, buttons, and cards, and
# the number of cards facing up.
class Card():
    def __init__(self, imageName, imageDict, buttonDict, cardDict, cardsUp, cleared):
        self.ImageDict = imageDict
        self.ButtonDict = buttonDict
        self.imageName = imageName
        self.cardDict = cardDict
        self.cardUpList = cardsUp

        # Define standard images for the back of cards and a gray block for when a card is matched.
        self.cardGone = PhotoImage(file = "deck_of_cards/gray_block.png")
        self.cardBack = PhotoImage(file = "deck_of_cards/purple_back.png")

        # Determines image name based on if the card is a copy (has "x" in the name) or if it is an original.
        if "x" in self.imageName:
            self.cardID = self.imageName[11: 14]
        else:
            self.cardID = self.imageName[14: 17]

    # A function which hides a card by setting its image to its back, and changing its command.
    def hide(self):
        self.ButtonDict[self.cardID]["image"] = self.cardBack
        self.ButtonDict[self.cardID]["command"] = self.show

    # A function which displays a card by setting its image to its value in the image dictionary and calls checkMatch().
    def show(self):
        self.ButtonDict[self.cardID]["image"] = self.ImageDict[self.cardID]
        self.checkMatch()

    # Appends the card to a list once it is flipped over. This is called by checkMatch() which is called every time a card is flipped.
    def listCardsUp(self):
        if self.ButtonDict[self.cardID]["image"] != self.cardBack:
            self.cardUpList.append(self.cardID)

    # Determines if two cards are matching and takes appropriate action.
    def checkMatch(self):
        # Waits until there are 2 cards facing up before comparing their cardIDs.
        self.listCardsUp()
        if len(self.cardUpList) > 2:
            card1 = self.cardUpList[0]
            card2 = self.cardUpList[1]
            self.cardUpList.clear()

            time.sleep(1)
        # Once the list is cleared and the user has been given a second to see the cards, their IDs are compared.
            if card1[0:2] == card2[0:2] and card1 != card2:
                # If they are matching, and the card is not itself, their images will be replaced by a gray block and they will be removed from the button dictionary.
                self.ButtonDict[card1]["image"] = self.cardGone
                self.ButtonDict[card2]["image"] = self.cardGone
                del(self.ButtonDict[card1])
                del(self.ButtonDict[card2])
            # If the cards are not matching, flip them back over.
            else:
                self.ButtonDict[card1]["image"] = self.cardBack
                self.ButtonDict[card2]["image"] = self.cardBack