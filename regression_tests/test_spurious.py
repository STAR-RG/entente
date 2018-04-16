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
    file_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/well-known_symbols_Symbol.match_String.prototype.includes.js')
    res = multicall.callAll(file_path)
    print('\n',res)

@pytest.mark.skip(reason="temporarilly disabling... checking issue")
def test_regexp_flags():
    # Object.getOwnPropertyDescriptor invalid 
    # https://github.com/Microsoft/ChakraCore/issues/254
    file_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/Proxy_internal_get_calls_RegExp.prototype.flags.js')
    res = multicall.callAll(file_path)
    print('\n',res)

@pytest.mark.skip(reason="temporarilly disabling... checking issue")
def test_array_prototype_values():
    # Array.prototype.values not yet implemented on v8
    file_path = os.path.join(constants.logs_dir, 'fuzzed_Array.prototype_methods_Array.prototype.values.js')
    res = multicall.callAll(file_path)
    print('\n',res)

@pytest.mark.skip(reason="")
def test_pad():
    file_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/String.prototype_methods_String.prototype.padEnd.js')
    res = multicall.callAll(file_path)
    assert "bad error:" in str(res)

    file_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6/String.prototype_methods_String.prototype.padStart.js')
    res = multicall.callAll(file_path)
    assert "bad error:" in str(res)

@pytest.mark.skip(reason="")
def test_t():
    file_path = os.path.join(constants.logs_dir, 'fuzzed_Symbol_typeof_support.js')
    res = multicall.callAll(file_path)
    print('\n', res)
    # assert 'handle files without method reference' in str(res)