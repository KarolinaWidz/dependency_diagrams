import os
from dependencyFinders.FilesWithDefinitionsDependencies import FilesWithDefinitionsDependencies


class FilesDependencies:

    def find_files_in_directory(self, file_path):
        file_names = []
        for root, dirs, files in os.walk(file_path):
            if root.__contains__("venv"):
                break
            for file_name in files:
                if file_name[-3:] == '.py':
                    fp = os.path.join(root, file_name)
                    size = os.path.getsize(fp)
                    file_names.append(file_name + " " + str(size))
        return file_names

    def find_files_dependencies(self, file_path, files_in_directory):
        counter = 0
        file_names = []
        file_dependencies = []
        cur_path = file_path+"/"+self
        if os.path.isfile(cur_path):
            with open(cur_path) as file:
                for line in file:
                    if line.startswith("from"):
                        file_names.append(line)
        else:
            cur_file = FilesWithDefinitionsDependencies.find_dir_with_file(self, file_path, self)
            with open(cur_file) as file:
                for line in file:
                    if line.startswith("from"):
                        file_names.append(line)

        for line in file_names:
            words = line.split()
            for file in files_in_directory:
                if (words[3] + ".py") == file:
                    file_dependencies.append(file)
                    counter += 1
        return file_dependencies, counter


