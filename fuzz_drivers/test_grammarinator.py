from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer.grammarinator_fuzzer import Grammarinator

ECMASCRIPT_GRAMMAR = os.path.join(constants.fuzzers_dir, 'grammarinator_deps', 'ECMAScriptGrammar.g4')
JS_GRAMMAR = [
    os.path.join(constants.fuzzers_dir, 'grammarinator_deps', 'JavaScriptLexer.g4'),
    os.path.join(constants.fuzzers_dir, 'grammarinator_deps', 'JavaScriptParser.g4')
]

@pytest.mark.skip(reason="temporarilly disabling")
def test_grammarinator():
    path_name = os.path.join(constants.seeds_dir, 'grammarinator')

    # generate grammar deps
    g = Grammarinator(ECMASCRIPT_GRAMMAR, single_grammar=True)
    # generate 50 js files with distincts depths (10, 20, ..., 100)
    for i in range(10, 101, 10):
        g.run_grammarinator(path_name, number_of_testcases=50, depths=i)

    multicall.multicall_directories(path_name, False, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_grammarinator_without_validation():
    path_name = os.path.join(constants.seeds_dir, 'grammarinator')

    # generate grammar deps
    g = Grammarinator(ECMASCRIPT_GRAMMAR, single_grammar=True)
    
    # generate 1000 files without validation
    g.run_grammarinator(path_name, number_of_testcases=1000, depths=20, validation=False)

    multicall.multicall_directories(path_name, False, validator=validate)