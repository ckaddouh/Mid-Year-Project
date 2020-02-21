# This file will manage the various screens of the game.

from tkinter import *
from startScreen import Start_screen
from memory import Application
from summaryWindow import summary

# Define a class Memory_Manager() which manages the screens of our Memory card game.
class Memory_Manager():
    # Intialize the function by creating a root and setting a number of cards.
    def __init__(self):
        self.root = Tk()
        self.current_screen = None
        self.numOfCards = 24

    # Define startscreen to display the welcome screen when the program is opened.
    def startscreen(self):
        self.root.title("Welcome! ")
        self.current_screen = Start_screen(self.root, self.start_button)

    # Create a start button which destroys the start screen and opens up the game window.
    def start_button(self):
        self.current_screen.destroy()
        self.memoryGame()

    # Run the game window and link this to the end game window.
    def memoryGame(self):
        self.root.title("Memory!")
        self.current_screen = Application(self.root, self.summaryAction)

    # Once the game over button is pressed, summaryAction will run and the game over screen will be displayed.
    def summaryAction(self):
        self.current_screen.destroy()
        self.root.title("Game Summary")
        self.current_screen = summary(self.root, self.close_screen)

    # Once the exit button is clicked, exit the program.
    def close_screen(self):
        self.root.destroy()

# Define the main to run Memory_Manager(), startscreen(), and root.mainloop().
def main():
    memory = Memory_Manager()
    memory.startscreen()
    memory.root.mainloop()

# Run the main. 
main()