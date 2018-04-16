from regression_tests import * #pylint: disable=W0614 
from utils import constants, multicall
from fuzzer.validator import validate

def test_max():
    pathName = os.path.join(constants.seeds_dir, 'max.js')
    res = multicall.callAll(pathName)
    assert 67 == int(res.jsc_outerr)
    assert 67 == int(res.chakra_outerr)
    assert 67 == int(res.spiderm_outerr)
    assert 67 == int(res.v8_outerr)

def test_validator():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/Promise_basic_functionality.js')
    value = validate(path_name)
    assert "drainMicroTasks" in value

# Run test without fuzzing
@pytest.mark.skip(reason="temporarilly disabling")
def test_webkit():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    multicall.multicall_directories(path_name, False, validator=validate)    