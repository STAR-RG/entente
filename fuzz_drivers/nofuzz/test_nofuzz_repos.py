import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants


def test_repos():
    path_name = os.path.join(constants.seeds_dir, 'repos')
    projects = [
        os.path.join(path_name, project_name)
        for project_name in os.listdir(path_name)
    ]
    for project_path in projects:
        multicall.multicall_directories(
            project_path, False, validator=validate
        )
