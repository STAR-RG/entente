import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

jerryjs_path = os.path.join(constants.seeds_dir, 'JerryJS')

IGNORED_FILES = []


# @pytest.mark.skip(reason="temporarilly disabling")
def test_jerryjs_ecma():
    path_name = os.path.join(jerryjs_path, 'ecma')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        validator=validate
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_jerryjs_regression():
    path_name = os.path.join(jerryjs_path, 'regression')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        shell='shell.js', validator=validate
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_jerry_debugger():
    path_name = os.path.join(jerryjs_path, 'debugger')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        validator=validate
    )
