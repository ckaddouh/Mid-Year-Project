# This window displays a summary/end game screen.

from tkinter import *

# Define a class summary which displays a game over message.
class summary(Frame):
    # Initialize tkinter, run create_widgets(), and format the screen with grid().
    def __init__(self, master, exitScreen):
        super(summary, self).__init__(master)
        self.call_on_selected = exitScreen
        self.create_widgets()
        self.grid()

    # Create a congratulations and exit label on the screen.
    def create_widgets(self):
        Label(self, text = "CONGRATULATIONS!", font="Helvetica 20 bold", fg = "white", bg = "purple").grid(row = 1, column = 1)
        Label(self, text = "Come back to play soon!", font="Helvetica 20 bold").grid(row = 2, column = 1)

        # Create an exit button to exit the program.
        Button(self, text="EXIT!", command=self.exit_clicked, fg="white", bg="red").grid(row=6, column=1, sticky=E)

    # Define the exit to call the function in screenManager.py which closes the program.
    def exit_clicked(self):
        self.call_on_selected()
