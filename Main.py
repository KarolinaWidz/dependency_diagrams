from Graph import Graph
from gui.Window import Window


def main():
    test = Window()
    test.window.mainloop()
    tmp = Graph()
    tmp.files_dependency()
    tmp.files_methods_dependencies()


main()
