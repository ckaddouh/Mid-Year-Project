# This file selects cards, randomizes them, and displays them to the screen.  
from CardObject import Card
import random

cardDict = {}
suitList = ["C", "D", "H", "S"]
numberList = ("1 2 3 4 5 6 7 8 9 A J K Q").split()

for i in range(12):
    cSuit = random.choice(suitList)
    cNumber = random.choice(numberList)
    name = cSuit + cNumber + ".jpg"
    if name not in list(cardDict.keys()):
        cardDict[name] = Card(name, cSuit, cNumber)
        cardDict[name + "2"] = Card(name, cSuit, cNumber)
#as;dlkfjd