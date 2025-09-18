class FileFunctions:

    def add_line_to_file(self, file_path, line):
        with open(file_path, 'a') as file:
            file.write(line + '\n')

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()