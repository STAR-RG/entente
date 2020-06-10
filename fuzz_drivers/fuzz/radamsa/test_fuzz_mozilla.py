import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate_mozilla
from jsfuzz.utils import constants, multicall

# see https://chromium.googlesource.com/v8/v8.git/+/6.8.40/test/mozilla/mozilla.status
# for test compatibility details for v8


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_mozilla():
    path_name = os.path.join(constants.seeds_dir, 'mozilla')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        validator=validate_mozilla,
        shell='shell.js'
    )
