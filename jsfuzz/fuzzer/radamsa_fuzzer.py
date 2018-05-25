import tempfile, os, shutil, shlex, subprocess, ntpath, timeout_decorator, re, logging, datetime
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed

from jsfuzz.utils import constants, multicall

@timeout_decorator.timeout(1)
def validate_wrapper(validator, fuzzed_file_path):
    return validator(fuzzed_file_path)

@timeout_decorator.timeout(2)
def call_engines(fuzzed_file_path, libs):
    return multicall.callAll(fuzzed_file_path, libs=libs)

# @timeout_decorator.timeout(10) # change this value if you want to wait more or less time to run this method
def fuzz_file(num_iterations, file_path, mcalls, validator=None, libs=None):
    '''
        Call an external fuzzer (hardcoded with radamsa, for now) to fuzz/mutate 
        the input file (file_path) for a number of times (num_iterations). Each 
        time it makes a multicall on different engines. 
    '''
    
    widgets = ['fuzzing ' + file_path + ' ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ']
    bar = ProgressBar(widgets=widgets, maxval=num_iterations).start()
    logging.debug('fuzzing %s', file_path)

    #pylint: disable=W0612
    num_it = 0
    num_unsuccessful_iterations = 0
    num_consecutive_unsuccessful_iterations = 0
    while num_it < num_iterations:
        
        logging.debug('num_successful_iterations %s', str(num_it))
        logging.debug('num_unsuccessful_iterations %s', str(num_unsuccessful_iterations))

        if num_unsuccessful_iterations > (2 * num_iterations) or num_consecutive_unsuccessful_iterations == constants.limit_num_consecutive_unsuccessful_iterations:
            logging.debug('   hit max number of unsuccessful iterations or max number of consecutive unsuccessful iterations (%s,%s,%s,%s)', num_iterations, num_consecutive_unsuccessful_iterations, num_unsuccessful_iterations, num_it)
            break # quit this file

        # fuzz the file with radamsa
        fuzzed_file_path = os.path.join(tempfile.gettempdir(), 'temp_filefuzzed')
        cmd = "radamsa --output {} {}".format(fuzzed_file_path, file_path)
        args = shlex.split(cmd)
        try:
            logging.debug('starting radamsa %s', datetime.datetime.now().isoformat())
            p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate()
        except Exception as error:
            raise Exception('Error:', error)
        finally:
            logging.debug('done radamsa %s', datetime.datetime.now().isoformat())
        
        '''
            Check if file is valid and should be considered

            # TODO: consider optimizing. This is taking a LOT of time, both parsing and validating. - Marcelo
        '''
        try:
            logging.debug('start validation %s', datetime.datetime.now().isoformat())
            if validator is not None:
                try:
                    validation_error = validate_wrapper(validator, fuzzed_file_path)
                    if validation_error:
                        res = multicall.Results(fuzzed_file_path, validation_error)
                        mcalls.notify(res)
                        num_unsuccessful_iterations += 1
                        num_consecutive_unsuccessful_iterations += 1
                        continue # skip this file
                except timeout_decorator.TimeoutError as e: # error raised by timeout decorator
                    logging.debug('timeout while validating.. %s', str(e))
                    num_unsuccessful_iterations += 1
                    num_consecutive_unsuccessful_iterations += 1
                    continue

        finally:
            logging.debug('done validation %s', datetime.datetime.now().isoformat())

        # check discrepancy
        try:
            logging.debug('start calling engines %s', datetime.datetime.now().isoformat())
            res = call_engines(fuzzed_file_path, libs=libs)
            path_list = file_path.split('/')
            index = path_list.index('seeds') + 1
            name = 'fuzzed_' + '_'.join(path_list[index:])
            res.path_name = os.path.join(constants.logs_dir, name)
            if mcalls.notify(res): # true if it is interesting and distinct. in this case, save the file
                
                # one file can be involved in more than one bucket
                # we can rename it with "_1_.js, _2_.js..."
                if os.path.isfile(res.path_name):
                    filename = res.path_name.split('/')[-1]
                    pattern = r"\_\d{1,2}\_.+js" # check files which endswith pattern '_Integer_.js'
                    jsfiles = [jsfile for jsfile in os.listdir(constants.logs_dir) if re.sub(pattern,'.js', jsfile) == filename]
                    count = len(jsfiles) + 1
                    res.path_name = res.path_name.replace('.js', '_{}_.js'.format(count))
                
                shutil.copy(fuzzed_file_path, res.path_name)
        except UnicodeDecodeError as exc:
            # TODO: It is silly but we can't handle properly non-unicode outputs 
            # just because the .decode('utf-8') to convert bytes into strings 
            # raises this exception when the non-unicode char is mapped.
            num_unsuccessful_iterations += 1
            num_consecutive_unsuccessful_iterations += 1
            continue
        except timeout_decorator.TimeoutError as e: # error raised by timeout decorator
            logging.debug('timeout while calling engines.. %s', str(e))
            num_unsuccessful_iterations += 1
            num_consecutive_unsuccessful_iterations += 1
            continue
        finally:
            logging.debug('done calling engines %s', datetime.datetime.now().isoformat())

        # successful iteration
        num_it += 1 
        num_consecutive_unsuccessful_iterations = 0
        bar.update(num_it) 
        
    bar.finish()
    logging.debug('done fuzzing %s', file_path)

if __name__ == "__main__":
    dir_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    # fuzz_dir(dir_path)