#https://github.com/Microsoft/ChakraCore/issues/4953
import os
from jsfuzz.utils import constants, multicall

def test_max():
    pathName = os.path.join(constants.seeds_dir, 'exercise_1/chakra_4953.js')
    res = multicall.callAll(pathName)
    print('\n', res)
