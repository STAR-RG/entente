import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants


# @pytest.mark.skip(reason="temporarilly disabling")
def test_hermes():
    path_name = os.path.join(constants.seeds_dir, 'hermes')
    multicall.multicall_directories(
        path_name,
        fuzzer='quickfuzz',
        validator=validate
    )
