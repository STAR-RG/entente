from tempfile import NamedTemporaryFile

from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer import radamsa_fuzzer

@pytest.mark.skip(reason="temporarilly disabling")
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

@pytest.mark.skip(reason="temporarilly disabling")
def test_tinyjs():
    path_name = os.path.join(constants.seeds_dir, 'Tiny-js.tests')
    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryjs():
    path_name = os.path.join(constants.seeds_dir, 'JerryJS/jerryjs.ecma')
    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_webkit_benchmarks():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.microbenchmarks')
    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_kraken():
    path_name = os.path.join(constants.seeds_dir, 'v8.test.benchmarks.data/kraken')
    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_sunspider():
    path_name = os.path.join(constants.seeds_dir, 'v8.test.benchmarks.data/sunspider')
    multicall.multicall_directories(path_name, True, validator=validate)    

