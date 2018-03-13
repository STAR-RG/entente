import pytest
import os
from regression_tests import callAll
from fuzzer.constants import seeds_dir

def test_max():
    pathName = os.path.join(seeds_dir, 'max.js')
    res = callAll(pathName)
    assert 67 == int(res.jsc_out)
    assert 67 == int(res.chakra_out)
    assert 67 == int(res.spiderm_out)
    assert 67 == int(res.v8_out)
