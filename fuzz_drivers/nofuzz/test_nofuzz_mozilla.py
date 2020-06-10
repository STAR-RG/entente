import os

from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate_mozilla
from jsfuzz.utils import constants, multicall

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


#@pytest.mark.skip(reason="temporarilly disabling")
def test_mozilla_non262():
    path_name = os.path.join(constants.seeds_dir, 'mozilla')
    multicall.multicall_directories(
        path_name,
        validator=validate_mozilla,
        shell='shell.js'
    )


# def test_fuzz_mozilla_non262_Array():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Array/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_ArrayBuffer():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/ArrayBuffer/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_arrowfunctions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/arrow-functions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_asyncfunctions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/async-functions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_AsyncGenerators():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/AsyncGenerators/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Boolean():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Boolean/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_class():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/class/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_comprehensions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/comprehensions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_DataView():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/DataView/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Date():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Date/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_destructuring():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/destructuring/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Error():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Error/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_eval():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/eval/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Exceptions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Exceptions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_executioncontexts():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/execution-contexts/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_expressions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/expressions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_extensions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/extensions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Function():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Function/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_GC():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/GC/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_generators():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/generators/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_getset():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/get-set/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_global():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/global/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Intl():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Intl/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_iterable():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/iterable/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_jit():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/jit/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_JSON():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/JSON/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_lexical():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/lexical/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_lexicalconventions():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/lexical-conventions/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_lexicalenvironment():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/lexical-environment/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Map():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Map/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Math():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Math/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_misc():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/misc/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_module():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/module/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Number():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Number/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_object():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/object/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_operators():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/operators/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_pipeline():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/pipeline/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Promise():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Promise/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Proxy():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Proxy/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Reflect():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Reflect/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_reflectparse():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/reflect-parse/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_RegExp():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/RegExp/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_regress():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/regress/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Scope():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Scope/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Script():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Script/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Set():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Set/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_SIMD():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/SIMD/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_statements():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/statements/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_strict():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/strict/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_String():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/String/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Symbol():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Symbol/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_syntax():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/syntax/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_templatestrings():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/template-strings/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_TypedArray():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/TypedArray/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_TypedObject():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/TypedObject/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_types():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/types/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_Unicode():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/Unicode/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)


# def test_fuzz_mozilla_non262_WeakMap():
#     path_name = os.path.join(constants.seeds_dir, 'mozilla/non262/WeakMap/')
#     multicall.multicall_directories(path_name, False, validator=validate_mozilla,
#                                     search_root=os.path.join(constants.seeds_dir, 'mozilla'),
#                                     search_libfiles=['shell.js'],
#                                     ignored_files=IGNORED_FILES)
