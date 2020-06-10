import shlex
import os
import hashlib
import logging
import signal
import re
import timeout_decorator
import multiprocessing
from subprocess import (
    STDOUT, check_output, CalledProcessError, getstatusoutput
)
from tempfile import mkstemp
from jsfuzz.utils import constants
from jsfuzz.utils.utils import remove_tmp_files, kill_processes
from jsfuzz.fuzzer.fuzzer import Fuzzer
from jsfuzz.utils.blacklist import (
    INVALID_STRINGS, REPORT_PASS_KEYWORDS, GLOBAL_HASH, SEED_INVALID
)

'''
    Class that saves state across several multicalls
'''


class Multicalls:

    def __init__(self, short_file_path, long_file_path):
        self.numskipped = 0
        self.hashmap = {}
        self.hits = 0
        self.numfiles = 0
        self.numwarnings = 0
        self.short_file_path = short_file_path
        self.long_file_path = long_file_path

    def notify(self, res):
        '''
            This function will be called multiple times. Statistics will
            be collected for these calls.
        '''
        self.numfiles += 1
        is_interesting_and_distinct = False
        # interesting if we find diverging responses
        if res.is_interesting():
            self.numwarnings += 1
            hashcode = res.hash()
            if hashcode in self.hashmap:
                self.hits += 1
                tests = self.hashmap[hashcode]
            else:
                is_interesting_and_distinct = True
                self.hashmap[hashcode] = tests = set()
            tests.add(res)
            with open(self.long_file_path, 'a+') as long_log:
                long_log.write(str(res))
            # all files with high priority is interesting
            if (res.priority() == '[HIGH]'):
                is_interesting_and_distinct = True
        elif res.is_invalid():
            self.numskipped += 1
        return is_interesting_and_distinct

    def save_summary(self, fuzzer=None):
        # generating log
        with open(self.short_file_path, 'w') as short_log:
            short_log.write(
                'number of files processed: {}\n'.format(self.numfiles))
            short_log.write(
                'number of warnings (interesting cases) observed: {}\n'.format(
                    self.numwarnings
                )
            )
            short_log.write(
                'number of invalid cases observed: {}\n'.format(
                        self.numskipped
                    )
                )
            short_log.write(
                'number of cache hits: {}\n'.format(self.hits))
            short_log.write(
                'number of buckets: {}\n'.format(len(self.hashmap)))

            # add engines version to the short_log
            versions = constants.get_versions()
            engines_versions = (
                'V8 {}\n' +
                'SpiderMonkey {}\n' +
                'JavascriptCore {}\n' +
                'Chakra {}\n' +
                'Hermes {}\n\n'
            ).format(versions['v8'], versions['sm'], versions['jsc'],
                     versions['ch'], versions['hermes'])
            short_log.write(
                '\nEngines Versions:\n{}'.format(engines_versions))
            short_log.write('fuzzer: {}\n'.format(fuzzer))

            # show contents associated with each bucket
            bucket_num = 0
            for key, val_set in self.hashmap.items():
                bucket_num += 1
                short_log.write(
                    '\n>>>>>\n files in bucket #{}:\n'.format(bucket_num)
                )
                bucket_files = []
                for res in val_set:
                    if res.path_name in bucket_files:
                        continue
                    is_file = os.path.isfile(res.path_name)
                    cp_file = ''
                    if is_file and 'fuzz' in res.path_name:
                        cp_file = ' (copied)'
                    short_log.write(' {}{}\n'.format(res.path_name, cp_file))
                    bucket_files.append(res.path_name)

                if key not in GLOBAL_HASH:
                    GLOBAL_HASH.append(key)
                    short_log.write('\nhash: {}\n'.format(key))
                else:
                    short_log.write('\nhash: {} (cached)\n'.format(key))

                res = next(iter(val_set))
                short_log.write('\npriority: {}\n'.format(res.priority()))
                short_log.write('\npattern:\n')
                short_log.write(res.str_canonical())


def multicall_directories(path_name, fuzzer=None, validator=None, shell=None):
    """
        Process files in a directory, running multicall on each file.

        :param path_name:
            path of the directory that contains the JS files
        :param fuzzer:
            to fuzzer a file you should set the fuzzer name
            (eg. radamsa, quickfuzz)
        :param shell:
            external lib file that should be included before run the test
        :param callable validator:
            function used to exclude files (e.g. parsing error).
            Calling the function on a valid file should return None/empty
            string; otherwise the reason for the error should be returned
            as a string.
        :param engines_version: dict that contains the engines versions
    """
    if not os.path.exists(path_name):
        raise Exception(
            'Cannot search *.js files in {}. '
            'Path does not exists.'.format(path_name)
        )

    if fuzzer and fuzzer not in ['radamsa', 'quickfuzz']:
        raise Exception('Error: Invalid fuzzer name')

    path_list = path_name.split('/')
    index = path_list.index('seeds') + 1

    fuzzed = fuzzer if fuzzer else 'nofuzz'
    name = '_'.join(path_list[index:])

    log_name_suffix = '_{}_diff_report_{}.txt'.format(fuzzed, name)

    if not os.path.isdir(constants.logs_dir):
        os.mkdir(constants.logs_dir)

    short_log_path = os.path.join(constants.logs_dir,
                                  'short{}'.format(log_name_suffix))
    long_log_path = os.path.join(constants.logs_dir,
                                 'long{}'.format(log_name_suffix))

    mcalls = Multicalls(short_log_path, long_log_path)

    if fuzzer:
        FUZZER = Fuzzer(fuzzer, mcalls, constants.num_iterations,
                        validator)

    # search for js files recursively in directory path name
    seeds = constants.scan_seeds(path_name)

    if shell:
        shell = constants.scan_seeds(path_name, shell=shell)

    size = len(seeds)

    for index, file_path in enumerate(seeds):
        filename = file_path.split('/seeds/')[-1]
        print(filename, index + 1, 'of', size)

        if fuzzer:
            try:
                FUZZER.fuzz_file(file_path, shell=shell)
            except Exception as e:
                # error raised by timeout decorator
                # import traceback
                # print(traceback.format_exc())
                logging.error('UNEXPECTED {}'.format(e))
                continue
        else:
            # run without fuzz
            res = callAll(file_path, shell=shell)
            mcalls.notify(res)

    mcalls.save_summary(fuzzer=fuzzer)
    remove_tmp_files()
    # store cache quickfuzz hash
    if fuzzer == 'quickfuzz' and constants.cache_quickfuzz:
        with open(constants.cache_quickfuzz[0], 'w') as doc:
            for i in FUZZER.cache:
                doc.write('{}\n'.format(i))


def get_valid_engines(path_name):
    """
        return the list of engines that could run a specific file (@path_name)
    """
    valid_engines = ['chakra', 'jsc', 'spidermonkey', 'v8', 'hermes']
    # get string after seeds/ pattern
    pattern = r"(?<=seeds\/).*$"
    regex = re.compile(pattern, re.IGNORECASE)
    name = regex.search(path_name).group()
    # check if engine should not ran this file
    if name in SEED_INVALID['chakra']:
        valid_engines.remove('chakra')
    elif name in SEED_INVALID['spidermonkey']:
        valid_engines.remove('spidermonkey')
    elif name in SEED_INVALID['jsc']:
        valid_engines.remove('jsc')
    elif name in SEED_INVALID['v8']:
        valid_engines.remove('v8')
    elif name in SEED_INVALID['hermes']:
        valid_engines.remove('hermes')

    return valid_engines


def to_one_file(path_name, shell):
    if not shell:
        return path_name

    fd, tmp_path = mkstemp(prefix='/tmp/temp_test', text=True)
    all_files = []
    all_files.append(shell)
    all_files.append(path_name)
    with open(fd, 'w', encoding='utf-8', errors='ignore') as outfile:
        for filename in all_files:
            with open(filename, encoding='utf-8', errors='ignore') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")
    return tmp_path


def callAll(path_name, validator=None, shell=None, eshost=True):
    '''
        This function calls all engines and returns a Results object
        encapsulating the output and error streams of corresponding calls
    '''
    if validator:
        res = Results(path_name, validator(path_name), eshost=eshost)
    else:
        res = Results(path_name, eshost=eshost)

    jsc_outerr, chakra_outerr = '', ''
    spidermonkey_outerr, v8_outerr = '', ''
    hermes_outerr = ''

    engines = [
        constants.javascriptcore,
        constants.v8,
        constants.spidermonkey,
        constants.chakra,
        constants.hermes
    ]

    # add all libs to one file if libs != None
    outputs = {
        'jsc': '',
        'v8': '',
        'sm': '',
        'ch': '',
        'hermes': '',
    }
    path_name = to_one_file(path_name, shell)
    try:
        outputs = fork_join_call(path_name, engines)
    except timeout_decorator.TimeoutError as e:
        outputs = {
            'jsc': 'timeout',
            'v8': 'timeout',
            'sm': 'timeout',
            'ch': 'timeout',
            'hermes': 'timeout',
        }

    jsc_outerr = outputs['jsc']
    v8_outerr = outputs['v8']
    chakra_outerr = outputs['ch']
    spidermonkey_outerr = outputs['sm']
    hermes_outerr = outputs['hermes']

    res.set_results({
        "jsc": jsc_outerr,
        "chakra": chakra_outerr,
        "spidermonkey": spidermonkey_outerr,
        "v8": v8_outerr,
        "hermes": hermes_outerr
    })

    return res


def callEngine(cmd_line, queue):
    output = callJSEngine(cmd_line)
    if 'jsvu/v8' in cmd_line:
        output = '$v8$' + output
    elif 'jsvu/ch' in cmd_line:
        output = '$ch$' + output
    elif 'jsvu/jsc' in cmd_line:
        output = '$jsc$' + output
    elif 'jsvu/sm' in cmd_line:
        output = '$sm$' + output
    elif 'jsvu/hermes' in cmd_line:
        output = '$hermes$' + output
    queue.put(output)


@timeout_decorator.timeout(constants.timeout_JS_engine)
def fork_join_call(path_name, engines):
    q = multiprocessing.Queue()
    number_processes = len(engines)
    cmd = ['{} {}'.format(engine, path_name) for engine in engines]
    ps = []
    outputs = {}
    try:
        for i in range(number_processes):
            p = multiprocessing.Process(
                target=callEngine,
                args=[cmd[i], q],
                name="Parallel process " + str(i)
            )
            p.daemon = True
            p.start()
            ps.append(p)
        for proc in ps:
            proc.join()
            out = q.get()
            if '$v8$' in out:
                outputs['v8'] = out.replace('$v8$', '')
            if '$sm$' in out:
                outputs['sm'] = out.replace('$sm$', '')
            if '$ch$' in out:
                outputs['ch'] = out.replace('$ch$', '')
            if '$jsc$' in out:
                outputs['jsc'] = out.replace('$jsc$', '')
            if '$hermes$' in out:
                outputs['hermes'] = out.replace('$hermes$', '')
    except timeout_decorator.TimeoutError as e:
        outputs = {
            'jsc': 'timeout',
            'v8': 'timeout',
            'sm': 'timeout',
            'ch': 'timeout',
            'hermes': 'timeout',
        }
    kill_processes()
    return outputs


@timeout_decorator.timeout(constants.timeout_JS_engine)
def call_cmd(cmd):
    msg = ''
    try:
        msg = check_output(cmd, stderr=STDOUT).decode('utf-8')
    except CalledProcessError as errorExc:
        try:
            msg = errorExc.output.decode('utf-8', errors='ignore')
        except:
            try:
                msg = errorExc.output.decode("utf-8", "replace")
            except:
                msg = errorExc.output
    return msg


@timeout_decorator.timeout(constants.timeout_JS_engine)
def callJSEngine(cmd_line, eshost=False):
    '''
        This function makes the system call to the JS engine binary
    '''
    if eshost:
        file = ''.join(cmd_line.split()[1:])
        cmd_line = 'eshost {}'.format(file)

    cmd = shlex.split(cmd_line)
    try:
        msg = call_cmd(cmd)
    except timeout_decorator.TimeoutError as e:
        msg = 'Error: TIMEOUT'

    if not msg:
        # double check to get unexpected behaviour
        status, error = getstatusoutput(cmd_line)
        if error:
            msg = 'Error: [CHECK_MANUALLY] {}'.format(error)
    return msg


def close_eshost(eshost):
    ''' close eshost connection (handle OSError for memory allocation) '''
    if not eshost:
        return
    pids = os.popen('ps ax | grep {} | grep -v grep | awk "{print $1}"')
    pids = [pid.strip() for pid in pids]
    for pid in pids:
        if pid:
            os.kill(int(pid), signal.SIGKILL)


class Results:
    """
        An object of this class encapsulates the results of multiple
        calls to JS engines. It is used, for example, to check if
        there is observed discrepancies across calls.
    """

    def __init__(self, path_name, validation_error=None, eshost=True):
        self.path_name = path_name
        self.validation_error = validation_error
        self.stack_traces = {'chakra': '', 'jsc': '', 'spidermonkey': '',
                             'v8': '', 'hermes': ''}
        self.jsc_outerr = None
        self.chakra_outerr = None
        self.spiderm_outerr = None
        self.v8_outerr = None
        self.hermes_outerr = None
        self.eshost = eshost

    def __str__(self):
        if self.validation_error:
            return "***  {path}\n    validation error: {error}\n".format(
                path=self.path_name, error=self.validation_error
            )
        else:
            return (
                """
                ***  {path}\n
                -------------JavaScriptCore\n{jsc}\n
                -------------Chakra\n{chakra}\n
                -------------SpiderMonkey\n{sm}\n
                -------------v8\n{v8}\n
                -------------hermes\n{hermes}\n
                """
            ).format(path=self.path_name, jsc=self.jsc_outerr,
                     chakra=self.chakra_outerr, sm=self.spiderm_outerr,
                     v8=self.v8_outerr, hermes=self.hermes_outerr)

    '''
        This string function abstract the parts of error messages
        related to the code that originated the error. This is
        important to identify duplicate errors.
    '''
    def str_canonical(self):
        if self.validation_error:
            return self.validation_error
        else:
            if self.eshost:
                return (
                    "-------------JavaScriptCore\n" +
                    self.jsc_outerr + "\n" +
                    "-------------Chakra\n" +
                    self.chakra_outerr + "\n" +
                    "-------------SpiderMonkey\n" +
                    self.spiderm_outerr + "\n" +
                    "-------------v8\n" +
                    self.v8_outerr + "\n" +
                    "-------------hermes\n" +
                    self.hermes_outerr + "\n"
                )
            else:
                return (
                    "-------------JavaScriptCore\n" +
                    self.abstract(self.jsc_outerr) + "\n" +
                    "-------------Chakra\n" +
                    self.abstract(self.chakra_outerr) + "\n" +
                    "-------------SpiderMonkey\n" +
                    self.abstract(self.spiderm_outerr) + "\n" +
                    "-------------v8\n" +
                    self.abstract(self.v8_outerr) + "\n" +
                    "-------------hermes\n" +
                    self.abstract(self.hermes_outerr) + "\n"
                )

    def abstract(self, string):
        error_message = ''
        for line in string.splitlines():
            if [invalid for invalid in REPORT_PASS_KEYWORDS if invalid in line]:
                break
            elif 'Error' in line:
                ind = line.index('Error')
                error_message = line[ind:] if 'Error' in line[ind:] else line
                break
            elif 'Fatal' in line:
                ind = string.index('Fatal')
                error_message = string[ind:]
                break
            elif 'Exception:' in line and 'Error' not in string:
                ind = line.index('Exception:')
                error_message = line[ind:] if 'Exception:' in line[ind:] else line
                break
            elif 'throw' in line and 'Error' not in string:
                ind = line.index('throw')
                error_message = string[ind:]
                break
            elif 'uncaught' in line and 'Error' not in string:
                ind = line.index('uncaught')
                error_message = string[ind:]
                break
            elif 'error:' in line:
                ind = line.index('error:')
                error_message = line[ind:]
                break
        return error_message

    def hash(self):
        bytes = self.str_canonical().encode()
        hash_object = hashlib.md5(bytes)
        return hash_object.hexdigest()

    def priority(self):
        """
        Define priority based on engine output
        """
        if self.is_high_priority():
            priority = '[HIGH]'
        else:
            priority = '[LOW]'
        return priority

    def is_high_priority(self):
        '''
            Check if a string is a warning with HIGH priority.
            We based on pattern on textual reports
        '''
        assert_patterns = [
            'failed',
            'Test',
            'assert',
            'expected',
            ' bad ',
            'Bad ',
            'Fail',
            'FAILED',
            'Crash',
            '0x',
            'segmentation',
            'fault'
        ]

        # check high priority by stack trace
        outputs = self.get_all_outerr(abstract=False)
        for output in outputs:
            if not output:
                continue
            # check if assert function appear in output
            lines = output.splitlines()
            for line in lines:
                for pattern in assert_patterns:
                    if pattern in line:
                        return True
        return False

    def is_interesting(self):
        '''
            This is the function that decides whether or not this result is
            interesting and should be reported.
        '''
        try:
            all_engines = all(self.get_all_outerr())
            is_fundamentally_interesting = (
                self.is_valid() and self.is_atleastone() and not all_engines
                and not self.is_only_timeout()
            )
            # necessary condition to be interesting
            if not is_fundamentally_interesting:
                return False

            return not self.is_spurious()
        except AttributeError:
            # TODO either add all missing attr. to the (invalidated) result or fix this
            return False

    def is_spurious(self):
        """
        Remove spurious reports based on keywords/strings
        TODO: updating strings in blacklist file
        """
        all_outputs = self.get_all_outerr()
        for engine_output in all_outputs:
            if 'Fatal' in engine_output or '[CHECK_MANUALLY]' in engine_output:
                return False

        # TODO: check better solution
        for engine_output in all_outputs:
            for keyword in INVALID_STRINGS:
                keyword = keyword.lower()
                if keyword in engine_output.lower():
                    return True
        return False

    def is_invalid(self):
        return self.validation_error

    def is_valid(self):
        return self.validation_error is None

    def is_atleastone(self):
        """
        Return True if at least one engine reports an error message
        """
        return any(self.get_all_outerr())

    def is_only_timeout(self):
        """
        Return True if all outputs have a timeout error message
        """
        outputs = self.get_all_outerr()
        len_outputs = len(outputs)
        len_timeouts = len(
            [output for output in outputs if 'TIMEOUT' in output]
        )
        len_empty = len([output for output in outputs if '' == output])

        return (
            len_timeouts == len_outputs or
            len_empty + len_timeouts == len_outputs
        )

    def get_all_outerr(self, abstract=True):
        """
        Return a list of all engines output errors
        """
        if abstract:
            return [
                self.abstract(output) for output in self.stack_traces.values()
            ]
        return [output for output in self.stack_traces.values()]

    # TODO generalize this stuff with a dict
    def set_results(self, results):
        if self.validation_error:
            return

        self.jsc_outerr = results['jsc']
        self.stack_traces['jsc'] = results['jsc']

        self.v8_outerr = results['v8']
        self.stack_traces['v8'] = results['v8']

        self.chakra_outerr = results['chakra']
        self.stack_traces['chakra'] = results['chakra']

        self.spiderm_outerr = results['spidermonkey']
        self.stack_traces['spidermonkey'] = results['spidermonkey']

        self.hermes_outerr = results['hermes']
        self.stack_traces['hermes'] = results['hermes']


if __name__ == "__main__":
    pass
