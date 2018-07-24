from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_full():
    path_name = os.path.join(constants.seeds_dir, 'DukTape/ecmascript')
    multicall.multicall_directories(path_name, True, validator=validate)