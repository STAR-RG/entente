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
base_dir = os.getcwd()

if not os.path.exists(os.path.join(base_dir,'javascript')):
    raise NameError("please load this module from the base directory (or generalize this code)")

js_dir = os.path.join(base_dir, 'javascript/')
seeds_dir = os.path.join(base_dir, 'seeds/')
rhino = find('*.jar', os.path.join(js_dir, 'rhino/buildGradle/libs/'))
javascriptcore_release_dir = os.path.join(js_dir, 'WebKit/WebKitBuild/Release/')
javascriptcore_lib_dir = os.path.join(javascriptcore_release_dir, 'lib/')
javascriptcore = find('jsc', os.path.join(javascriptcore_release_dir, 'bin/'))