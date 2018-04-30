import os

from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.utils import constants, multicall
from jsfuzz.fuzzer.validator import validate_mozilla

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


