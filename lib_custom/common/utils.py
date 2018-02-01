import os
import glob


class FileUtils:
    @staticmethod
    def clean_directory(dir_path, ignore_pattern):
        files = glob.glob(dir_path)
        for file_ in files:
            if not ignore_pattern in file_:
                os.remove(file_)
                print 'File removed {}'.format(file_)

    @staticmethod
    def save_txt_file(file_path, file_content):
        with open(file_path, 'w') as outfile:
            outfile.writelines(["%s\n" % item for item in file_content])

    @staticmethod
    def create_folder(long_file_path):
        if not os.path.exists(long_file_path):
            os.mkdir(long_file_path)


class MiscUtils:

    @staticmethod
    def check_variables_specified(variables_list):
        for variable in variables_list:
            if os.getenv(variable.upper()) is None:
                raise ValueError("Variable {} not specified.".format(variable))
