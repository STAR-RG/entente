import os
import re
import json
import fnmatch
import datetime
import logging
import glob
from .utils import string_to_hash
from jsfuzz.utils.BLACKLIST import get_blacklist, duktape_utils, v8_data


date = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")

# file constants
this_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.join(this_dir, '../../')
seeds_dir = os.path.join(base_dir, 'seeds/')
logs_dir = os.path.join(base_dir, 'logs_{}/'.format(date))
fuzzers_scripts_dir = os.path.join(base_dir, 'jsfuzz', 'fuzzer')
quickfuzz_dir = os.path.join(seeds_dir, 'quickfuzz')

# fuzzing constants
num_iterations = 20
limit_num_consecutive_unsuccessful_iterations = 10
timeout_JS_engine = 2
num_tests_grammar_based = 1000

# loggers
logging.basicConfig(level=logging.DEBUG, filename='/tmp/debug.log',
                    filemode='w')
logging.disable(logging.DEBUG)  # disable debugging


def find(file_name, path):
    # This function looks for a file (file_name param) within a directory
    result = find_file_bypattern(file_name, path)
    return [] if result == [] else result[0]


def find_file_bypattern(pattern, path):
    result = []
    # pylint: disable=W0612
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def get_versions(ch=None, sm=None, jsc=None, v8=None, hermes=None):
    versions = {}
    status_path = os.path.join(engines_dir, 'status.json')
    with open(status_path) as doc:
        v = json.load(doc)
    versions['ch'] = v['chakra'] if ch in [None, 'latest'] else ch
    versions['jsc'] = v['javascriptcore'] if jsc in [None, 'latest'] else jsc
    versions['v8'] = v['v8'] if v8 in [None, 'latest'] else v8
    versions['sm'] = v['spidermonkey'] if sm in [None, 'latest'] else sm
    versions['hermes'] = v['hermes'] if hermes in [None, 'latest'] else hermes
    return versions


def scan_seeds(root_path, _format='*.js', ignore_files=[], shell=None):
    ignore_files.extend(['assert.js', 'shell.js', 'run.js', 'kraken_shell.js',
                         'octane_shell.js'])
    ignore_files.extend(duktape_utils)
    ignore_files.extend(v8_data)

    blacklist = get_blacklist()

    pattern = r"(?<=seeds\/).*$"
    regex = re.compile(pattern, re.IGNORECASE)

    if shell:
        shell_file = None
        for path, dirs, files in os.walk(root_path):
            for d in dirs:
                for f in glob.iglob(os.path.join(path, d, _format)):
                    if shell and os.path.basename(f) == shell:
                        shell_file = f
        if not shell_file:
            # back directory
            root = root_path.split('/')
            root_path = '/'.join(root[0:root.index('seeds')+2])
            return scan_seeds(root_path=root_path, _format=_format,
                              ignore_files=ignore_files, shell=shell)
        return shell_file
    else:
        total = []
        for path, dirs, files in os.walk(root_path):
            for d in dirs:
                for f in glob.iglob(os.path.join(path, d, _format)):
                    # get pathname after seeds/ pattern
                    name = regex.search(f).group()
                    name = string_to_hash(name)
                    if name in blacklist:
                        continue
                    if os.path.basename(f) not in ignore_files:
                        total.append(f)
        total.sort()
        return total


home_dir = os.path.expanduser('~')
engines_dir = os.path.join(home_dir, '.jsvu')
# javascriptcore
javascriptcore = find('jsc', engines_dir)
# chakra
chakra = find('ch', engines_dir)
# spider monkey
spidermonkey = find('sm', engines_dir)
# v8
v8 = find('v8', engines_dir)
# hermes
hermes = find('hermes', engines_dir)

fuzzers_dir = os.path.join(base_dir, 'js_engines')
# radamsa
radamsa = find('radamsa', fuzzers_dir)
# quickfuzz
quickfuzz = find('QuickFuzz', fuzzers_dir)
cache_quickfuzz = find('cache_quickfuzz.txt', fuzzers_dir)
