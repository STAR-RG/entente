from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer import radamsa_fuzzer

jerryjs_path = os.path.join(constants.seeds_dir, 'JerryJS')

@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryjs():
    path_name = os.path.join(jerryjs_path, 'ecma')
    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_jerryJS_regression():
    path_name = os.path.join(jerryjs_path, 'regression_edited')
    multicall.multicall_directories(path_name, True, validator=validate)

@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_jerry_debugger():
    path_name = os.path.join(jerryjs_path, 'debugger_edited')
    multicall.multicall_directories(path_name, True, validator=validate)
    
@pytest.mark.skip(reason="temporarilly disabling")                                
def test_fuzz_jerry_shell():
    path_name = os.path.join(jerryjs_path, 'debugger_edited/shell_files')
    multicall.multicall_directories(
        path_name, True, validator=validate,
        search_root=os.path.join(constants.seeds_dir, 'shell_files'),
        search_libfiles=['client_source.js']
    )