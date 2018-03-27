import shlex, os, hashlib, ntpath
from subprocess import STDOUT, check_output, PIPE, CalledProcessError, TimeoutExpired
from utils import constants
from fuzzer import radamsa_fuzzer

'''
    Class that saves state across several multicalls
'''
class Multicalls:

    def __init__(self, long_file, short_file):
        self.hashmap = {}
        self.hits = 0
        self.numfiles = 0
        self.numwarnings = 0
        self.long_file = long_file
        self.short_file = short_file

    # This function will be called multiple times. Statistics will 
    # be collected for these calls.
    def notify(self, res):
        self.numfiles += 1
        if res.is_interesting(): # interesting if we find diverging responses
            self.numwarnings += 1
            hashcode = res.hash()
            if hashcode in self.hashmap:
                self.hits += 1
                tests = self.hashmap[hashcode]
            else:    
                self.hashmap[hashcode] = tests = set()
            tests.add(res)
            self.long_file.write(str(res))

    def save_summary(self):
        # generating log
        self.short_file.write('number of files processed: {}\n'.format(self.numfiles))
        self.short_file.write('number of warnings observed: {}\n'.format(self.numwarnings))
        self.short_file.write('number of cache hits: {}\n'.format(self.hits))
        self.short_file.write('number of buckets: {}\n'.format(len(self.hashmap)))
        # show contents associated with each bucket        
        bucket_num = 0
        #pylint: disable=W0612
        for key, val_set in self.hashmap.items():
            bucket_num += 1
            self.short_file.write('\n>>>>> files in bucket #{}:\n'.format(bucket_num))
            for res in val_set:
                self.short_file.write(' ' + res.path_name + "\n" )
            self.short_file.write('\npattern:\n')
            res = next(iter(val_set))
            self.short_file.write(res.str_canonical())


'''
    Process files in a directory, running multicall on each file.
'''
def multicall_directories(path_name, should_fuzz):
    name = ntpath.basename(path_name)

    log_name_suffix = ('fuzz' if should_fuzz else '') + '_diff_report' + name + '.txt'
    
    with open(os.path.join(constants.logs_dir, 'short' + log_name_suffix), 'w') as short_file, \
        open(os.path.join(constants.logs_dir, 'long'+ log_name_suffix), 'w') as long_file:

        mcalls = Multicalls(long_file, short_file) 

        # multicall JS engines on each file
        for file_name in os.listdir(path_name):
            file_path = os.path.join(path_name, file_name)
            print('testing file {}'.format(file_path))
            if should_fuzz:
                radamsa_fuzzer.fuzz_file(constants.num_iterations, file_path, mcalls)
            else:
                res = callAll(file_path)
                mcalls.notify(res)

        mcalls.save_summary()

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
        "-------------JavaScriptCore\n" + 
        self.jsc_outerr + "\n" +
        "-------------Chakra\n" + 
        self.chakra_outerr + "\n" +
        "-------------SpiderMonkey\n" + 
        self.spiderm_outerr + "\n" +
        "-------------v8\n" + 
        self.v8_outerr + "\n")

    '''
        This string function abstract the parts of error messages 
        related to the code that originated the error. This is 
        important to identify duplicate errors.
    '''
    def str_canonical(self):
        return (
        "-------------JavaScriptCore\n" + 
        self.abstract(self.jsc_outerr) + "\n" +
        "-------------Chakra\n" + 
        self.abstract(self.chakra_outerr) + "\n" +
        "-------------SpiderMonkey\n" + 
        self.abstract(self.spiderm_outerr) + "\n" +
        "-------------v8\n" + 
        self.abstract(self.v8_outerr) + "\n")

    def abstract(self, str):
        for line in str.splitlines():
            if 'Error' in line:
                ind = str.index('Error')
                return line[ind:] # shows what comes after Error
        return ''                

    def hash(self):
        bytes = self.str_canonical().encode()
        hash_object = hashlib.md5(bytes)
        return hash_object.hexdigest()
    
    # def update_counters(self, counters):
    #     output = 'output_and_error: '
    #     output += 'N' if not self.jsc_outerr else "Y"
    #     output += 'N' if not self.chakra_outerr else "Y"
    #     output += 'N' if not self.spiderm_outerr else "Y"
    #     output += 'N' if not self.v8_outerr else "Y"
    #     counters[output] = counters.get(output, 0) + 1
        
    def is_interesting(self):
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
    res = callAll(os.path.join(constants.seeds_dir, 'max.js'))
    print (res)