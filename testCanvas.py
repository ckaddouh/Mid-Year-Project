from tkinter import *

root = Tk()
root.geometry("300x350")

c = Canvas(root, height = 300, width = 350, bg="blue")
l = c.create_line(5,5,100,7, width = 5)
o = c.create_oval(20,20,100,100, fill = "red")

c.pack()

root.mainloop()