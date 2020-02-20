# This window displays a summary screen.

from tkinter import *
from startScreen import Start_screen
class summary(Frame):
    def __init__(self, master):
        super(summary, self).__init__(master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
            Label(self, text = "CONGRATULATIONS!", font="Helvetica 20 bold", fg = "white", bg = "purple").grid(row = 1, column = 1)
            Label(self, text = "Come back to play soon!", font="Helvetica 20 bold").grid(row = 2, column = 1)

            # Label(self, text="NICE TRY!", font="Helvetica 20 bold").grid(row=1, column=1)
            # Label(self, text="Try and !", font="Helvetica 20 bold").grid(row=2, column=1)