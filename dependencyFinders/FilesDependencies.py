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

    def is_file(self, files):
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
            for root, dirs, files in os.walk(".",topdown=True):
                curDir = os.path.join(root)
                for d in dirs:
                    if ("venv" not in d) & ("__pycache__" not in d) & (".git"  not in d) & (".idea" not in d):
                        curSubDir = os.path.join(curDir, d)
                        for f in os.listdir(curSubDir):
                            if f[-3:] == '.py':
                                if f in self:
                                    curFile = os.path.join(curSubDir, f)
                                    with open(curFile) as file:
                                        for line in file:
                                            re.sub('\s+', ' ', line).strip()
                                            if line.startswith("from"):
                                                file_names.append(line)
        for x in file_names:
            words = x.split()
            if words[3] + ".py" in files:
                file_dependencies.append(words[3] + ".py")
                counter += 1
                print(file_dependencies)
        return file_dependencies, counter


