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

if not os.path.exists(os.path.join(base_dir, 'javascript')):
    raise NameError("please load this module from the base directory (or generalize this code)")

js_dir = os.path.join(base_dir, 'javascript/')
seeds_dir = os.path.join(base_dir, 'seeds/')
# rhino
rhino = find('*.jar', os.path.join(js_dir, 'rhino/buildGradle/libs/'))
# javascriptcore
javascriptcore_release_dir = os.path.join(js_dir, 'WebKit/WebKitBuild/Release/')
javascriptcore_lib_dir = os.path.join(javascriptcore_release_dir, 'lib/')
javascriptcore = find('jsc', os.path.join(javascriptcore_release_dir, 'bin/'))
# chakra
chakra = find('ch', os.path.join(js_dir, 'ChakraCore/out/Release/'))
# spider monkey
spidermonkey = find('js', os.path.join(js_dir, 'gecko-dev/js/src/build_OPT.OBJ/dist/bin'))
v8 = find('d8', os.path.join(js_dir, 'v8/out.gn/x64.release/'))
