import os
import pytest
from fuzz_drivers import *  #pylint: disable=W0614

from jsfuzz.fuzzer.validator import validate
from jsfuzz.utils import multicall, constants

v8_path = os.path.join(constants.seeds_dir, 'v8')
search_root = v8_path
search_libfiles = ['assert.js', 'base.js']

IGNORED_FILES = ['assert.js', 'utils.js', 'run.js']

data_kraken = [
    'ai-astar-data.js', 'audio-beat-detection-data.js',
    'audio-dft-data.js', 'audio-fft-data.js',
    'audio-oscillator-data.js', 'imaging-darkroom-data.js',
    'imaging-desaturate-data.js', 'stanford-crypto-aes-data.js',
    'stanford-crypto-ccm-data.js', 'json-parse-financial-data.js',
    'imaging-gaussian-blur-data.js', 'stanford-crypto-pbkdf2-data.js', 
    'json-stringify-tinderbox-data.js', 'stanford-crypto-sha256-iterative-data.js',
]


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_monorail():
    path_name = os.path.join(v8_path, 'monorail')
    multicall.multicall_directories(path_name, False, validator=validate)


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_kraken():
    path_name = os.path.join(v8_path, 'benchmarks/data/kraken')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        fuzzer=False, shell='kraken_shell.js'
    )


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_sunspider():
    path_name = os.path.join(v8_path, 'benchmarks/data/sunspider')
    multicall.multicall_directories(path_name, False, validator=validate)


# @pytest.mark.skip(reason="temporarilly disabling")
def test_fuzz_v8_octane():
    path_name = os.path.join(v8_path, 'benchmarks/data/octane')
    multicall.multicall_directories(
        path_name,
        validator=validate,
        fuzzer=False, shell='octane_shell.js'
    )
