import tempfile, os, shutil, shlex, subprocess, progressbar, ntpath
from utils import constants, multicall

## TODO: cache discrepancy -- one per type or error per file

num_iterations = 10

def fuzz_file(file_path):

    with open(os.path.join(constants.logs_dir, "all.log"), "w") as generallog_file_object:
        generallog_file_object.write(file_path + "\n")
        bar = progressbar.ProgressBar()
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
            except UnicodeDecodeError as exc:
                # TODO: It is silly but we can't handle properly non-unicode outputs 
                # just because the .decode('utf-8') to convert bytes into strings 
                # raises this exception when the non-unicode char is mapped.
                continue

            if res.is_interesting():
                # create log dir if it does not exist
                if not os.path.exists(constants.logs_dir):
                    os.makedirs(constants.logs_dir)  
                # create log file as there is something to report
                with open(os.path.join(constants.logs_dir, ntpath.basename(file_path) + ".log"), "w") as logfile:
                    logfile.write('original: ' + file_path + '\n')
                    with open(file_path, "r") as file_object:
                        logfile.write(file_object.read())
                    logfile.write('*** modified: ' + fuzzed_file + '\n')
                    with open(fuzzed_file, "r") as file_object:
                        try:
                            logfile.write(file_object.read())
                        except UnicodeDecodeError as exc:
                            logfile.write('Could not print fuzzed file because it contains non-utf-8 chars!' )
                    logfile.write(res.__str__())

def fuzz_dir (dir_path):

    for file_name in os.listdir(dir_path):
        fuzz_file(os.path.join(dir_path, file_name))

if __name__ == "__main__":
    dir_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    fuzz_dir(dir_path)