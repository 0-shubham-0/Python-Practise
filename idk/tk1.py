from tkinter import *
win = Tk()
win.title("GUI")
win.geometry('350x200')
l1 = Label(win, text="Hello Worlds!!")
l1.place(x=200, y=100)
b1 = Button(win, text="Enter")
win.mainloop()
