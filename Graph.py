from graphviz import Digraph
from FilesDependencies import FilesDependencies
import os


class Graph:
    def files_dependency(self):
        file_names = FilesDependencies.find_files_in_directory(self)
        graph = Digraph('graph', format='png', filename='graph',
                        node_attr={'color': 'mistyrose', 'style': 'filled', 'shape': 'diamond'})
        graph.attr(size='50')
        for file in file_names:
            graph.node(file+ "\n"  + str(os.path.getsize(file)))
            dependencies = FilesDependencies.is_file(file, file_names)
            for dependent_file in dependencies:
                graph.edge(file + "\n"  + str(os.path.getsize(file)), dependent_file)
        graph.view()

