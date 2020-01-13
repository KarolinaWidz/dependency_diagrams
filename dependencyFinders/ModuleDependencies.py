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