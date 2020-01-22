import os


class FilesWithDefinitionsDependencies:
    def open_file(self, file_path, file_name):
        tmp = []
        cur_path = file_path + "/" + file_name
        with open(cur_path) as file:
            for line in file:
                line = line.strip()
                if line.startswith("def"):
                    line = line.split(' ')[1].split("(")[0]
                    tmp.append(line)
        return tmp

    def open_files_from_directory(self, file_path, file_name):
        cur_file = ''
        for root, dirs, files in os.walk(file_path, topdown=True):
            cur_dir = os.path.join(root)
            for d in dirs:
                if ("venv" not in d) and ("__pycache__" not in d) and (".git" not in d) and (".idea" not in d):
                    cur_sub_dir = os.path.join(cur_dir, d)
                    for f in os.listdir(cur_sub_dir):
                        if f[-3:] == '.py':
                            if f in file_name:
                                cur_file = os.path.join(cur_sub_dir, f)

        return cur_file

    def methods_in_file(self, file_path, file_name):
        tmp = []
        all_methods = []
        cur_path = file_path + "/" + file_name
        if os.path.isfile(cur_path):
            tmp = FilesWithDefinitionsDependencies.open_file(self, file_path, file_name)
            for i in tmp:
                all_methods.append(i)
        else:
            cur_file = FilesWithDefinitionsDependencies.open_files_from_directory(self, file_path, file_name)
            with open(cur_file) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("def "):
                        line= line.split(' ')[1].split("(")[0]
                        tmp.append(line)
                        all_methods.append(line)

        names = {file_name: tmp}
        return names, all_methods

    def get_all_methods(self, file_path, files):
        tmp = []
        for file in files:
            methods = FilesWithDefinitionsDependencies.methods_in_file(self, file_path, file)[1]
            for i in methods:
                tmp.append(i)
        return tmp

    def find_dependencies(self, file_path, file_arg, methods):
        tmp = []
        cur_path = file_path + "/" + file_arg
        if os.path.isfile(cur_path):
            with open(cur_path) as file:
                for line in file:
                    line = line.strip()
                    if not line.startswith("def"):
                        for met in methods:
                            k = met.replace("def ", '')
                            k = k.split("(")[0]
                            if k + "(" in line:
                                tmp.append(met)
        else:
            cur_file = FilesWithDefinitionsDependencies.open_files_from_directory(self, file_path, file_arg)
            with open(cur_file) as file:
                for line in file:
                    line = line.strip()
                    if not line.startswith("def"):
                        for met in methods:
                            k = met.replace("def ", '')
                            k = k.split("(")[0]
                            if k + "(" in line:
                                tmp.append(met)

        return tmp
