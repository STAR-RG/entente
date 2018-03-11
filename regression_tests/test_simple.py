import pytest
import os
from regression_tests import callAll
from fuzzer.constants import seeds_dir

def test_max():
    pathName = os.path.join(seeds_dir, 'max.js')
    myset = callAll(pathName)
    assert len(myset) == 1
    assert 67 == int(myset.pop())

@pytest.mark.skip(reason="no way of currently testing this")
def test_urlconnection():
    myset = callAll('urlconnection.js')
    assert len(myset) == 1