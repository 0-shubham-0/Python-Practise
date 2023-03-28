from tkinter import *

win = Tk()

win.title("GUI")
win.geometry('1000x500')
l1 = Label(win, text="Number 1")
l1.grid(column=1, row=1, pady=20, padx=10)
l2 = Label(win, text="Number 1")
l2.grid(column=1, row=2, pady=20, padx=10)
txt1 = Entry(win, width=10)
txt1.grid(column=2, row=1, pady=20, padx=10)
txt2 = Entry(win, width=10)
txt2.grid(column=2, row=2, pady=20, padx=10)
l3 = Label(win)
l3.grid(column=3, row=2, padx=20, pady=10)


def click(a, b):
    l3.configure(text=a+b)


b1 = Button(win, text="Add", command=lambda: click(int(txt1.get()), int(txt2.get())))
b1.grid(column=2, row=3, padx=20, pady=10)
win.mainloop()
