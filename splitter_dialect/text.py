class Text(object):

    def read_file(self, file_path):
        with open(file_path) as f:
            return f.readlines()
    
    def write_file(self, lines, new_file_name):
        with open(new_file_name, 'w+') as f:
            f.writelines(lines)