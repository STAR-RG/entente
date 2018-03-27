from regression_tests import *
from utils.multicall import multicall_directories
from utils import constants
from fuzzer.validator import validate
import pytest


# @pytest.mark.skip(reason="temporarilly disabling")
def test_ec6():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    multicall_directories(path_name, False, validator=validate)


def test_validator():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/Promise_basic_functionality.js')
    value = validate(path_name)
    assert "drainMicroTasks" in value
