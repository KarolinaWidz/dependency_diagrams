from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror

from Graph import Graph
from Consolidation import Consolidation

class Window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Dependency diagrams")
        self.window.attributes('-topmost', True)
        self.window.update()
        self.window.geometry('770x25')
        self.path = askdirectory(initialdir="..")
        self.selected1 = IntVar()
        self.selected2 = IntVar()
        self.selected3 = IntVar()
        self.selected4 = IntVar()
        self.selected5 = IntVar()
        self.file_button = Checkbutton(self.window, text="Files dependencies", bg='mistyrose', variable=self.selected1,
                                       onvalue=1, offvalue=0, command=self.show)
        self.file_button.grid(column=0, row=0)
        self.method_button = Checkbutton(self.window, text="Methods dependencies", bg='skyblue',
                                         variable=self.selected2, onvalue=1, offvalue=0, command=self.show)
        self.method_button.grid(column=1, row=0)
        self.package_button = Checkbutton(self.window, text="Packages dependencies", bg='yellowgreen',
                                          variable=self.selected3, onvalue=1, offvalue=0, command=self.show)
        self.package_button.grid(column=2, row=0)
        self.method_files = Button(self.window, text="Files with definition dependencies", bg='khaki',
                                   command=self.show_files_method_dependencies)
        self.method_files.grid(column=4, row=0)
        self.method_button = Checkbutton(self.window, text="Cyclomatic Complexity", bg='bisque',
                                         variable=self.selected5, onvalue=1, offvalue=0, command=self.show)
        self.method_button.grid(column=3, row=0)
        if self.path is "":
            showerror("ERROR", "You didn't choose a dir")
            self.window.destroy()

    def show_error(self):
        showerror("ERROR", "Graphviz cannot generate the graph")

    def show_files_method_dependencies(self):
        tmp = Graph()
        tmp.files_with_definitions_dependencies(self.path)

    def show(self):
        tmp = Graph()
        consolidation = Consolidation()
        if (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 0) & (self.selected5.get() == 0):
            print("Files")
            tmp.files_dependency(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 0) & (self.selected5.get() == 0) :
            print("Files + methods")
            consolidation.files_with_methods(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 1) & (self.selected5.get() == 0):
            print("Files + methods + packages")
            consolidation.files_with_modules_with_methods(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 1) & (self.selected5.get() == 0):
            print("Methods + packages")
            consolidation.modules_with_methods(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 1) & (self.selected5.get() == 0):
            print("Files + packages")
            consolidation.files_with_modules(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 0) & (self.selected5.get() == 0):
            print("Methods")
            tmp.methods_dependencies(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 0) & (self.selected3.get() == 1) & (self.selected5.get() == 0):
            print("Packages")
            tmp.module_dependency(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 0) & (self.selected5.get() == 1):
            print("Files  with cyclomatic")
            tmp.files_dependency(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 0) & (self.selected5.get() == 1) :
            print("Files + methods with cyclomatic")
            consolidation.files_with_methods(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 1) & (self.selected3.get() == 1) & (self.selected5.get() == 1):
            print("Files + methods + packages with cyclomatic")
            consolidation.files_with_modules_with_methods(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 1) & (self.selected5.get() == 1):
            print("Methods + packages with cyclomatic")
            consolidation.modules_with_methods(self.path)
        elif (self.selected1.get() == 1) & (self.selected2.get() == 0) & (self.selected3.get() == 1) & (self.selected5.get() == 1):
            print("Files + packages with cyclomatic")
            consolidation.files_with_modules(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 1) & (self.selected3.get() == 0) & (self.selected5.get() == 1):
            print("Methods with cyclomatic")
            tmp.methods_dependencies(self.path)
        elif (self.selected1.get() == 0) & (self.selected2.get() == 0) & (self.selected3.get() == 1) & (self.selected5.get() == 1):
            print("Packages with cyclomatic")
            tmp.module_dependency_with_cc(self.path)

