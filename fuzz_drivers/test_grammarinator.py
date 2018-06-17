from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer import grammarinator_fuzzer

@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_grammarinator():
    path_name = os.path.join(constants.seeds_dir, 'grammarinator')
    grammarinator_fuzzer.run_grammarinator(path_name, validate)

    multicall.multicall_directories(path_name, False, validator=validate)