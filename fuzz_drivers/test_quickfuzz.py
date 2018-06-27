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

# @pytest.mark.skip(reason="temporarilly disabling")
def test_mutate_all():
    quantity = 1000
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
        os.path.join(constants.seeds_dir, 'mozilla/non262/Array/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/ArrayBuffer/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/arrow-functions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/async-functions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/AsyncGenerators/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Boolean/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/class/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/comprehensions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/DataView/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Date/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/destructuring/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Error/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/eval/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Exceptions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/execution-contexts/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/expressions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/extensions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Function/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/GC/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/generators/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/get-set/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/global/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Intl/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/iterable/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/jit/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/JSON/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/lexical/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/lexical-conventions/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/lexical-environment/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Map/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Math/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/misc/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/module/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Number/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/object/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/operators/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/pipeline/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Promise/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Proxy/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Reflect/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/reflect-parse/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/RegExp/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/regress/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Scope/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Script/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Set/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/SIMD/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/statements/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/strict/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/String/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Symbol/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/syntax/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/template-strings/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/TypedArray/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/TypedObject/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/types/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/Unicode/'),
        os.path.join(constants.seeds_dir, 'mozilla/non262/WeakMap/')
    ]

    for seed_path in seeds:
        q = Quickfuzz()
        try:
            q.mutate(seed_path, quantity) # generating N files for each seed
        except timeout_decorator.TimeoutError as e:
            print('something wrong happened:', str(e))
            continue

        if 'mozilla' in seed_path: # cannot run mozilla test with quickfuzz yet
            continue

        multicall.multicall_directories(q.outpath, False, validator=validate)


