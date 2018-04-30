from tests import *
from jsfuzz.utils import constants, multicall
from jsfuzz.fuzzer.validator import validate

@pytest.mark.skip(reason="")
def test_exercise_1():
    path_name = os.path.join(constants.seeds_dir, 'exercise_1')
    multicall.multicall_directories(path_name, False, validator=validate)