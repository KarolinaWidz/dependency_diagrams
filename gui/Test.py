from tkinter import *


class gui:
    @staticmethod
    def show():
        window = Tk()
        label = Label(window, text="HELLO WORLD")
        label.pack()
        window.mainloop()
