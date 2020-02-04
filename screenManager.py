# This file will manage the various screens of the game.  

from tkinter import *
from startScreen import Start_screen
from CardObject import Card

class Memory_Manager(object):
    def __init__(self, numOfCards):
        # Initializes a new battle manager by loading the card images and by initializing tkinter.  
        self.root = tkinter.Tk()
        self.current_screen = None
        self.numOfCards = numOfCards

    def startscreen(self):
        self.root.title("Welcome! ")
        self.current_screen = startScreen()

    def start_button(self):
        self.current_screen.destroy
        self.game()
    
    def game(self):
        self.root.title("Memory!")
        self.current_screen = displayCard(self.root, self.close_screen)
    
    def summary(self):
        self.current_screen.destroy
        self.root.title("Game Summary")
        self.current_screen = summaryWindow(self.root, self.close_screen, self.start_button)

    def close_screen(self):
        self.current_screen.destroy()

def main():
    memory = memory_Manager()
    memory.startscreen()
    memory.root.mainloop()

main()