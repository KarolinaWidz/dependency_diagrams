import tempfile

from graphviz import Digraph
from dependencyFinders.FilesDependencies import FilesDependencies
from dependencyFinders.FilesWithDefinitionsDependencies import FilesWithDefinitionsDependencies
from dependencyFinders.ModuleDependencies import ModuleDependencies
from dependencyFinders.MethodsDependencies import MethodsDependencies
from Color import Color
from functionalities.CyclomaticComplexity import FunctionsCC
from functionalities.HashCommit import HashCommit


class Graph:
    #DEPENDENCIES
    def files_dependency(self, path):
        file_names = FilesDependencies.find_files_in_directory(self, path)
        names = []
        sizes = []
        graph = Digraph('filesGraph', format='pdf', filename='filesGraph',
                        node_attr={'color': 'mistyrose', 'style': 'filled', 'shape': 'circle'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))

        for i in file_names:
            tmp = i.split(" ")
            names.append(tmp[0])
            sizes.append(tmp[1])

        for file, size in zip(names, sizes):
            graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000)})
            dependencies, counter = FilesDependencies.find_files_dependencies(file, path, names)
            for dependent_file in dependencies:
                graph.edge(file, dependent_file, *{str(counter)})
        try:
            graph.view(tempfile.mktemp('.filesGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    def methods_dependencies(self, path):

        function_connections = []
        function_connections_tmp = MethodsDependencies().methods_dependency(path)
        function_names = MethodsDependencies().methods_list_from_directory(path)

        for element in function_connections_tmp:
            if element != []:
                function_connections.append(element)

        graph = Digraph('methodGraph', format='pdf', filename='methodGraph',
                        node_attr={'color': 'skyblue', 'style': 'filled', 'shape': 'doublecircle'})
        graph.attr(size='6,6', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))
        for name in function_names:
            graph.node(name)

        for edge in function_connections:
            for x in edge:
                graph.edge(x[1], x[0], label=str(x[2]))

        try:
            graph.view(tempfile.mktemp('.moduleGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    def module_dependency(self, path='.'):
        edges = ModuleDependencies().get_relation_names(path)
        graph = Digraph('moduleGraph', format='pdf', filename='moduleGraph',
                        node_attr={'color': 'yellowgreen', 'style': 'filled', 'shape': 'doublecircle'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))
        for i in edges:
            graph.edge(i[1][0], i[1][1], label=str(i[0]))
        try:
            graph.view(tempfile.mktemp('.moduleGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    def files_with_definitions_dependencies(self, path):
        file_names = FilesDependencies.find_files_in_directory(self, path)
        names = []
        sizes = []
        graph = Digraph('filesMethodsDefinitionsGraph', strict=True, format='pdf', filename='filesMethodsDefinitionsGraph',
                        node_attr={'color': 'khaki', 'style': 'filled', 'shape': 'doublecircle'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))
        color = Color()
        for i in file_names:
            tmp = i.split(" ")
            names.append(tmp[0])
            sizes.append(tmp[1])

        for file, size in zip(names, sizes):
            same_function_dependencies = FilesWithDefinitionsDependencies.methods_in_file(self, path, file)
            graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000),
                                'color': color.__str__()})
            for i in same_function_dependencies[file]:
                graph.edge(i, file)
            color.h += 0.05
        try:
            graph.view(tempfile.mktemp('.filesMethodsDefinitionsGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    #CC
    def module_dependency_with_cc(self, path='.'):
        edges = ModuleDependencies().get_relation_names(path)
        graph = Digraph('moduleGraph', format='pdf', filename='moduleGraph',
                        node_attr={'color': 'yellowgreen', 'style': 'filled', 'shape': 'doublecircle'})
        graph.attr(size='50', labelloc = 'b', label = 'Version: \n' + HashCommit.get_commit_hash(path))

        cc = FunctionsCC().get_all_functions_cc(path)

        for i in edges:
            if i[1][0] in cc:
                graph.edge(i[1][0] + '\ncc ' + cc[i[1][0]], i[1][1], label=str(i[0]))
            else:
                graph.edge(i[1][0], i[1][1], label=str(i[0]))
        try:
            graph.view(tempfile.mktemp('.moduleGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)


