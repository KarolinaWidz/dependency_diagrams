from graphviz import Digraph
from dependencyFinders.FilesDependencies import FilesDependencies
from dependencyFinders.FilesMethodsDependencies import FilesMethodsDependencies
from dependencyFinders.ModuleDependencies import ModuleDependencies
from Color import Color


class Graph:
    def files_dependency(self,path):
        file_names = FilesDependencies.find_files_in_directory(self,path)
        names = []
        sizes = []
        graph = Digraph('filesGraph', format='pdf', filename='filesGraph',
                        node_attr={'color': 'mistyrose', 'style': 'filled', 'shape': 'circle'})
        graph.attr(size='50')

        for i in file_names:
            tmp = i.split(" ")
            names.append(tmp[0])
            sizes.append(tmp[1])

        for file, size in zip(names, sizes):
            graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000)})
            dependencies, counter = FilesDependencies.find_files_dependencies(file,path, names)
            for dependent_file in dependencies:
                graph.edge(file, dependent_file, *{str(counter)})
        graph.view()

    def files_with_modules(self,path):
        file_names = FilesDependencies.find_files_in_directory(self,path)
        names = []
        sizes = []
        edges = ModuleDependencies().get_relation_names(path)
        graph = Digraph('filesModulesGraph', format='pdf', filename='filesModulesGraph',
                        node_attr={'style': 'filled', 'shape': 'circle'})
        graph.attr(size='50')

        with graph.subgraph(name='packages') as modules_graph:
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
                dependencies, counter = FilesDependencies.find_files_dependencies(file,path, names)
                for dependent_file in dependencies:
                    files_graph.edge(file, dependent_file, *{str(counter)})
        graph.view()


    def files_with_modules_with_methods(self, path):
        file_names = FilesDependencies.find_files_in_directory(self, path)
        names = []
        sizes = []
        edges = ModuleDependencies().get_relation_names(path)
        graph = Digraph('filesModulesGraph', format='pdf', filename='filesModulesGraph',
                        node_attr={'style': 'filled', 'shape': 'circle'})
        graph.attr(size='50')

        with graph.subgraph(name='packages') as modules_graph:
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
        graph.view()


    def files_methods_dependencies(self,path):
        file_names = FilesDependencies.find_files_in_directory(self,path)
        names = []
        sizes = []
        graph = Digraph('filesMethodsGraph', format='pdf', filename='filesMethodsGraph',
                        node_attr={'color': 'khaki', 'style': 'filled', 'shape': 'doublecircle'})
        graph.attr(size='50')
        color = Color()
        for i in file_names:
            tmp = i.split(" ")
            names.append(tmp[0])
            sizes.append(tmp[1])

        methods = FilesMethodsDependencies.get_all_methods(self,path, names)

        for file, size in zip(names, sizes):
            same_function_dependencies = FilesMethodsDependencies.methods_in_file(self,path, file)[0]
            different_function_dependencies, counter = FilesMethodsDependencies.find_dependencies(self,path, file,methods)
            graph.node(file, **{'width': str(float(size) / 15000), 'height': str(float(size) / 15000),
                                'color': color.__str__()})
            for i in same_function_dependencies[file]:
                graph.edge(file,i)
            for i in different_function_dependencies:
                graph.edge(i,file)
            color.h += 0.1
        graph.view()

    def module_dependency(self, path='.'):
        edges = ModuleDependencies().get_relation_names(path)
        graph = Digraph('moduleGraph', format='pdf', filename='moduleGraph',
                        node_attr={'color': 'yellowgreen', 'style': 'filled', 'shape': 'doublecircle'})
        for i in edges:
            graph.edge(i[1][0], i[1][1], label=str(i[0]))
        graph.view()
