import shlex, os
from subprocess import STDOUT, check_output, PIPE, CalledProcessError, TimeoutExpired
from fuzzer import constants

'''
    This function calls all engines and returns a Results object (see class below) 
    encapsulating the output and error streams of corresponding calls
'''
def callAll(pathName):
    res = Results(pathName)
    # JavaScriptCore
    outerr = callJavaScriptCore(pathName)
    res.set_jsc_results(outerr)
    # Chakra
    outerr = callChakra(pathName)
    res.set_chakra_results(outerr)
    # SpiderMonkey
    outerr = callSpiderMonkey(pathName)
    res.set_spiderm_results(outerr)
    # v8
    outerr = callV8(pathName)
    res.set_v8_results(outerr)

    return res

'''
    This function makes the system call to the JS engine binary
'''
def callJSEngine(cmd_line):
    cmd = shlex.split(cmd_line)
    #pylint: disable=W0612
    try:
        # Using Python3 API because of the timeout, which appears to be 
        # essential as I found a case of hang
        msg = check_output(cmd, stderr=STDOUT, timeout=1).decode('utf-8')
    except CalledProcessError as errorExc:
        msg = errorExc.output.decode('utf-8')
    except TimeoutExpired as timeoutExc:
        msg = 'TIMEOUT'
    return msg

def callJavaScriptCore(pathName):
    cmd_line = constants.javascriptcore + " " + pathName
    #os.environ['LD_LIBRARY_PATH'] = constants.javascriptcore_lib_dir
    return callJSEngine(cmd_line)

def callChakra(pathName):
    cmd_line = constants.chakra + " " + pathName
    return callJSEngine(cmd_line)

def callSpiderMonkey(pathName):
    cmd_line = constants.spidermonkey + " " + pathName
    return callJSEngine(cmd_line)

def callV8(pathName):
    cmd_line = constants.v8 + " " + pathName
    return callJSEngine(cmd_line)

'''
    An object of this class encapsulates the results of multiple 
    calls to JS engines. It is used, for example, to check if 
    there is observed discrepancies across calls.
'''
class Results:
    def __init__(self, path_name):
        self.path_name = path_name

    def __str__(self):
        return ("***  " + self.path_name + "\n" 
        "-------------" +
        "JavaScriptCore" + 
        self.jsc_outerr + "\n" +
        "-------------" +
        "Chakra" + 
        self.chakra_outerr + "\n" +
        "-------------" +
        "SpiderMonkey" + 
        self.spiderm_outerr + "\n" +
        "-------------" +
        "v8" + 
        self.v8_outerr + "\n")
    
    def update_counters(self, counters):
        output = 'output_and_error: '
        output += 'N' if not self.jsc_outerr else "Y"
        output += 'N' if not self.chakra_outerr else "Y"
        output += 'N' if not self.spiderm_outerr else "Y"
        output += 'N' if not self.v8_outerr else "Y"
        counters[output] = counters.get(output, 0) + 1
        
    def should_report(self):
        atleastone = self.jsc_outerr or self.chakra_outerr or self.spiderm_outerr or self.v8_outerr
        all = self.jsc_outerr and self.chakra_outerr and self.spiderm_outerr and self.v8_outerr
        return atleastone and not all

    def set_jsc_results(self, outerr):
        self.jsc_outerr = outerr

    def set_chakra_results(self, outerr):
        self.chakra_outerr = outerr

    def set_spiderm_results(self, outerr):
        self.spiderm_outerr = outerr

    def set_v8_results(self, outerr):
        self.v8_outerr = outerr

if __name__ == "__main__":
    # example
    callAll(os.path.join(constants.seeds_dir, 'max.js'))