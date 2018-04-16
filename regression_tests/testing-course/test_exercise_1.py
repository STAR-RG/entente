from regression_tests import *
from utils import constants, multicall
from fuzzer.validator import validate

@pytest.mark.skip(reason="")
def test_exercise_1():
    path_name = os.path.join(constants.seeds_dir, 'exercise_1')
    multicall.multicall_directories(path_name, False, validator=validate)