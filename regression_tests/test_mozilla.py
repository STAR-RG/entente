import os
from utils import constants, multicall
from fuzzer.validator import validate_mozilla


def test_fuzz_mozilla_non262_Array():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Array')
    libs = [os.path.join(constants.seeds_dir, 'mozilla/browser.js'),
            os.path.join(constants.seeds_dir, 'mozilla/shell.js')]
    multicall.multicall_directories(path_name, True, validator=validate_mozilla, libs=libs,
                                    search_libfiles=['browser.js', 'shell.js'])


def test_fuzz_mozilla_non262_Math():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Math')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'])
