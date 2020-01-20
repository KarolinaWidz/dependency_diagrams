from tkinter import *
from tkinter.filedialog import askdirectory
from Graph import Graph


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dependency diagrams")
        self.window.geometry('700x25')
        self.path = askdirectory(initialdir="..")
        print(self.path)
        self.selected1 = IntVar()
        self.selected2 = IntVar()
        self.selected3 = IntVar()
        self.selected4 = IntVar()
        self.file_button = Checkbutton(self.window, text="Files dependencies", bg='mistyrose', variable=self.selected1,
                                       onvalue=1, offvalue=0, command=self.show)
        self.file_button.grid(column=0, row=0)
        self.method_button = Checkbutton(self.window, text="Methods dependencies", bg='skyblue',
                                         variable=self.selected2, onvalue=1, offvalue=0, command=self.show)
        self.method_button.grid(column=1, row=0)
        self.package_button = Checkbutton(self.window, text="Packages dependencies", bg='yellowgreen',
                                          variable=self.selected3, onvalue=1, offvalue=0, command=self.show)
        self.package_button.grid(column=2, row=0)
        self.method_files = Button(self.window, text = "Files with Methods dependencies", bg='khaki',
                                   command=self.show_files_method_dependencies)
        self.method_files.grid(column=3,row=0)

    def show_files_method_dependencies(self):
        tmp = Graph()
        tmp.files_methods_dependencies(self.path)
    def show(self):
        tmp = Graph()
        if (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 0):
            tmp.files_dependency(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 0):
            print("Files + methods")
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 1):
            print("Files + methods + packages")
            tmp.files_with_modules_with_methods(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 1):
            print("Methods + packages")
        elif (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 1):
            print("Files + packages")
            tmp.files_with_modules(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 0):
            print("Methods")
        elif (self.selected1.get() == 0) & (self.selected2.get() == 0) & (self.selected3.get() == 1):
            tmp.module_dependency(self.path)
            print("Packages")

