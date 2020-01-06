import os
import re


class FilesDependencies:

    def find_files_in_directory(self):
        file_names = []
        for root, dirs, files in os.walk("."):
            if root.__contains__("venv"):
                break
            for file_name in files:
                if file_name[-3:] == '.py':
                    fp = os.path.join(root, file_name)
                    size = os.path.getsize(fp)
                    file_names.append(file_name + " " + str(size))
        return file_names

    def find_files_dependencies(self, files_in_directory):
        counter = 0
        file_names = []
        file_dependencies = []

        if os.path.isfile(self):
            with open(self) as file:
                for x in file:
                    re.sub('\s+', ' ', x).strip()
                    if x.startswith("from"):
                        file_names.append(x)
        else:
            for root, dirs, files in os.walk(".", topdown=True):
                cur_dir = os.path.join(root)
                for d in dirs:
                    if ("venv" not in d) and ("__pycache__" not in d) and (".git" not in d) and (".idea" not in d):
                        cur_sub_dir = os.path.join(cur_dir, d)
                        for f in os.listdir(cur_sub_dir):
                            if f[-3:] == '.py':
                                if f in self:
                                    cur_file = os.path.join(cur_sub_dir, f)
                                    with open(cur_file) as file:
                                        for line in file:
                                            re.sub('\s+', ' ', line).strip()
                                            if line.startswith("from"):
                                                file_names.append(line)

        for x in file_names:
            words = x.split()
            for file in files_in_directory:
                if (words[3] + ".py") == file:
                    file_dependencies.append(file)
                    counter += 1
        return file_dependencies, counter


