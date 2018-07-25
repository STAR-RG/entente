import os
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

jerryjs_path = os.path.join(constants.seeds_dir, 'JerryJS')

search_root = jerryjs_path
search_libfiles = ['assert.js']
IGNORED_FILES = []

#@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryjs():
    path_name = os.path.join(jerryjs_path, 'ecma')
    multicall.multicall_directories(path_name, False, validator=validate)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryJS_regression():
    path_name = os.path.join(jerryjs_path, 'regression')
    multicall.multicall_directories(path_name, False, validator=validate,
                                    search_root=search_root,
                                    search_libfiles=search_libfiles,
                                    ignored_files=IGNORED_FILES)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_jerry_debugger():
    path_name = os.path.join(jerryjs_path, 'debugger')
    multicall.multicall_directories(path_name, False, validator=validate)