import shlex, subprocess
from fuzzer.constants import seeds_dir, rhino, javascriptcore, javascriptcore_lib_dir, chacra, spidermonkey
import os

class JSEngineError(Exception):
    pass

def callAll(pathName):
    #@TODO use a proper exception type
    myset = set()
    out, err = callJavaScriptCore(pathName)
    if err is not '':
        raise JSEngineError(err)
    myset.add(out)
    out, err = callChacra(pathName)
    if err is not '':
        raise JSEngineError(err)
    myset.add(out)
    out, err = callSpiderMonkey(pathName)
    if err is not '':
        raise JSEngineError(err)
    myset.add(out)
    return myset

def callJSEngine(engine_name, cmd_line):
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()
#    print(engine_name)
#    print(out, err)
#    return (out, err)

def callRhino(pathName):
    cmd_line = "java -jar " + rhino + " " + pathName
    return callJSEngine('Rhino', cmd_line)

def callJavaScriptCore(pathName):
    cmd_line = javascriptcore + " " + pathName
    os.environ['LD_LIBRARY_PATH'] = javascriptcore_lib_dir
    return callJSEngine('JavaScriptCore', cmd_line)

def callChacra(pathName):
    cmd_line = chacra + " " + pathName
    return callJSEngine('Chacra', cmd_line)

def callSpiderMonkey(pathName):
    cmd_line = spidermonkey + " " + pathName
    return callJSEngine('SpiderMonkey', cmd_line)