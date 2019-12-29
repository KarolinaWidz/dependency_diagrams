import re
import os
from pathlib import Path
from FilesDependencies import FilesDependencies


class FilesMethodsDependencies:
    def methods_in_file(self, file_name):
        tmp = []
        if os.path.isfile(file_name):
            with open(file_name) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("def"):
                        tmp.append(line)
        else:
            for root, dirs, files in os.walk("."):
                if root.__contains__("venv"):
                    break
                for f in files:
                    if f[-3:] == '.py':
                        if f.__contains__(file_name):
                            fp = os.path.join(root, file_name)
                            if os.path.isfile(fp):
                                with open(fp) as file:
                                    for line in file:
                                        line = line.strip()
                                        if line.startswith("def"):
                                            tmp.append(line)
        names = {file_name: tmp}
        return names
