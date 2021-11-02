#This script has some funtions to create/update a .gitignore File
import os, sys

working_path = os.path.abspath('.gitignore')

def appe_str_to_file(filename, string):
    '''Appends the given text to the specified file.'''
    f = open(filename, 'a')
    f.write(string + '\n')
    f.close()
    return

if  __name__ == '__main__':
    args = sys.argv[:]
    if len(args) > 1: # if no terminal argument is given shows the help info.
        for words in sys.argv[1:]:
            appe_str_to_file(working_path, words)
            print('Adding ' + words)
    else: # help info.
        print('Usage: python quickignore.py [filesnames]... \n'
              'Write filenames to the .gitignore of the current folder. \n'
              'If there is no .gitignore file one will be created.')