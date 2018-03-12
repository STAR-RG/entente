import shlex, subprocess
from fuzzer.constants import seeds_dir, rhino, javascriptcore, javascriptcore_lib_dir, chacra, spidermonkey
import os

'''
    This function calls all engines and returns a Results 
    objects encapsulating output and error streams of 
    corresponding calls
'''
def callAll(pathName):
    res = Results(pathName)
    # JavaScriptCore
    out, err = callJavaScriptCore(pathName)
    res.set_jsc_results(out, err)
    # Chacra
    out, err = callChacra(pathName)
    res.set_chacra_results(out, err)
    # SpiderMonkey
    out, err = callSpiderMonkey(pathName)
    res.set_spiderm_results(out, err)
    return res

def callJSEngine(engine_name, cmd_line):
    args = shlex.split(cmd_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()

'''
    not using this engine
'''
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
        "Chacra" + 
        self.chacra_out + "\n" +
        self.chacra_err + "\n" +
        "-------------" +
        "SpiderMonkey" + 
        self.spiderm_out + "\n" +
        self.spiderm_err + "\n")
    
    def update_counters(self, counters):
        output = 'output_'
        output += 'N' if self.jsc_out == '' else "Y"
        output += 'N' if self.chacra_out == '' else "Y"
        output += 'N' if self.spiderm_out == '' else "Y"
        counters[output] = counters.get(output, 0) + 1
        error = 'error_'
        error += 'N' if self.jsc_err == '' else "Y"
        error += 'N' if self.chacra_err == '' else "Y"
        error += 'N' if self.spiderm_err == '' else "Y"
        counters[error] = counters.get(error, 0) + 1
        
    def should_report(self):
        contains_report_in_jsc = self.jsc_out != '' or self.jsc_err != ''
        contains_report_in_chacra = self.chacra_out != '' or self.chacra_err != ''
        contains_report_in_spiderm = self.spiderm_out != '' or self.spiderm_err != ''
        atleastone = contains_report_in_jsc or contains_report_in_chacra or contains_report_in_spiderm
        all = contains_report_in_jsc and contains_report_in_chacra and contains_report_in_spiderm
        return atleastone and not all

    def set_jsc_results(self, out, err):
        self.jsc_out = out
        self.jsc_err = err

    def set_chacra_results(self, out, err):
        self.chacra_out = out
        self.chacra_err = err

    def set_spiderm_results(self, out, err):
        self.spiderm_out = out
        self.spiderm_err = err