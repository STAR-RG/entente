from regression_tests import *

def test_max():
    pathName = os.path.join(constants.seeds_dir, 'max.js')
    res = multicall.callAll(pathName)
    assert 67 == int(res.jsc_out)
    assert 67 == int(res.chakra_out)
    assert 67 == int(res.spiderm_out)
    assert 67 == int(res.v8_out)
