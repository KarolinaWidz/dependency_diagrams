import os
from dependencyFinders.ModuleDependencies import ModuleDependencies


class FunctionsCC:

    def get_file_cc(self, path_to_file):
        stream = os.popen('radon cc ' + path_to_file)
        output = stream.read()

        list_of_funtion_cc = []
        for l in output.splitlines():
            if ':' in l:
                if len(l.lstrip().split(' ')) >= 5:
                    cc = l.lstrip().split(' ')[4]
                    if '.' in l.lstrip().split(' ')[2]:
                        list_of_funtion_cc.append(tuple((l.lstrip().split(' ')[2].split('.')[1], cc)))
        return list_of_funtion_cc

    def get_all_functions_cc(self, path='.'):
        directories = ModuleDependencies().get_directory_names(path)
        function_cc = []
        for dirs in directories:
            filenames = ModuleDependencies().get_current_filenames_in_directory(dirs)
            for file in filenames:
                function_cc += self.get_file_cc(file)

        files = [f for f in os.listdir(path) if os.path.isfile(f) if f[-3:] == '.py']
        print(files)
        for file_name in files:
            function_cc += self.get_file_cc(file_name)
        return dict(function_cc)

