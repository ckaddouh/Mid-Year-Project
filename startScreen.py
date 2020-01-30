from tkinter import *

class Start_screen(Frame):
    def __init__(self, master):
        super(Start_screen, self).__init__(master)

        #self.call_on_selcted = call_on_selected

        self.grid()

        self.create_widgets()

    def create_widgets(self):
        
        Label(self, text = "Memory Card Game", font = "Helvetica 20 bold").grid(row = 0, column = 0, sticky = N)
        Label(self, text = "Click on two cards. If they match, you get a point!\n If they don't, they'll flip back over. \nTry to remember the cards so you can match all the pairs and win!").grid(row = 1, column = 0, sticky = N)
        start_button= Button(self, text = "START GAME", font = "Courier 16 bold")
        start_button.grid(row = 2, column = 0, sticky = N)
    
    #def continue_clicked(self):
        #self.call_on_selcted(self.game.get())

root = Tk()
root.title("StartScreen")
root.geometry("410x150")
app = Start_screen(root)
root.mainloop()