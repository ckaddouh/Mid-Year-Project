# This file will manage the various screens of the game.

from tkinter import *
from startScreen import Start_screen
from memory import Application
from summaryWindow import summary


class Memory_Manager (object):
    def __init__(self):
        # Initializes a new battle manager by loading the card images and by initializing tkinter.
        self.root = Tk()
        self.current_screen = None
        self.numOfCards = numOfCards
        self.numOfCards = 24

    def startscreen(self):
        self.root.title("Welcome! ")
        self.current_screen = Start_screen(self.root, self.start_button)

    def start_button(self):
        self.current_screen.destroy()
        self.game()

    def game(self):
        self.root.title("Memory!")
        self.current_screen = Application(self.root, self.summary)
    
    def summary(self):
        self.current_screen.destroy()
        self.root.title("Game Summary")
        self.current_screen = summary(self.root, self.startscreen, self.close_screen)
    
    def close_screen(self):
        self.current_screen.destroy()


def main():
    memory = Memory_Manager()
    memory.startscreen()
    memory.root.mainloop()

main()