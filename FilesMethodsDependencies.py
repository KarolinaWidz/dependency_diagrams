import re
import os
from FilesDependencies import FilesDependencies


class FilesMethodsDependencies:
    def open_file(self, file_name):
        tmp = []
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                if line.startswith("def"):
                    tmp.append(line)
        return tmp

    def methods_in_file(self, file_name):
        tmp = []
        all_methods = []
        if os.path.isfile(file_name):
            tmp = FilesMethodsDependencies.open_file(self, file_name)
            all_methods.append(FilesMethodsDependencies.open_file(self, file_name))
        else:
            for root, dirs, files in os.walk("."):
                if root.__contains__("venv"):
                    break
                for f in files:
                    if f[-3:] == '.py':
                        if f.__contains__(file_name):
                            tmp = FilesMethodsDependencies.open_file(self, os.path.join(root, file_name))
                            all_methods.append(FilesMethodsDependencies.open_file(self, os.path.join(root, file_name)))
        names = {file_name: tmp}
        return names,all_methods

    def get_all_methods(self, files):
        tmp = []
        for file in files:
            methods = FilesMethodsDependencies.methods_in_file(self,file)[1]
            for i in methods:
                for j in i:
                    tmp.append(j)
        return tmp

    def find_dependencies(self, file, methods):
        tmp = []

        if os.path.isfile(file):
            with open(file) as file:
                for line in file:
                    line = line.strip()
                    if not line.startswith("def"):
                        for met in methods:
                            counter = 0
                            k = met.replace("def ", '')
                            k = k.split("(")[0]
                            if k+"(" in line:
                                tmp.append(met)
                                counter+=1
                                #tmp.append(line)
                        print(tmp)
                           # print(tmp)
               # names = {file: tmp}
            #print(tmp)


                        #if line.__contains__(k):
                                #tmp.append(line)




        return tmp




