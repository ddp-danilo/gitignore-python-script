import pytest
import autogitignore as gitig
import random
from os import path

def is91to96(y):# avoids the characters that could be a plobem
    if y >= 91 and y <= 96:
        return True # returns true if is inbetween 91 and 96
    return False
def random_srt(size=random.randrange(1,255)): # returns a string with random sizes and values.
    rn_srt = ''
    for n in range(size):
        chr_n = ''
        while chr_n == '' or is91to96(chr_n) :
            chr_n = random.randrange(48,122)
        rn_srt += chr(chr_n)
    return rn_srt
def randomstr_tuple(tuple_size):# makes a tuple of random strings
    tuple_values = []
    for i in range(tuple_size):
        tuple_values.append(random_srt())
    return tuple_values
def find_linebreaks(string):# uses the linebreaks to make a word tuple
    for n in range(len(string)):
        if string[n] == '\n':
            return [string[:n]] + find_linebreaks(string[n + 1:])
    return [string]

print(find_linebreaks('abc\nteste\n123'))
working_path = path.abspath('test_gitignore')
z = open(working_path,'w') # blanks the file.
z.write('')
z.close()

def appestrtofile(list):
    for word in list:
        gitig.appe_str_to_file(working_path, word)

@pytest.mark.parametrize('wrds_to_test', [
    (['abc','test','123']),
    (randomstr_tuple(10)), # 10 items
    (randomstr_tuple(1)) # 1 item
])

def test_gitignore(wrds_to_test):
    appestrtofile(wrds_to_test)# adds 
    r = open(working_path, 'r')
    rs = r.read()
    r.close()
    d = open(working_path, 'w')# blanks the test file
    d.write('')
    d.close()
    rs = find_linebreaks(rs)
    for i in range(len(wrds_to_test)):
        assert wrds_to_test[i] == rs[i]