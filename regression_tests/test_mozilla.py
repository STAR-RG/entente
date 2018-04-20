import os
from utils import constants, multicall
from fuzzer.validator import validate_mozilla
from regression_tests import *  #pylint: disable=W0614

# changes done on support libs:
#  - made uneval() throw an error (non262/shell.js)
#
# see https://chromium.googlesource.com/v8/v8.git/+/6.8.40/test/mozilla/mozilla.status
# for test compatibility details for v8

# remaining test suites to add
# test262 (standard stuff, should be easier)

# ignored for now
# non262/extensions (lots of mozilla-specific stuff)
IGNORED_FILES = {"browser.js", "shell.js", "template.js", "user.js", "js-test-driver-begin.js", "js-test-driver-end.js"}

def test_fuzz_mozilla_non262_Array():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Array/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_ArrayBuffer():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/ArrayBuffer/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_arrowfunctions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/arrow-functions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_asyncfunctions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/async-functions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_AsyncGenerators():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/AsyncGenerators/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Boolean():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Boolean/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_class():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/class/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_comprehensions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/comprehensions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_DataView():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/DataView/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Date():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Date/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_destructuring():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/destructuring/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Error():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Error/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_eval():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/eval/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Exceptions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Exceptions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_executioncontexts():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/execution-contexts/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_expressions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/expressions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_extensions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/extensions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Function():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Function/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_GC():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/GC/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_generators():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/generators/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_getset():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/get-set/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_global():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/global/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Intl():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Intl/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_iterable():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/iterable/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_jit():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/jit/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_JSON():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/JSON/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_lexical():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/lexical/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_lexicalconventions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/lexical-conventions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_lexicalenvironment():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/lexical-environment/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Map():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Map/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Math():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Math/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_misc():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/misc/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_module():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/module/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Number():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Number/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_object():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/object/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_operators():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/operators/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_pipeline():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/pipeline/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Promise():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Promise/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Proxy():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Proxy/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Reflect():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Reflect/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_reflectparse():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/reflect-parse/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_RegExp():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/RegExp/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_regress():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/regress/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Scope():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Scope/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Script():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Script/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Set():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Set/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_SIMD():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/SIMD/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_statements():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/statements/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_strict():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/strict/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_String():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/String/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Symbol():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Symbol/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_syntax():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/syntax/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_templatestrings():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/template-strings/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_TypedArray():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/TypedArray/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_TypedObject():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/TypedObject/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_types():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/types/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_Unicode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Unicode/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_non262_WeakMap():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/WeakMap/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)

def test_fuzz_mozilla_test262_annexB_builtins():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Array():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Array/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_ArrayBuffer():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/ArrayBuffer/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_ArrayIteratorPrototype():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/ArrayIteratorPrototype/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_AsyncFunction():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/AsyncFunction/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Atomics():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Atomics/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_BigInt():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/BigInt/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Boolean():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Boolean/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_DataView():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/DataView/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Date():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Date/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_decodeURI():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/decodeURI/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_decodeURIComponent():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/decodeURIComponent/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_encodeURI():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/encodeURI/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_encodeURIComponent():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/encodeURIComponent/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Error():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Error/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_eval():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/eval/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Function():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Function/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_GeneratorFunction():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/GeneratorFunction/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_GeneratorPrototype():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/GeneratorPrototype/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_global():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/global/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Infinity():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Infinity/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_isFinite():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/isFinite/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_isNaN():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/isNaN/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_IteratorPrototype():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/IteratorPrototype/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_JSON():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/JSON/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Map():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Map/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_MapIteratorPrototype():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/MapIteratorPrototype/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Math():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Math/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_NaN():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/NaN/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_NativeErrors():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/NativeErrors/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Number():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Number/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Object():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Object/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_parseFloat():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/parseFloat/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_parseInt():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/parseInt/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Promise():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Promise/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Proxy():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Proxy/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Reflect():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Reflect/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_RegExp():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/RegExp/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Set():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Set/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_SetIteratorPrototype():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/SetIteratorPrototype/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_SharedArrayBuffer():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/SharedArrayBuffer/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_String():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/String/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_StringIteratorPrototype():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/StringIteratorPrototype/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_Symbol():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/Symbol/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_ThrowTypeError():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/ThrowTypeError/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_TypedArray():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/TypedArray/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_TypedArrays():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/TypedArrays/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_undefined():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/undefined/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_WeakMap():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/WeakMap/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_builtins_WeakSet():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/built-ins/WeakSet/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_Collator():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/Collator/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_Date():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/Date/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_DateTimeFormat():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/DateTimeFormat/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_Intl():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/Intl/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_Number():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/Number/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_NumberFormat():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/NumberFormat/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_PluralRules():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/PluralRules/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_intl402_String():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/intl402/String/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_argumentsobject():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/arguments-object/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_asi():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/asi/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_blockscope():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/block-scope/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_comments():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/comments/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_computed_property_names():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/computed-property-names/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_destructuring():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/destructuring/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_directiveprologue():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/directive-prologue/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_evalcode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/eval-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_export():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/export/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_expressions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/expressions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_functioncode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/function-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_futurereserved_words():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/future-reserved-words/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_globalcode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/global-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_identifierresolution():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/identifier-resolution/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_identifiers():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/identifiers/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_import():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/import/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_keywords():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/keywords/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_lineterminators():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/line-terminators/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_literals():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/literals/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_modulecode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/module-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_punctuators():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/punctuators/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_reservedwords():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/reserved-words/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_restparameters():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/rest-parameters/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_sourcetext():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/source-text/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_statements():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/statements/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_types():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/types/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_language_whitespace():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/language/white-space/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_harness():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/harness/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_local():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/local/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_Date():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/Date/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_escape():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/escape/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_Function():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/Function/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_Object():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/Object/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_RegExp():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/RegExp/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_String():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/String/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_builtins_unescape():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/built-ins/unescape/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_comments():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/comments/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_evalcode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/eval-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_expressions():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/expressions/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_functioncode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/function-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_globalcode():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/global-code/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_literals():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/literals/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


def test_fuzz_mozilla_test262_annexB_language_statements():
    path_name = os.path.join(constants.seeds_dir, 'mozilla/test262/annexB/language/statements/')
    multicall.multicall_directories(path_name, True, validator=validate_mozilla,
                                    search_root=os.path.join(constants.seeds_dir, 'mozilla'),
                                    search_libfiles=['shell.js'],
                                    ignored_files=IGNORED_FILES)


