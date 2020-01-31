# This file will manage the various screens of the game.  

from tkinter import *

class Memory_Manager(object):
    def __init__(self, numOfCards):
        # Initializes a new battle manager by loading the card images and by initializing tkinter.  
        self.root = tkinter.Tk()
        self.current_screen = None
        self.numOfCards = numOfCards

    def start_button(self):
        self.current_screen.destroy
        self.game()
    
    def game(self):
        self.root.title("Memory!")
        self.current_screen = displayCard(self.root, self.close_screen)

    def close_screen(self):
        self.current_screen.destroy()

    
def main():
    battle = Battle_Manager()
    battle.setup_character_selector()
    battle.root.mainloop()

main()