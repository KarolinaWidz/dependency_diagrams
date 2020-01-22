import glob
import inspect
import os
import re

# Historyjka 2: Jako programista chcę zobaczyć graf relacji między funkcjami/metodami w podanym kodzie źródłowym,
# w celu analizy zależności w kodzie źródłowym.
import textwrap


class MethodsDependencies:

    def methods_list_from_directory(self, project_directory_path):

        df_lines = []
        all_py_files_paths = glob.glob(project_directory_path + '/' + '**/*.py', recursive=True)

        # print(all_py_files_paths)
        # ścieżki plików .py które trzeba przeszukać

        for py_file_path in all_py_files_paths:
            with open(py_file_path) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("def "):
                        df_lines.append(line)

        # print(df_lines)
        # całe linie które zaczynają sie na "def"

        methods_list = []

        for line in df_lines:
            words = line.split()
            method_name = words[1].split("(")[0]
            if not method_name.startswith("__"):
                methods_list.append(method_name)

        # print(methods_list)
        # nazwy wszystkich metod w naszym projekcie

        return methods_list

    def get_list_of_dependecies_from_file(self, file_path, tab_of_all_functions):

        # nazwy wszystkich funkcji definiowanych w danym pliku - file_path
        names_of_function_in_file_splitted = []

        if os.path.isfile(file_path):
            names_of_function_in_file = self.open_clear_find(file_path, 'def ')

            for name in names_of_function_in_file:
                words = name.split()
                function_name = words[1].split("(")[0]
                if not function_name.startswith("__"):
                    names_of_function_in_file_splitted.append(function_name)

            list_of_dependencies = []

            for function in tab_of_all_functions:
                # indeks w tablicy counter
                i = 0

                # każda funkcja zdefiniowana w tym w pliku ma swój licznik
                counter = [0] * len(names_of_function_in_file_splitted)

                with open(file_path) as file:
                    if (function + "(") not in file.read():
                        continue
                    file.seek(0)
                    is_line_of_function = False

                    for line in file:

                        if line is '\n':  # skips blank lines
                            continue

                        if 'def' + ' ' not in line:
                            if is_line_of_function:
                                if not line.startswith(' ') and not line.startswith('\t'):
                                    is_line_of_function = False
                                    continue
                            counter[i] += line.count(function + "(")
                    else:
                        if is_line_of_function is True:
                            i += 1
                        else:
                            is_line_of_function = True

                for actual_function, actual_counter in zip(names_of_function_in_file_splitted, counter):
                    if actual_counter != 0:
                        list_of_dependencies.append((actual_function, function, actual_counter))

            return list_of_dependencies
        else:
            print("This is not a File.")
            return []

    def open_clear_find(self, name, word):
        names = []

        with open(name) as file:
            for line in file:
                line = line.strip()
                if line.startswith(word):
                    names.append(line)
        return names

    # MAIN
    def methods_dependency(self, project_directory_path):
        all_py_files_paths = glob.glob(project_directory_path + '/' + '**/*.py', recursive=True)
        functions_list = self.methods_list_from_directory(project_directory_path)

        functions_connections = []

        for file_path in all_py_files_paths:
            functions_connections.append(self.get_list_of_dependecies_from_file(file_path, functions_list))

        return functions_connections


# path = "C:/Users/Kuba/Desktop/GitHub/dependency_diagrams"
# test1 = MethodsDependencies()
# print(test1.methods_dependency(path))
