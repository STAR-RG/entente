from regression_tests import *  #pylint: disable=W0614
from fuzzer.validator import validate
from tempfile import NamedTemporaryFile
from utils import multicall
from fuzzer import radamsa_fuzzer

def test_fuzz_invalid(): # expect no raised exception
    with NamedTemporaryFile(mode='wt', delete=False) as short_file, NamedTemporaryFile(mode='wt', delete=False) as long_file:
        mcalls = multicall.Multicalls(long_file, short_file) 
        file_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/well-known_symbols_Symbol.replace.js')
        radamsa_fuzzer.fuzz_file(constants.num_iterations, file_path, mcalls, validate)
        mcalls.save_summary()

@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_webkit():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    multicall.multicall_directories(path_name, True, validator=validate)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8():
    path_name = os.path.join(constants.seeds_dir, 'v8.test.benchmarks.data/kraken')
    multicall.multicall_directories(path_name, True, validator=validate)
#@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryjs():
    path_name = os.path.join(constants.seeds_dir, 'JerryJS.jerryjs.ecma')
    multicall.multicall_directories(path_name, True, validator=validate)