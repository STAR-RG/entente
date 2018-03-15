import os, fnmatch

## find a file within a directory
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return [] if result == [] else result[0]

## constants
base_dir = os.path.join(os.getcwd(), '..')
seeds_dir = os.path.join(base_dir, 'seeds/')

if not os.path.exists(os.path.join(base_dir, 'javascript')):
    raise NameError("please load this module from the base directory (or generalize this code)")
js_dir = os.path.join(base_dir, 'javascript/bin')
# javascriptcore
javascriptcore = find('jsc', js_dir)
# chakra
chakra = find('ch', js_dir)
# spider monkey
spidermonkey = find('spidermonkey', js_dir)
# v8
v8 = find('v8', js_dir)
