import shlex, os, hashlib, ntpath
from subprocess import STDOUT, check_output, PIPE, CalledProcessError, TimeoutExpired
from utils import constants
from fuzzer import radamsa_fuzzer

'''
    Class that saves state across several multicalls
'''
class Multicalls:

    def __init__(self, long_file, short_file):
        self.numskipped = 0
        self.hashmap = {}
        self.hits = 0
        self.numfiles = 0
        self.numwarnings = 0
        self.long_file = long_file
        self.short_file = short_file

    def notify(self, res):
        ''' 
            This function will be called multiple times. Statistics will 
            be collected for these calls.
        ''' 
        self.numfiles += 1
        is_interesting_and_distinct = False
        if res.is_interesting(): # interesting if we find diverging responses
            self.numwarnings += 1
            hashcode = res.hash()
            if hashcode in self.hashmap:
                self.hits += 1
                tests = self.hashmap[hashcode]
            else:
                is_interesting_and_distinct = True
                self.hashmap[hashcode] = tests = set()
            tests.add(res)
            self.long_file.write(str(res))
        elif res.is_invalid():
            self.numskipped += 1
        return is_interesting_and_distinct

    def save_summary(self):
        # generating log
        self.short_file.write('number of files processed: {}\n'.format(self.numfiles))
        self.short_file.write('number of warnings (interesting cases) observed: {}\n'.format(self.numwarnings))
        self.short_file.write('number of invalid cases observed: {}\n'.format(self.numskipped))
        self.short_file.write('number of cache hits: {}\n'.format(self.hits))
        self.short_file.write('number of buckets: {}\n'.format(len(self.hashmap)))
        # show contents associated with each bucket        
        bucket_num = 0
        for key, val_set in self.hashmap.items():
            bucket_num += 1
            self.short_file.write('\n>>>>>\n files in bucket #{}:\n'.format(bucket_num))
            for res in val_set:
                self.short_file.write(' ' + res.path_name + "\n" )
            self.short_file.write('\nhash: {}\n'.format(key))
            self.short_file.write('\npattern:\n')
            res = next(iter(val_set))
            self.short_file.write(res.str_canonical())


def multicall_directories(path_name, should_fuzz, validator=None):
    """
        Process files in a directory, running multicall on each file.

        :param callable validator: Function used to exclude files (e.g. parsing error). Calling the function on a valid
        file should return None/empty string; otherwise the reason for the error should be returned as a string.

    """
    name = ntpath.basename(path_name)

    log_name_suffix = ('fuzz' if should_fuzz else '') + '_diff_report_' + name + '.txt'

    if not os.path.isdir(constants.logs_dir):
        os.mkdir(constants.logs_dir)

    short_log_path = os.path.join(constants.logs_dir, 'short' + log_name_suffix)
    long_log_path = os.path.join(constants.logs_dir, 'long' + log_name_suffix)
    
    with open(short_log_path, 'w') as short_file, open(long_log_path, 'w') as long_file:
        mcalls = Multicalls(long_file, short_file) 

        # multicall JS engines on each file
        for file_name in os.listdir(path_name):
            file_path = os.path.join(path_name, file_name)

            #TODO: Please check. consider removing this code. I think this only makes sense to be called insider fuzzers, which is done already. -Marcelo
            if validator is not None:
                validation_error = validator(file_path)
                if validation_error:
                    res = Results(file_path, validation_error)
                    mcalls.notify(res)
                    continue # skip this file

            if should_fuzz:
                radamsa_fuzzer.fuzz_file(constants.num_iterations, file_path, mcalls, validator)
            else:
                res = callAll(file_path)
                mcalls.notify(res)

        mcalls.save_summary()


def callAll(pathName):
    '''
        This function calls all engines and returns a Results object (see class below) 
        encapsulating the output and error streams of corresponding calls
    '''
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


def callJSEngine(cmd_line):
    '''
        This function makes the system call to the JS engine binary
    '''
    cmd = shlex.split(cmd_line)
    #pylint: disable=W0612
    try:
        # Using Python3 API because of the timeout, which appears to be 
        # essential. I found a case of hang
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

class Results:
    """
        An object of this class encapsulates the results of multiple
        calls to JS engines. It is used, for example, to check if
        there is observed discrepancies across calls.
    """

    def __init__(self, path_name, validation_error=None):
        self.path_name = path_name
        self.validation_error = validation_error

    def __str__(self):
        if self.validation_error:
            return "***  {path}\n    validation error: {error}\n".format(path=self.path_name,error=self.validation_error)
        else:
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
        if self.validation_error:
            return self.validation_error
        else:
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

    def is_interesting(self):
        try:
            atleastone = self.jsc_outerr or self.chakra_outerr or self.spiderm_outerr or self.v8_outerr
            all = self.jsc_outerr and self.chakra_outerr and self.spiderm_outerr and self.v8_outerr
            return self.validation_error is None and atleastone and not all
        except AttributeError:  # TODO either add all missing attr. to the (invalidated) result or fix this
            return False

    def is_invalid(self):
        return self.validation_error

    # TODO generalize this stuff with a dict

    def set_jsc_results(self, outerr):
        assert not self.validation_error
        self.jsc_outerr = outerr

    def set_chakra_results(self, outerr):
        assert not self.validation_error
        self.chakra_outerr = outerr

    def set_spiderm_results(self, outerr):
        assert not self.validation_error
        self.spiderm_outerr = outerr

    def set_v8_results(self, outerr):
        assert not self.validation_error
        self.v8_outerr = outerr


if __name__ == "__main__":
    # example
    res = callAll(os.path.join(constants.seeds_dir, 'max.js'))
    print (res)
