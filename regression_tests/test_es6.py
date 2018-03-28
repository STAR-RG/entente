from regression_tests import * #pylint: disable=W0614 
from utils import constants, multicall
from fuzzer.validator import validate

#@pytest.mark.skip(reason="temporarilly disabling")
def test_ec6():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    multicall.multicall_directories(path_name, False, validator=validate)

def test_validator():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/Promise_basic_functionality.js')
    value = validate(path_name)
    assert "drainMicroTasks" in value
