# This file will manage the various screens of the game.  

from tkinter import *

class Memory_Manager(object):
    def __init__(self):
        # Initializes a new battle manager by loading the card images and by initializing tkinter.  
        self.root = Tkinter.Tk()

    def flipCard(self):
        # Uses Canvas to illustrate a card flipping over.  