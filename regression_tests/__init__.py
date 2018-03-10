import shlex, subprocess
from fuzzer.constants import seeds_dir, rhino, javascriptcore, javascriptcore_lib_dir, chacra
import os

def callJSEngine(cmd_line):
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    return p.communicate()

def callRhino(funName):
    cmd_line = "java -jar " + rhino + " " + os.path.join(seeds_dir, funName)
    return callJSEngine(cmd_line)

def callJavaScriptCore(funName):
    cmd_line = javascriptcore + " " + os.path.join(seeds_dir, funName)
    os.environ['LD_LIBRARY_PATH'] = javascriptcore_lib_dir
    return callJSEngine(cmd_line)

def callChacra(funName):
    cmd_line = chacra + " " + os.path.join(seeds_dir, funName)
    return callJSEngine(cmd_line)

def callSpiderMonkey(funName):
    cmd_line = chacra + " " + os.path.join(seeds_dir, funName)
    return callJSEngine(cmd_line)