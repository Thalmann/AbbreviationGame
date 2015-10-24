import os

def set_directory(directory):
    os.chdir(directory)

def get_available_abbreviations():
    return os.listdir('../database/')

def get_abbreviation_list(list_name):
    l = dict()
    with open(list_name, 'r') as f:
        for line in f:
            for a, r, l in line.split(','):
                l[a] = r, l
    return l

set_directory('../database/')
print(get_available_abbreviations())
for a, r, l in get_abbreviation_list('dummy.txt'):
    print(a, r, l)
