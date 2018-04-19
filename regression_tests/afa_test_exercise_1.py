#https://github.com/Microsoft/ChakraCore/issues/4953
from regression_tests import * 
from utils import constants, multicall

def test_max():
    pathName = os.path.join(constants.seeds_dir, 'exercise_1/chakra_3407.js')
    res = multicall.callAll(pathName)
    print('\n', res)
