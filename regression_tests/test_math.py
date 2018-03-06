import shlex, subprocess
from fuzzer.constants import seeds_dir, rhino_path
import os

## this is a pytest test

def test_math_rhino():
    cmd_line = "java -jar " + rhino_path + " " + os.path.join(seeds_dir,'max.js')
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, err = p.communicate()
    assert int(out) == 67
