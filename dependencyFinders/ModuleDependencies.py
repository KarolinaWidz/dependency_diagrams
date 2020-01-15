import os


class ModuleDependencies:

    # zwraca listę wszystkich katalogów w folderze
    def get_directory_names(self):
        list_of_folders = next(os.walk('.'))[1]
        list_of_folders = [x for x in list_of_folders if x not in ['.idea', 'venv', '__pycache__', '.git']]
        return list_of_folders

    def get_current_filenames_in_directory(self, name_of_curent_directory):
        file_names = []
        path = name_of_curent_directory
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name[-3:] == '.py':
                    # potrzebuje całej ścieżki do pliku
                    file_names.append(name_of_curent_directory + '/' + file_name)
        return file_names

    def get_relation_names(self):
        list_nodes = ModuleDependencies().get_directory_names()
        tmp = []
        # iteruje po folderach
        for current_node in list_nodes:
            current_filenames_in_directory_list = ModuleDependencies().get_current_filenames_in_directory(current_node)
            # iteruje po plikach w folderze
            for current_file in current_filenames_in_directory_list:
                if os.path.isfile(current_file):
                    with open(current_file) as file:
                        for line in file:
                            line = line.strip()
                            if line.startswith("from "):
                                file_package = line.split(' ')[1].split('.')[0]  # wycinam nazwę modułu z linii
                                if file_package in list_nodes:
                                    if file_package == current_node:
                                        continue
                                    tmp.append(tuple((current_node, file_package)))
                                else:
                                    continue
                            #
                            elif line.startswith('def'):
                                tmp.append(tuple((line.split(' ')[1].split('(')[0], current_file.split('/')[0])))
        tmp2 = []
        for i in tmp:
            tmp2.append(tuple((tmp.count(i), i)))
        return list(set([i for i in tmp2]))
