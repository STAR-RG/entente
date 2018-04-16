from regression_tests import * #pylint: disable=W0614 
from utils import constants, multicall
from fuzzer.validator import validate


@pytest.mark.skip(reason="temporarilly disabling... checking issue")
def test_regexp_prototype():
    # https://github.com/Microsoft/ChakraCore/issues/578
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/Proxy_internal_get_calls_RegExp.prototype.test.js')
    res = multicall.callAll(path_name)
    #TODO: general advice: don't add print messages in tests. use assertions. - Marcelo
    print(res)

@pytest.mark.skip(reason="temporarilly disabling... checking issue")
def test_string_includes():
    # https://github.com/Microsoft/ChakraCore/issues/577
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/well-known_symbols_Symbol.match_String.prototype.includes.js')
    res = multicall.callAll(path_name)
    print('\n',res)

@pytest.mark.skip(reason="temporarilly disabling... checking issue")
def test_regexp_flags():
    # Object.getOwnPropertyDescriptor dont 
    # https://github.com/Microsoft/ChakraCore/issues/254
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/Proxy_internal_get_calls_RegExp.prototype.flags.js')
    res = multicall.callAll(path_name)
    print('\n',res)

def test_pad():
    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/String.prototype_methods_String.prototype.padEnd.js')
    res = multicall.callAll(path_name, validator=validate)
    assert "bad error:" in str(res)

    path_name = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/String.prototype_methods_String.prototype.padStart.js')
    res = multicall.callAll(path_name, validator=validate)
    assert "bad error:" in str(res)