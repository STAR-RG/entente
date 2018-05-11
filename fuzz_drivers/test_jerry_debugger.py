import os
from utils import constants, multicall
from fuzzer.validator import *
from regression_tests import * 


@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_jerry_debugger():
    path_name = os.path.join(constants.seeds_dir, 'JerryJS/debugger/baac')
    multicall.multicall_directories(path_name, True, validator=validate)
    
@pytest.mark.skip(reason="temporarilly disabling")                                
def test_fuzz_jerry_shell():
    path_name = os.path.join(constants.seeds_dir, 'JerryJS/debugger/baac/shell_files')
    multicall.multicall_directories(path_name, True, validator=validate),
    								search_root=os.path.join(constants.seeds_dir, 'baac'),
                                    search_libfiles=['client_source.js']