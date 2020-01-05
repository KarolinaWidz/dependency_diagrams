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

            for x in file_names:
                words = x.split()
                if words[1] + ".py" in files:
                    file_dependencies.append(words[1] + ".py")
                    counter += 1
            return file_dependencies, counter
        else:
            return [], 0
