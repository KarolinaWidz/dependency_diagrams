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
                    file_names.append(file_name)

        return file_names

    def is_file(self, files):
        file_names = []
        file_depedencies = []

        if os.path.isfile(self):
            with open(self) as file:
                for x in file:
                    re.sub('\s+', ' ', x).strip()
                    if x.startswith("from"):
                        file_names.append(x)

            for x in file_names:
                words = x.split()
                if words[1] + ".py" in files:
                    file_size = os.path.getsize(words[1] + ".py")
                    file_depedencies.append(words[1] + ".py\n" + str(file_size))
            return file_depedencies
        else:
            return []
