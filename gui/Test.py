from tkinter import *
from Graph import Graph
from PIL import ImageTk, Image


class gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Diagrams")
        self.window.geometry('600x900')
        self.selected1 = IntVar()
        self.selected2 = IntVar()
        self.selected3 = IntVar()
        self.file_button = Checkbutton(self.window, text="Files dependencies", bg='mistyrose', variable=self.selected1,
                                       onvalue=1, offvalue=0, command=self.show)
        self.file_button.grid(column=0, row=0)
        self.method_button = Checkbutton(self.window, text="Methods dependencies", bg='skyblue',
                                         variable=self.selected2, onvalue=1, offvalue=0, command=self.show)
        self.method_button.grid(column=1, row=0)
        self.package_button = Checkbutton(self.window, text="Packages dependencies", bg='yellowgreen',
                                          variable=self.selected3, onvalue=1, offvalue=0, command=self.show)
        self.package_button.grid(column=2, row=0)

    def show(self):
        if (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 0):
            Graph.files_dependency(self)
            img = Image.open("graph.png")
            img = img.resize((500,700), Image.ANTIALIAS)
            tmp = ImageTk.PhotoImage(img)
            label =Label(image=tmp)
            label.image = tmp
            label.place(x=20, y=30)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 0):
            print("Files + methods")
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 1):
            print("Files + methods + packages")
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 1):
            print("Methods + packages")
        elif (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 1):
            print("Files + packages")
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 0):
            print("Methods")
        elif (self.selected1.get() == 0) & (self.selected2.get() == 0) & (self.selected3.get() == 1):
            print("Packages")
