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
rhino_path = find('*.jar', os.path.join(js_dir,'rhino/buildGradle/libs/'))
javascriptcore_path = find('jsc', os.path.join(js_dir,'WebKit/WebKitBuild/Release/bin'))
