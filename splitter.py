import os, sys, getopt, pathlib
import splitter_dialect

class Splitter(object):
    def __init__(self, dialect):
        self.dialect = dialect

    def split(self, file_path, output, lines_per_file):
        lines = self.dialect.read_file(file_path)

        start = 0
        end = lines_per_file
        file_name, output_file_ext = os.path.splitext(file_path)

        self._create_output_if_necessary(output)

        while start <= len(lines):
            new_lines = lines[start:end]
            self._write(new_lines, f'{output}/{self._format_file_name(start, end)}{output_file_ext}')
            start += lines_per_file
            end += start
    
    def _create_output_if_necessary(self, output):
        pathlib.Path(output).mkdir(parents=True, exist_ok=True)

    def _format_file_name(self, start, end):
        return f'chunk-{start}-{end}'

    def _write(self, lines, file_name):
        self.dialect.write_file(lines, file_name)

def print_help():
    print('splitter.py -i <inputfile> -l <linesperfile> [-o <output directory>]')

def extract_args(argv):
    inputfile = None
    output = '.'
    linesperfile = None
    try:
        opts, args = getopt.getopt(argv,"hi:o:l:",["ifile=","output=","linesperfile="])
        for opt, arg in opts:
            if opt == '-h':
                print_help()
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--output"):
                output = arg
            elif opt in ("-l", "--linesperfile"):
                linesperfile = arg

        return (inputfile, output, linesperfile)
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

def main(argv):
    inputfile, output, linesperfile = extract_args(argv)

    if(not inputfile):
        print_help()
        sys.exit(2)

    if(not linesperfile):
        print_help()
        sys.exit(2)

    splitter = Splitter(splitter_dialect.Text())
    splitter.split(inputfile, output, int(linesperfile))

if(__name__ == '__main__'):
    main(sys.argv[1:])