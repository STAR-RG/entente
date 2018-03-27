import os, fnmatch

## file constants
this_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.join(this_dir, '../')
seeds_dir = os.path.join(base_dir, 'seeds/')
logs_dir = os.path.join(base_dir, 'logs/')
if not os.path.exists(os.path.join(base_dir, 'js_engines')):
    raise NameError("please load this module from the base directory (or generalize this code)")
js_dir = os.path.join(base_dir, 'js_engines/bin')

# fuzzing constants
num_iterations = 10

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

# javascriptcore
javascriptcore = find('jsc', js_dir)
# chakra
chakra = find('ch', js_dir)
# spider monkey
spidermonkey = find('spidermonkey', js_dir)
# v8
v8 = find('v8', js_dir)