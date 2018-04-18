import tempfile, os, shutil, shlex, subprocess, ntpath, time, hashlib
from utils import constants, multicall
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed

def fuzz_file(num_iterations, file_path, mcalls, validator=None, libs=None):
    '''
        Call an external fuzzer (hardcoded with radamsa, for now) to fuzz/mutate 
        the input file (file_path) for a number of times (num_iterations). Each 
        time it makes a multicall on different engines. 
    '''
    widgets = ['fuzzing ' + file_path + ' ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ']
    bar = ProgressBar(widgets=widgets, max_value=num_iterations)
    #pylint: disable=W0612
    num_it = 1

    while num_it <= num_iterations:


        # fuzz the file with radamsa
        fuzzed_file_path = os.path.join(tempfile.gettempdir(), 'temp_filefuzzed')
        cmd = "radamsa --output {} {}".format(fuzzed_file_path, file_path)
        args = shlex.split(cmd)
        try:
            p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate()
        except FileNotFoundError as error:
            if 'radamsa' in str(error):
                raise Exception('Please check if radamsa is installed on your environment (see README.md file).')
        except Exception as error:
            raise Exception('Error:', error)

        # TODO: consider optimizing. This is taking a LOT of time, both parsing and validating. - Marcelo
        '''
            Check if file is valid and should be considered
        '''
        if validator is not None: 
            validation_error = validator(fuzzed_file_path)
            if validation_error:
                res = multicall.Results(fuzzed_file_path, validation_error)
                mcalls.notify(res)
                continue # skip this file

        # check discrepancy
        try:
            res = multicall.callAll(fuzzed_file_path)
            hash_object = hashlib.md5(str(time.time()).encode()).hexdigest()[:5]
            name = 'fuzzed_' + hash_object + '_' + ntpath.basename(file_path)
            res.path_name = os.path.join(constants.logs_dir, name)
            if mcalls.notify(res): # true if it is interesting and distinct. in this case, save the file
                ## get first name of file...
                shutil.copy(fuzzed_file_path, res.path_name)
        except UnicodeDecodeError as exc:
            # TODO: It is silly but we can't handle properly non-unicode outputs 
            # just because the .decode('utf-8') to convert bytes into strings 
            # raises this exception when the non-unicode char is mapped.
            continue

        bar.update(num_it)
        num_it += 1
    bar.finish()

if __name__ == "__main__":
    dir_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    # fuzz_dir(dir_path)