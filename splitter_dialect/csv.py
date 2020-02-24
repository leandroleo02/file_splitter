import csv

class Csv(object):

    def read_file(self, file_path):
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            return list(reader)
    
    def write_file(self, lines, new_file_name):
        with open(new_file_name, 'w+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(lines)