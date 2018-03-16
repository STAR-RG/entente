import os, fnmatch

''' 
    This function looks for a file (file_name param) within a directory (path)
'''
def find(file_name, path):
    result = find_file_bypattern(file_name, path)
    return [] if result == [] else result[0]

def find_file_bypattern(pattern, path):
    result = []
    #pylint: disable=W0612
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result