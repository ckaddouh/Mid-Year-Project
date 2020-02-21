# Create a welcome screen which has instructions and a button to the next screen.
from tkinter import *

# Define a class Start_screen which displays a welcome, instructions, and a continue button.
class Start_screen(Frame):
    def __init__(self, master, call_on_next):
        # Initialize tkinter, set the next screen according to the value passed in screenManager.py.
        super(Start_screen, self).__init__(master)
        self.call_on_selected = call_on_next
        # Set up the screen and run create_widgets().
        self.grid()
        self.create_widgets()

    # A function which creates a title label and an instructions label.
    def create_widgets(self):
        Label(self, text="Memory Card Game", font="Helvetica 20 bold").grid(row=0, column=0, sticky=N)
        Label(self,
              text="Click on two cards (make sure to double \nclick the second card!). If they match, you get a point!\n If they don't, they'll flip back over. Try to remember \nthe cards so you can match all the pairs and win!").grid(
            row=2, column=0, sticky=N)

        # Create a start button which runs continue_clicked.
        start_button = Button(self, text="START GAME", font="Courier 16 bold", command=self.continue_clicked)
        start_button.grid(row=4, column=0, sticky=N)

    # Take the user to the next screen according to values passed in screenManager.py when the play button is clicked.
    def continue_clicked(self):
        self.call_on_selected()

