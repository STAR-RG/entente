import shlex, subprocess
from fuzzer.constants import seeds_dir, rhino, javascriptcore, javascriptcore_lib_dir
import os

## this is a pytest test

def test_math_rhino():
    cmd_line = "java -jar " + rhino + " " + os.path.join(seeds_dir,'max.js')
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, err = p.communicate()
    assert int(out) == 67

def test_math_jsc():
    cmd_line = javascriptcore + " " + os.path.join(seeds_dir, 'max.js')
    args = shlex.split(cmd_line)
    os.environ['LD_LIBRARY_PATH'] = javascriptcore_lib_dir
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, err = p.communicate()
    assert int(out) == 67
    
