import shlex, subprocess
import constants
import os

'''
    This function calls all engines and returns a Results 
    objects encapsulating output and error streams of 
    corresponding calls
'''
enable_v8 = False

def callAll(pathName):
    res = Results(pathName)
    # JavaScriptCore
    out, err = callJavaScriptCore(pathName)
    res.set_jsc_results(out, err)
    # Chakra
    out, err = callChakra(pathName)
    res.set_chakra_results(out, err)
    # SpiderMonkey
    out, err = callSpiderMonkey(pathName)
    res.set_spiderm_results(out, err)
    # v8
    if enable_v8:
        out, err = callV8(pathName)
        res.set_v8_results(out, err)

    return res

def callJSEngine(engine_name, cmd_line):
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()

'''
    not using this engine
'''
def callRhino(pathName):
    cmd_line = "java -jar " + constants.rhino + " " + pathName
    return callJSEngine('Rhino', cmd_line)

def callJavaScriptCore(pathName):
    cmd_line = constants.javascriptcore + " " + pathName
    os.environ['LD_LIBRARY_PATH'] = constants.javascriptcore_lib_dir
    return callJSEngine('JavaScriptCore', cmd_line)

def callChakra(pathName):
    cmd_line = constants.chakra + " " + pathName
    return callJSEngine('Chakra', cmd_line)

def callSpiderMonkey(pathName):
    cmd_line = constants.spidermonkey + " " + pathName
    return callJSEngine('SpiderMonkey', cmd_line)

def callV8(pathName):
    cmd_line = constants.v8 + " " + pathName
    return callJSEngine('v8', cmd_line)

class Results:
    def __init__(self, path_name):
        self.path_name = path_name

    def __str__(self):
        return ("***  " + self.path_name + "\n" 
        "-------------" +
        "JavaScriptCore" + 
        self.jsc_out + "\n" +
        self.jsc_err + "\n" +
        "-------------" +
        "Chakra" + 
        self.chakra_out + "\n" +
        self.chakra_err + "\n" +
        "-------------" +
        "SpiderMonkey" + 
        self.spiderm_out + "\n" +
        self.spiderm_err + "\n" +
        "-------------" +
        "v8" + 
        self.v8_out + "\n" +
        self.v8_err + "\n")
    
    def update_counters(self, counters):
        output = 'output_'
        output += 'N' if self.jsc_out == '' else "Y"
        output += 'N' if self.chakra_out == '' else "Y"
        output += 'N' if self.spiderm_out == '' else "Y"
        output += 'N' if self.v8_out == '' else "Y"
        counters[output] = counters.get(output, 0) + 1
        error = 'error_'
        error += 'N' if self.jsc_err == '' else "Y"
        error += 'N' if self.chakra_err == '' else "Y"
        error += 'N' if self.spiderm_err == '' else "Y"
        error += 'N' if self.v8_err == '' else "Y"
        counters[error] = counters.get(error, 0) + 1
        
    def should_report(self):
        contains_report_in_jsc = self.jsc_out != '' or self.jsc_err != ''
        contains_report_in_chakra = self.chakra_out != '' or self.chakra_err != ''
        contains_report_in_spiderm = self.spiderm_out != '' or self.spiderm_err != ''
        contains_report_in_v8 = self.v8_out != '' or self.v8_err != ''
        atleastone = contains_report_in_jsc or contains_report_in_chakra or contains_report_in_spiderm or contains_report_in_v8
        all = contains_report_in_jsc and contains_report_in_chakra and contains_report_in_spiderm and contains_report_in_v8
        return atleastone and not all

    def set_jsc_results(self, out, err):
        self.jsc_out = out
        self.jsc_err = err

    def set_chakra_results(self, out, err):
        self.chakra_out = out
        self.chakra_err = err

    def set_spiderm_results(self, out, err):
        self.spiderm_out = out
        self.spiderm_err = err

    def set_v8_results(self, out, err):
        self.v8_out = out
        self.v8_err = err
