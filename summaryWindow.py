from tkinter import *

class summary(Frame):
    def __init__(self, master):
        super(summaryWindow, self).__init__(master)

        self.call_on_selcted = call_on_selected

        self.grid()
        
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "You Win!", font = "Helvetica 20 bold").grid(row = 0, column = 0, sticky = N)
        Label(self, text = "It took you %s to match %s pairs." % (time, numPairs), font = "Helvetica 20 bold").grid(row = 1, column = 0, sticky = N)
        Label(self).grid(row = 2,column = 0)

        retry_button= Button(self, text = "Retry", font = "Courier 16 bold", command = self.game)
        retry_button.grid(row = 3, column = 0, sticky = W)

        exit_button= Button(self, text = "Exit", font = "Courier 16 bold", command = self.close_screen)
        exit_button.grid(row = 3, column = 1, sticky = E)


    def continue_clicked(self):
        self.call_on_selcted(self.start_button.get())