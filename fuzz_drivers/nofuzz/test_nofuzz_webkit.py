import os
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_webkit():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.es6')
    multicall.multicall_directories(path_name, False, validator=validate)

# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_webkit_benchmarks():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.microbenchmarks')
    multicall.multicall_directories(path_name, False, validator=validate)