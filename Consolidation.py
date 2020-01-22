import tempfile
from graphviz import Digraph
from dependencyFinders.FilesDependencies import FilesDependencies
from dependencyFinders.ModuleDependencies import ModuleDependencies
from dependencyFinders.MethodsDependencies import MethodsDependencies
from functionalities.HashCommit import HashCommit


class Consolidation:

    def files_with_modules(self, path):
        file_names = FilesDependencies.find_files_in_directory(self, path)
        names = []
        sizes = []
        edges = ModuleDependencies().get_relation_names(path)
        graph = Digraph('filesModulesGraph', format='pdf', filename='filesModulesGraph',
                        node_attr={'style': 'filled', 'shape': 'circle'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))

        with graph.subgraph(name='modules') as modules_graph:
            modules_graph.node_attr.update(style='filled', color='yellowgreen')
            for i in edges:
                modules_graph.edge(i[1][0], i[1][1], label=str(i[0]))

        with graph.subgraph(name='files') as files_graph:
            files_graph.node_attr.update(style='filled', color='mistyrose')
            for i in file_names:
                tmp = i.split(" ")
                names.append(tmp[0])
                sizes.append(tmp[1])

            for file, size in zip(names, sizes):
                files_graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000)})
                dependencies, counter = FilesDependencies.find_files_dependencies(file, path, names)
                for dependent_file in dependencies:
                    files_graph.edge(file, dependent_file, *{str(counter)})
        try:
            graph.view(tempfile.mktemp('.filesModulesGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    def files_with_methods(self, path):
        file_names = FilesDependencies.find_files_in_directory(self, path)
        names = []
        sizes = []
        function_connections = []
        function_connections_tmp = MethodsDependencies().methods_dependency(path)
        function_names = MethodsDependencies().methods_list_from_directory(path)

        for element in function_connections_tmp:
            if element != []:
                function_connections.append(element)
        graph = Digraph('filesMethodGraph', format='pdf', filename='filesMethodGraph',
                        node_attr={'style': 'filled', 'shape': 'circle', 'color':'skyblue'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))

        with graph.subgraph(name='methods') as method_graph:
            method_graph.node_attr.update(style='filled', color='skyblue')
            for name in function_names:
                graph.node(name)
            for edge in function_connections:
                for x in edge:
                    method_graph.edge(x[1], x[0], label=str(x[2]))

        with graph.subgraph(name='files') as files_graph:
            files_graph.node_attr.update(style='filled', color='mistyrose')
            for i in file_names:
                tmp = i.split(" ")
                names.append(tmp[0])
                sizes.append(tmp[1])

            for file, size in zip(names, sizes):
                files_graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000)})
                dependencies, counter = FilesDependencies.find_files_dependencies(file, path, names)
                for dependent_file in dependencies:
                    files_graph.edge(file, dependent_file, *{str(counter)})
        try:
            graph.view(tempfile.mktemp('.filesMethodGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    def modules_with_methods(self, path):
        function_connections = []
        function_connections_tmp = MethodsDependencies().methods_dependency(path)
        edges = ModuleDependencies().get_relation_names(path)
        function_names = MethodsDependencies().methods_list_from_directory(path)

        for element in function_connections_tmp:
            if element != []:
                function_connections.append(element)
        graph = Digraph('modulesMethodGraph', format='pdf', filename='modulesMethodGraph',
                        node_attr={'style': 'filled', 'shape': 'circle', 'color':'skyblue'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))

        with graph.subgraph(name='methods') as method_graph:
            method_graph.node_attr.update(style='filled', color='skyblue')
            for name in function_names:
                graph.node(name)
            for edge in function_connections:
                for x in edge:
                    method_graph.edge(x[1], x[0], label=str(x[2]))

        with graph.subgraph(name='modules') as modules_graph:
            modules_graph.node_attr.update(style='filled', color='yellowgreen')
            for i in edges:
                modules_graph.edge(i[1][0], i[1][1], label=str(i[0]))
        try:
            graph.view(tempfile.mktemp('.modulesMethodGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)

    def files_with_modules_with_methods(self, path):
        file_names = FilesDependencies.find_files_in_directory(self, path)
        names = []
        sizes = []
        function_connections = []
        function_connections_tmp = MethodsDependencies().methods_dependency(path)
        edges = ModuleDependencies().get_relation_names(path)
        function_names = MethodsDependencies().methods_list_from_directory(path)

        for element in function_connections_tmp:
            if element != []:
                function_connections.append(element)
        graph = Digraph('modulesMethodFilesGraph', format='pdf', filename='modulesMethodFilesGraph',
                        node_attr={'style': 'filled', 'shape': 'circle', 'color':'skyblue'})
        graph.attr(size='50', labelloc='b', label='Version: \n' + HashCommit.get_commit_hash(path))

        with graph.subgraph(name='methods') as method_graph:
            method_graph.node_attr.update(style='filled', color='skyblue')
            for name in function_names:
                graph.node(name)
            for edge in function_connections:
                for x in edge:
                    method_graph.edge(x[1], x[0], label=str(x[2]))

        with graph.subgraph(name='modules') as modules_graph:
            modules_graph.node_attr.update(style='filled', color='yellowgreen')
            for i in edges:
                modules_graph.edge(i[1][0], i[1][1], label=str(i[0]))

        with graph.subgraph(name='files') as files_graph:
            files_graph.node_attr.update(style='filled', color='mistyrose')
            for i in file_names:
                tmp = i.split(" ")
                names.append(tmp[0])
                sizes.append(tmp[1])

            for file, size in zip(names, sizes):
                files_graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000)})
                dependencies, counter = FilesDependencies.find_files_dependencies(file, path, names)
                for dependent_file in dependencies:
                    files_graph.edge(file, dependent_file, *{str(counter)})

        try:
            graph.view(tempfile.mktemp('.modulesMethodFilesGraph'))
        except Exception:
            from gui.Window import Window
            Window.show_error(Window)