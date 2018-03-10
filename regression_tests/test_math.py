import pytest

from regression_tests import (callChacra, callJavaScriptCore, callRhino,
                              callSpiderMonkey)

## pytest test

def callAll(name):
    #@TODO use a proper exception type
    myset = set()
    out, err = callRhino(name)
    if err is not None:
        raise NameError(type(err))
    myset.add(out)
    out, err = callJavaScriptCore(name)
    if err is not None:
        raise NameError(type(err))
    myset.add(out)
    out, err = callChacra(name)
    if err is not None:
        raise NameError(type(err))
    myset.add(out)
    out, err = callJavaScriptCore(name)
    if err is not None:
        raise NameError(type(err))
    myset.add(out)
    return myset

def test_max():
    myset = callAll('max.js')
    assert len(myset) == 1
    assert 67 == int(myset.pop())

@pytest.mark.skip(reason="no way of currently testing this")
def test_urlconnection():
    myset = callAll('urlconnection.js')
    assert len(myset) == 1
