import os


class FilesWithDefinitionsDependencies:
    def open_file(self, file_path, file_name):
        tmp = []
        cur_path = file_path + "/" + file_name
        with open(cur_path,errors = 'ignore') as file:
            for line in file:
                line = line.strip()
                if line.startswith("def "):
                    line = line.split(' ')[1].split("(")[0]
                    tmp.append(line)
        return tmp

    def find_dir_with_file(self, file_path, file_name):
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
        cur_path = file_path + "/" + file_name
        if os.path.isfile(cur_path):
            tmp = FilesWithDefinitionsDependencies.open_file(self, file_path, file_name)

        else:
            cur_file = FilesWithDefinitionsDependencies.find_dir_with_file(self, file_path, file_name)
            with open(cur_file,errors = 'ignore') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("def "):
                        line = line.split(' ')[1].split("(")[0]
                        tmp.append(line)

        names = {file_name: tmp}
        return names
