from tempfile import NamedTemporaryFile

from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer import radamsa_fuzzer
	
#@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryJS_regression():
    path_name = os.path.join(constants.seeds_dir, 'JerryJS/regression_suite')
    multicall.multicall_directories(path_name, True, validator=validate)