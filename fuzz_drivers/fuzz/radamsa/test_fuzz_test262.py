import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.utils import constants, multicall
from jsfuzz.fuzzer.validator import validate


# @pytest.mark.skip(reason="temporarilly disabling")
def test_test262_annexB():
    path_name = os.path.join(constants.seeds_dir, 'test262/annexB')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        shell='shell.js',
        validator=validate
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_test262_builtins():
    path_name = os.path.join(constants.seeds_dir, 'test262/built-ins')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        shell='shell.js',
        validator=validate
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_test262_harness():
    path_name = os.path.join(constants.seeds_dir, 'test262/harness')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        shell='shell.js',
        validator=validate
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_test262_intl402():
    path_name = os.path.join(constants.seeds_dir, 'test262/intl402')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        shell='shell.js',
        validator=validate
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_test262_language():
    path_name = os.path.join(constants.seeds_dir, 'test262/language')
    multicall.multicall_directories(
        path_name,
        fuzzer='radamsa',
        shell='shell.js',
        validator=validate
    )
