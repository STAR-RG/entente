import os
from fuzzer import util

## constants
base_dir = os.getcwd()
seeds_dir = os.path.join(base_dir, 'seeds/')
logs_dir = os.path.join(base_dir, 'logs/')

if not os.path.exists(os.path.join(base_dir, 'javascript')):
    raise NameError("please load this module from the base directory (or generalize this code)")
js_dir = os.path.join(base_dir, 'javascript/bin')

# javascriptcore
javascriptcore = util.find('jsc', js_dir)
# chakra
chakra = util.find('ch', js_dir)
# spider monkey
spidermonkey = util.find('spidermonkey', js_dir)
# v8
v8 = util.find('v8', js_dir)
