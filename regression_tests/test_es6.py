import os 
from os import listdir
from os.path import isfile, join
from fuzzer.constants import js_dir
from regression_tests import callJavaScriptCore

def test_ec6():
    pathName = os.path.join(js_dir, 'WebKit/JSTests/es6')
    for fileName in listdir(pathName):
        myset = callJavaScriptCore(os.path.join(pathName, fileName))
        print fileName
        assert len(myset) == 1