from graphviz import Digraph
from FilesDependencies import FilesDependencies
import os


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
            dependencies = FilesDependencies.is_file(file, names)
            for dependent_file in dependencies:
                graph.edge(file, dependent_file)
        graph.view()
