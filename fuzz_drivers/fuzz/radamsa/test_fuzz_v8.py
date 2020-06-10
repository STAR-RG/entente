import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

v8_path = os.path.join(constants.seeds_dir, 'v8')


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_kraken():
    path_name = os.path.join(v8_path, 'benchmarks/data/kraken')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        fuzzer='radamsa', shell='kraken_shell.js'
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_sunspider():
    path_name = os.path.join(v8_path, 'benchmarks/data/sunspider')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        fuzzer='radamsa'
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_octane():
    path_name = os.path.join(v8_path, 'benchmarks/data/octane')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        fuzzer='radamsa', shell='octane_shell.js'
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_monorail():
    path_name = os.path.join(v8_path, 'monorail')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        fuzzer='radamsa', shell='octane_shell.js'
    )
