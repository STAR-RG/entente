from tempfile import NamedTemporaryFile

from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall
from jsfuzz.fuzzer import radamsa_fuzzer

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_arguments_access_inner():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-arguments-access-inner.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_arguments_caller():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-arguments-caller.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_array_proto_sort_comparefn():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-array-proto-sort-comparefn.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_array_write_invalid_length():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-array-write-invalid-length.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)


#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_array_push_maxlen():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-array-push-maxlen.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_arraybuffer_defineproperty():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-arraybuffer-defineproperty.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_arraybuffer_proto_properties():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-arraybuffer-proto-properties.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)


#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_dataview_constructor_plainbuf():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-dataview-constructor-plainbuf.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_bruteforce_conv():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-bruteforce-conv.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_canceling():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-canceling.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)


#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_instance():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-instance.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)


#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_midnigth_1970():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-midnight-1970.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)


#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_no_fracs():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-no-fracs.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)


#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_prototype_toprimitive():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-prototype-toprimitive.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_timeclip_zero():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-timeclip-zero.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_utc_custom():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-utc-custom.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_error_constructor():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-error-constructor.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_error_prototype():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-error-prototype.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_function_constructor_oneline_comment():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-function-constructor-oneline-comment.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_arguments_binding():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-arguments-binding.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bi_date_now():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bi-date-now.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bug_arridx_1():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bug-arridx-1.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_bug_bound_constructable_judofyr():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-bug-bound-constructable-judofyr.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_var_decl_same_name_value():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-var-decl-same-name-value.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_assign_eval_order_1():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-assign-eval-order-1.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_ttest_dev_assign_eval_order_2():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/ttest-dev-assign-eval-order-2.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_assign_eval_order_3():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-assign-eval-order-3.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_Test_dev_assign_eval_order_4():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/Test-dev-assign-eval-order-4.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_bufferobject_index_wrap():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-bufferobject-index-wrap.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_Test_dev_builtin_func_protos():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/Test-dev-builtin-func-protos.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_catch_binding():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-catch-binding.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_Test_dev_ctrl_with_binding():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/Test-dev-ctrl-with-binding.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_Test_dev_define_properties_1():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/Test-dev-define-properties-1.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_directive_prologue():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-directive-prologue.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_func_length_prop():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-func-length-prop.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_func_own_name_ref():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-func-own-name-ref.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_func_own_name_ref():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-func-own-name-ref.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)

#@pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_duktape_test_dev_lnot():
    path_name = os.path.join(constants.seeds_dir, 'DukTape.ecma/test-dev-lnot.js')
    # multicall.multicall_directories(path_name, True, validator=validate)    
    res = multicall.callAll(path_name)
    print(res)
