from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall

#@pytest.mark.skip(reason="temporarilly disabling")
def test_JSI():
    path_name = os.path.join(constants.seeds_dir, 'JSI')
    multicall.multicall_directories(path_name, False, validator=validate)