import shlex, subprocess
from fuzzer.constants import seeds_dir, rhino, javascriptcore, javascriptcore_lib_dir, chacra
import os

## this is a pytest test

def callJSEngine(cmd_line):
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    return p.communicate()

def test_math_rhino():
    cmd_line = "java -jar " + rhino + " " + os.path.join(seeds_dir,'max.js')
    out, err = callJSEngine(cmd_line)
    assert int(out) == 67

def test_math_jsc():
    cmd_line = javascriptcore + " " + os.path.join(seeds_dir, 'max.js')
    os.environ['LD_LIBRARY_PATH'] = javascriptcore_lib_dir
    out, err = callJSEngine(cmd_line)
    assert int(out) == 67
    
def test_math_chacra():
    cmd_line = chacra + " " + os.path.join(seeds_dir, 'max.js')
    out, err = callJSEngine(cmd_line)
    assert int(out) == 67