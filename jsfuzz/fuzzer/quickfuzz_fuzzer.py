import os, shlex, logging, shutil, hashlib, timeout_decorator
from subprocess import call, PIPE, Popen, check_output
from jsfuzz.utils import constants, blacklist
from jsfuzz.fuzzer import validator
from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed

class Quickfuzz:
    def __init__(self):
        self.widgets = [
            'Generating new seeds with QuickFuzz ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' '
        ]
        self.progress_bar = ProgressBar(widgets=self.widgets)
        self.outpath = None

    def generate(self, quantity, outdir):
        """ Generate N files via JS grammar with quickfuzz """
        if not os.path.exists(outdir+'/tmp'):
            os.makedirs(outdir+'/tmp')

        tmp_path = os.path.join(outdir, 'tmp')
        process_cmd = """
        quickfuzz gen js -l 1 -u 20 -q 100 -o {}
        """.format(tmp_path)
        args = shlex.split(process_cmd)

        valid_inputs = 0
        self.progress_bar.max_value = quantity
        self.progress_bar.start()
        try:
            while valid_inputs < quantity:
                call(args)
                for filename in os.listdir(tmp_path):
                    filepath = os.path.join(outdir, tmp_path, filename)
                    if not validator.validate(filepath):
                        new_filename = outdir + '/test_{}.js'.format(valid_inputs)
                        if not os.path.exists(new_filename):
                            shutil.copy(filepath, new_filename)
                            valid_inputs += 1
                            self.progress_bar.update(valid_inputs)
                            if valid_inputs == quantity:
                                break
                
                shutil.rmtree(tmp_path)
        except Exception as e:
            shutil.rmtree(outdir)
            raise Exception("Fail when try to validate quickfuzz tests. Error: ", e)
        self.progress_bar.finish()

    @timeout_decorator.timeout(60)
    def mutate(self, seed_dir, quantity):
        process_cmd = """
        quickfuzz muttest js "cat @@" {} -v -t 1 -l 1 -u 3 -q 1 -o {}
        """
        quickfuzz_path = constants.quickfuzz_dir
        seed_name = os.path.basename(seed_dir) if not seed_dir.endswith('/') else os.path.basename(seed_dir[:-1])

        if not os.path.exists(os.path.join(quickfuzz_path, seed_name)):
            os.mkdir(os.path.join(quickfuzz_path, seed_name))
        
        self.outpath = os.path.join(quickfuzz_path, seed_name)

        valid_files = 0
        pattern = 'test.js'
        self.progress_bar.max_value = quantity
        while valid_files < quantity:
            tmp_filepath = os.path.join(self.outpath, pattern)
            args = shlex.split(process_cmd.format(seed_dir, quickfuzz_path))
            pipe = Popen(args, stdout=PIPE)
            output = pipe.communicate()[0]
            with open(tmp_filepath, 'w') as tmp_file:
                try:
                    # removing invalid chars
                    output = str(output, 'utf-8')
                    index = output.index('\x1b')
                    output = output[0:index]
                    tmp_file.write(output)
                except UnicodeDecodeError:
                    continue

            if not validator.validate(tmp_filepath):
                try:
                    self.call_file(tmp_filepath)
                except timeout_decorator.TimeoutError:
                    continue

                with open(tmp_filepath) as tmp:
                    _hash = hashlib.md5(tmp.read().encode()).hexdigest()
                    _file = os.path.join(self.outpath, 'test_{}.js'.format(_hash))
                    if not os.path.exists(_file):
                        shutil.copy(tmp_filepath, _file)
                        valid_files += 1
                        self.progress_bar.update(valid_files)
        
        os.remove(tmp_filepath)
        self.progress_bar.finish()
    
    @timeout_decorator.timeout(15)
    def call_file(self, jspath):
        """ 
            this function checks if there is an infinite loop on file
        """
        call([constants.v8, jspath], stdout=PIPE)
        