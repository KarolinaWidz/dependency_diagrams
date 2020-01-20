import os


class ModuleDependencies:

    def get_directory_names(self, path='.'):
        list_of_folders = next(os.walk(path))[1]
        list_of_folders = [path + '/' + x for x in list_of_folders if x not in ['.idea', 'venv', '__pycache__', '.git']]
        return list_of_folders

    def get_current_filenames_in_directory(self, name_of_current_directory):
        file_names = []
        for root, dirs, files in os.walk(name_of_current_directory):
            for file_name in files:
                if file_name[-3:] == '.py':
                    file_names.append(name_of_current_directory + '/' + file_name)
        return file_names

    def get_relation_names(self, path='.'):
        list_nodes = ModuleDependencies().get_directory_names(path)
        tmp = []
        for dir_name in list_nodes:    # iteruje po folderach
            current_filenames_in_directory_list = ModuleDependencies().get_current_filenames_in_directory(dir_name)
            for current_file in current_filenames_in_directory_list:    # iteruje po plikach w folderze
                if os.path.isfile(current_file):
                    with open(current_file) as file:
                        for line in file:
                            line = line.strip()
                            if line.startswith("from "):
                                file_package = line.split(' ')[1].split('.')[0]
                                if file_package in list_nodes:
                                    if file_package == dir_name:
                                        continue
                                    tmp.append(tuple((dir_name, file_package)))
                                else:
                                    continue
                            #
                            elif line.startswith('def'):
                                if len(line.split(' ')) >= 2 and len(line.split(' ')[1].split('(')) >= 1 \
                                                             and len(dir_name.split('/')) >= 1:
                                 tmp.append(tuple((line.split(' ')[1].split('(')[0], dir_name.split('/')[-1])))
        tmp2 = []
        for i in tmp:
            tmp2.append(tuple((tmp.count(i), i)))
        return list(set([i for i in tmp2]))
