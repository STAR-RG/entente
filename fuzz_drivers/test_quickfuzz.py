from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer.quickfuzz_fuzzer import Quickfuzz
import timeout_decorator

@pytest.mark.skip(reason="temporarilly disabling")
def test_quickfuzz():
    """ this testcase generates X files via quickfuzz and run them """
    path_name = os.path.join(constants.seeds_dir, 'quickfuzz')
    quantity = 1000

    # generate grammar deps
    q = Quickfuzz()
    q.generate(quantity, path_name)

    multicall.multicall_directories(path_name, False, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_quickfuzz_radamsa():
    """ this testcase generates X files via quickfuzz and run them via radamsa """
    path_name = os.path.join(constants.seeds_dir, 'quickfuzz2')

    q = Quickfuzz()
    q.generate(1000, path_name)

    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_quickfuzz_mutate():
    seed_path = os.path.join(constants.seeds_dir, 'JerryJS', 'ecma')

    q = Quickfuzz()
    q.mutate(seed_path, 500)

    multicall.multicall_directories(q.outpath, False, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_mutate_all():
    quantity = 500
    seeds = [
        os.path.join(constants.seeds_dir, 'Tiny-js.tests'),
        os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6'),
        os.path.join(constants.seeds_dir, 'WebKit.JSTests.microbenchmarks'),
        os.path.join(constants.seeds_dir, 'DukTape', 'ecma_edited'),
        os.path.join(constants.seeds_dir, 'JerryJS', 'ecma'),
        os.path.join(constants.seeds_dir, 'JerryJS', 'debugger'),
        os.path.join(constants.seeds_dir, 'JerryJS', 'regression_edited'),
        os.path.join(constants.seeds_dir, 'JerryJS', 'debugger_edited', 'shell_files'),
        os.path.join(constants.seeds_dir, 'jsi.tests'),
        os.path.join(constants.seeds_dir, 'v8.test.benchmarks.data', 'kraken'),
        os.path.join(constants.seeds_dir, 'v8.test.benchmarks.data', 'sunspider'),
    ]

    for seed_path in seeds:
        q = Quickfuzz()
        try:
            q.mutate(seed_path, quantity) # generating N files for each seed
        except timeout_decorator.TimeoutError as e:
            print('something wrong happened:', str(e))
            continue

        multicall.multicall_directories(q.outpath, False, validator=validate)


