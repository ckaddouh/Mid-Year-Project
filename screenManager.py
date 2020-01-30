# This file will manage the various screens of the game.  

from tkinter import *

class Memory_Manager(object):
    def __init__(self, numOfCards):
        # Initializes a new battle manager by loading the card images and by initializing tkinter.  
        self.root = tkinter.Tk()
        self.current_screen = None
<<<<<<< HEAD

=======
        self.numOfCards = numOfCards
        c = Canvas(self.root, height = 300, width = 350, bg = "blue")
        c.pack()
        

    def displayCards(self):
        cardDict = {}
        
        
>>>>>>> 447a8f2366c179a9a0ff59077b34fd6a118c1dbb
    def flipCard(self):
        # Uses Canvas to illustrate a card flipping over.  

root.mainloop()