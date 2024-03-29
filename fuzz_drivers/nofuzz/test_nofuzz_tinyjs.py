import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

search_libfiles = ['shell.js']
IGNORED_FILES = []


# @pytest.mark.skip(reason="temporarilly disabling")
def test_tinyjs():
    path_name = os.path.join(constants.seeds_dir, 'TinyJS')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        shell='shell.js'
    )
