from tkinter import *

class Start_screen(Frame):

    def __init__(self, master, call_on_next):
        super(Start_screen, self).__init__(master)
        self.call_on_selected = call_on_next
        self.username = ""
        self.grid()

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Memory Card Game", font="Helvetica 20 bold").grid(row=0, column=0, sticky=N)
        Label(self).grid(row=1, column=0)
        Label(self,
              text="Click on two cards (make sure to double \nclick the second card!). If they match, you get a point!\n If they don't, they'll flip back over. Try to remember \nthe cards so you can match all the pairs and win!").grid(
            row=2, column=0, sticky=N)
        Label(self).grid(row=3, column=0)

        start_button = Button(self, text="START GAME", font="Courier 16 bold", command=self.continue_clicked)
        start_button.grid(row=4, column=0, sticky=N)

    def continue_clicked(self):
        self.call_on_selected()

