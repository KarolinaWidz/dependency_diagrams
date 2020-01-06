from graphviz import Digraph
from dependencyFinders.FilesDependencies import FilesDependencies
from dependencyFinders.FilesMethodsDependencies import FilesMethodsDependencies
from Color import Color


class Graph:
    def files_dependency(self):
        file_names = FilesDependencies.find_files_in_directory(self)
        names = []
        sizes = []
        graph = Digraph('graph', format='png', filename='graph',
                        node_attr={'color': 'mistyrose', 'style': 'filled', 'shape': 'circle'})
        graph.attr(size='50')

        for i in file_names:
            tmp = i.split(" ")
            names.append(tmp[0])
            sizes.append(tmp[1])

        for file, size in zip(names, sizes):
            graph.node(file, **{'width': str(float(size) / 400), 'height': str(float(size) / 400)})
            dependencies, counter = FilesDependencies.find_files_dependencies(file, names)
            for dependent_file in dependencies:
                graph.edge(file, dependent_file, *{str(counter)})
        #graph.view()

    def files_methods_dependencies(self):
        file_names = FilesDependencies.find_files_in_directory(self)
        names = []
        sizes = []
        graph = Digraph('graph2', format='png', filename='graph2',
                        node_attr={'color': 'khaki', 'style': 'filled', 'shape': 'doublecircle'})
        graph.attr(size='50')
        color = Color()
        for i in file_names:
            tmp = i.split(" ")
            names.append(tmp[0])
            sizes.append(tmp[1])

        methods = FilesMethodsDependencies.get_all_methods(self, names)

        for file, size in zip(names, sizes):
            same_function_dependencies = FilesMethodsDependencies.methods_in_file(self, file)[0]
            different_function_dependencies, counter = FilesMethodsDependencies.find_dependencies(self, file,methods)
            graph.node(file, **{'width': str(float(size) / 400), 'height': str(float(size) / 400),
                                'color': color.__str__()})
            for i in same_function_dependencies[file]:
                graph.edge(file,i)
            for i in different_function_dependencies:
                graph.edge(i,file)
            color.h += 0.1
        #graph.view()
