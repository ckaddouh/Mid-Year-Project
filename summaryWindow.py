# This window displays a summary screen.

from tkinter import *

class summary(Frame):
    def __init__(self, master, call_on_next):
        super(summary, self).__init__(master)

        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Label(self, text = "CONGRATULATIONS, "+self.username+"!").grid(row = 1, column = 1)
        Label(self, text = "You won Memory!")

    def exit_clicked(self):
        self.call_on_selected()