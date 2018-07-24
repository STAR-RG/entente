from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall

search_libfiles = ['shell.js']
IGNORED_FILES = []

# @pytest.mark.skip(reason="temporarilly disabling")
def test_tinyjs():
    path_name = os.path.join(constants.seeds_dir, 'TinyJS')
    multicall.multicall_directories(path_name, True, validator=validate,
                                    search_root=path_name,
                                    search_libfiles=search_libfiles,
                                    ignored_files=IGNORED_FILES)