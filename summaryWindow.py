from tkinter import *

class summary(Frame):
    def __init__(self, master, retry, exit):
        super(summary, self).__init__(master)

        self.grid()

        self.retry = retry
        self.exit = exit

        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "You Win!", font = "Helvetica 20 bold").grid(row = 0, column = 0, sticky = N)
        Label(self, text = "It took you %s to match %s pairs." % (0, numPairs), font = "Helvetica 20 bold").grid(row = 1, column = 0, sticky = N)
        Label(self).grid(row = 2,column = 0)

        retry_button= Button(self, text = "Retry", font = "Courier 16 bold", command = self.retry_clicked)
        retry_button.grid(row = 3, column = 0, sticky = W)

        exit_button= Button(self, text = "Exit", font = "Courier 16 bold", command = self.exit_clicked)
        exit_button.grid(row = 3, column = 1, sticky = E)


    def retry_clicked(self):
       self.retry()

    def exit_clicked(self):
        self.exit()
