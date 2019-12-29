from Graph import Graph
from gui.Test import gui


def main():
    test = gui()
    test.window.mainloop()
    tmp = Graph()
    tmp.files_methods_dependencies()


main()
