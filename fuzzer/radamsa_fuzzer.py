import jsparser, multicall, tempfile, constants, os, shutil, shlex, subprocess, progressbar, ntpath

## TODO: colocar arquivos de log em um mesmo diretorio, a ser criado dinamicamente se nao existir
## TODO: evitar escrita do arquivo de log se nao houver saida
## TODO: cache discrepancy -- one per type or error per file

num_iterations = 100

def fuzz_file(file_path):

    with open(os.path.join(constants.base_dir, ntpath.basename(file_path) + ".log"), "w") as logfile:
        bar = progressbar.ProgressBar()
        #pylint: disable=W0612
        print('fuzzing...' + file_path)
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
            (out, err) = p.communicate()
            if out!='' or err != '':
                raise EnvironmentError('problem accessing radamsa. check if you have radamsa installed.' + out + err)

            # check discrepancy
            res = multicall.callAll(fuzzed_file)
            if res.should_report():
                logfile.write(res.__str__())

def fuzz_dir (dir_path):

    for file_name in os.listdir(dir_path):
        fuzz_file(os.path.join(dir_path, file_name))

if __name__ == "__main__":
    dir_path = os.path.join(constants.seeds_dir, 'WebKit.JSTests.es6')
    fuzz_dir(dir_path)