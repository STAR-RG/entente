import tempfile, os, shutil, shlex, subprocess, progressbar, ntpath
from utils import constants, multicall

'''
    Call an external fuzzer (hardcoded with radamsa, for now) to fuzz/mutate 
    the input file (file_path) for a number of times (num_iterations). Each 
    time it makes a multicall on different engines. 
'''
def fuzz_file(num_iterations, file_path, mcalls):
    bar = progressbar.ProgressBar()
    bar.start()
    #pylint: disable=W0612
    for num_it in bar(range(1, num_iterations+1)):
        # copy original file to temporary directory
        temp_dir = tempfile.gettempdir()
        temp_file_name = 'temp_file'
        temp_path = os.path.join(temp_dir, temp_file_name)
        shutil.copy2(file_path, temp_path)

        # fuzz the file with radamsa
        fuzzed_file = os.path.join(temp_dir, temp_file_name + 'fuzzed')
        args = shlex.split("radamsa " + "--output " + fuzzed_file + " " + temp_path)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()

        # check discrepancy
        try:
            res = multicall.callAll(fuzzed_file)
            mcalls.notify(res)
            bar.update()
        except UnicodeDecodeError as exc:
            # TODO: It is silly but we can't handle properly non-unicode outputs 
            # just because the .decode('utf-8') to convert bytes into strings 
            # raises this exception when the non-unicode char is mapped.
            continue

if __name__ == "__main__":
    dir_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    # fuzz_dir(dir_path)