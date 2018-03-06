import os, fnmatch

## find a file within a directory
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

## constants
js_dir = os.path.join(os.getcwd(), '../javascript/')
seeds_dir = os.path.join(os.getcwd(), '../seeds/')
rhino_path = find('*.jar', os.path.join(js_dir,'rhino/buildGradle/libs/'))[0]
javascriptcore_path = find('jsc', os.path.join(js_dir,'WebKit/WebKitBuild/Release/bin'))[0]
