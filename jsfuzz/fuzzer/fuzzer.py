import timeout_decorator
import logging
import os
import tempfile
import shlex
import datetime
import shutil
import re
from subprocess import Popen, PIPE
from jsfuzz.utils import constants, multicall, utils
from progressbar import (
    ProgressBar, Percentage, Bar, RotatingMarker, ETA
)


def radamsa(fuzzed_file_path, file_path):
    """
    """
    cmd = "radamsa --output {} {}".format(fuzzed_file_path, file_path)
    try:
        logging.debug('starting radamsa %s',
                      datetime.datetime.now().isoformat())
        args = shlex.split(cmd)
        p = Popen(args, stdout=PIPE, stderr=PIPE)
        p.communicate()
    except Exception as error:
        raise Exception('Unexpected Error from radamsa:', error)
    finally:
        logging.debug('done radamsa %s', datetime.datetime.now().isoformat())


def quickfuzz(fuzzed_file_path, file_path, cache=None):
    """
    quickfuzz muttest js "cat @@" INPUT -v -t 1 -l 1 -u 10 -q 1 -o {} -s {}
    args:
        muttest: mutation using input files inside a directory
        js: generation type (javascript grammar)
        "cat @@": a hard-coded way to get all fuzzed files
        INPUT: path to JS files input (muttest fuzz by folder not by each file)
        -v: activate verbose to show the fuzzed file content
        -t: timeout
        -l and -u: lower and higher bits to fuzzing
        -q: quantity
        -o: output
    """
    # quickfuzz use a directory as input, we need to save each file
    # in our seed in a temp folder and run quickfuzz in that folder
    tmp_folder = os.path.join(tempfile.gettempdir(), 'tmp_quickfuzz')
    if not os.path.exists(tmp_folder):
        os.mkdir(tmp_folder)
    # copy the path_file to tmp_folder
    shutil.copy(file_path, os.path.join(tmp_folder, 'test.js'))
    cmd = '{} muttest js "cat @@" {} -v -t 1 -l 1 -u 10 -q 1 -o {}'.format(
        constants.quickfuzz,
        tmp_folder,
        tempfile.gettempdir()
    )

    try:
        logging.debug(
            'starting quickfuzz %s',
            datetime.datetime.now().isoformat()
        )
        args = shlex.split(cmd)
        p = Popen(args, stdout=PIPE, stderr=PIPE)
        # we need to get the quickfuzz console output
        # (we use cat @@ to print the content in console)
        output = p.communicate()[0]
    except Exception as error:
        raise Exception('Unexpected Error from quickfuzz:', error)

    # saving the output in the fuzzed_file_path
    with open(fuzzed_file_path, 'w') as tmp_file:
        logging.debug('saving in...%s', fuzzed_file_path)
        # removing invalid chars
        output = str(output, 'utf-8')
        index = output.index('\x1b')
        output = output[0:index]
        id_output = utils.string_to_hash(output)
        if id_output in cache:
            raise Exception('cache hit')
        cache.add(id_output)
        tmp_file.write(output)
    logging.debug('done quickfuzz %s', datetime.datetime.now().isoformat())


class Fuzzer:
    def __init__(self, fuzzer, mcalls, total_it, validator=None):
        self.fuzzer = fuzzer
        self.mcalls = mcalls
        self.total_it = total_it
        self.validator = validator
        self.cache = set({})

    def init_cache(self):
        cache_file = constants.cache_quickfuzz
        if cache_file:
            with open(cache_file[0]) as doc:
                for x in doc.readlines():
                    x = x.strip()
                    self.cache.add(str(x))

    @timeout_decorator.timeout(1)
    def validate_wrapper(self, validator, fuzzed_file_path):
        return validator(fuzzed_file_path)

    @timeout_decorator.timeout(3)
    def call_engines(self, fuzzed_file_path, shell):
        # return multicall_v2.callAll(fuzzed_file_path, shell=shell)
        return multicall.callAll(fuzzed_file_path, shell=shell)

    def progress_bar(self, file_path, iterations):
        widgets = ['fuzzing ' + file_path + ' ', Percentage(), ' ',
                   Bar(marker=RotatingMarker()), ' ', ETA(), ' ']
        return ProgressBar(widgets=widgets, maxval=iterations)

    def is_valid(self, fuzzed_file_path):
        """
        Check if file is valid and should be considered
        """
        logging.debug('start validation %s',
                      datetime.datetime.now().isoformat())
        is_valid = False
        validation_error = None
        try:
            validation_error = self.validate_wrapper(self.validator,
                                                     fuzzed_file_path)
            if validation_error:
                # res = multicall_v2.Results(fuzzed_file_path, validation_error)
                res = multicall.Results(fuzzed_file_path, validation_error)
                self.mcalls.notify(res)
                self.num_unsuccessful_it += 1
                self.num_consecutive_unsuccessful_it += 1
            else:
                is_valid = True
        except timeout_decorator.TimeoutError as e:
            # error raised by timeout decorator
            logging.debug('timeout while validating.. %s', str(e))
            self.num_unsuccessful_it += 1
            self.num_consecutive_unsuccessful_it += 1
        return is_valid

    def reach_unsuccessful_iterations(self):
        reached = False
        if self.num_unsuccessful_it > (2 * self.total_it):
            logging.debug('   hit max number of unsuccessful iterations')
            reached = True
        if (
            self.num_consecutive_unsuccessful_it ==
            constants.limit_num_consecutive_unsuccessful_iterations
        ):
            logging.debug(
                '   hit max number of consecutive unsuccessful iterations'
            )
            reached = True
        return reached

    def is_discrepant(self, file_path, fuzzed_file_path, shell=None):
        res = self.call_engines(fuzzed_file_path, shell=shell)
        path_list = file_path.split('/')
        index = path_list.index('seeds') + 1
        name = 'fuzzed_{}_{}'.format(self.fuzzer, '_'.join(path_list[index:]))
        res.path_name = os.path.join(constants.logs_dir, name)
        if self.mcalls.notify(res):
            self.saving_file(res, fuzzed_file_path)
            shutil.copy(fuzzed_file_path, res.path_name)

    def saving_file(self, res, fuzzed_file_path):
        # Saving file if it is interesting and distinct
        if os.path.isfile(res.path_name):
            filename = res.path_name.split('/')[-1]
            pattern = r"\_\d{1,2}\_.+js"
            jsfiles = [
                jsfile for jsfile in os.listdir(constants.logs_dir)
                if re.sub(pattern, '.js', jsfile) == filename
            ]
            count = len(jsfiles) + 1
            res.path_name = res.path_name.replace(
                '.js',
                '_{}_.js'.format(count)
            )

    def fuzz_file(self, file_path, shell=None):
        if self.fuzzer == 'quickfuzz' and not self.cache:
            self.init_cache()

        bar = self.progress_bar(file_path, self.total_it)
        bar.start()
        logging.debug('fuzzing %s', file_path)

        self.num_it = 0
        self.num_unsuccessful_it = 0
        self.num_consecutive_unsuccessful_it = 0

        fuzzed_file_path = None

        while self.num_it < self.total_it:
            logging.debug('num_successful_iterations %s', str(self.num_it))
            logging.debug('num_unsuccessful_iterations %s',
                          str(self.num_unsuccessful_it))

            if self.reach_unsuccessful_iterations():
                # quit this file
                break

            # tmp file fuzzed
            fuzzed_file_path = os.path.join(tempfile.gettempdir(),
                                            'temp_filefuzzed')

            if self.fuzzer == 'radamsa':
                # fuzz the file with radamsa
                fuzzed_file_path = os.path.join(tempfile.gettempdir(),
                                                'temp_filefuzzed')
                radamsa(fuzzed_file_path, file_path)
            elif self.fuzzer == 'quickfuzz':
                # fuzz the file with quickfuzz
                fuzzed_file_path = os.path.join(tempfile.gettempdir(),
                                                'temp_filefuzzed_qf')
                try:
                    quickfuzz(fuzzed_file_path, file_path, cache=self.cache)
                except UnicodeDecodeError as e:
                    logging.debug('quickfuzz (%s), trying again...', e)
                    continue
                except Exception as e:
                    if not ('cache hit' in str(e)):
                        raise Exception('Unexpected quickfuzz error (%s)', e)
                    logging.debug(
                        'quickfuzz cache hit! trying again... size %s',
                        len(self.cache)
                    )
                    continue
            try:
                if self.validator:
                    if not self.is_valid(fuzzed_file_path):
                        # skip this file
                        continue
            finally:
                logging.debug('done validation %s',
                              datetime.datetime.now().isoformat())

            # check discrepancy
            try:
                logging.debug('start calling engines %s',
                              datetime.datetime.now().isoformat())
                self.is_discrepant(file_path, fuzzed_file_path, shell=shell)
            except (UnicodeDecodeError, timeout_decorator.TimeoutError) as e:
                # TODO: we can't handle properly non-unicode outputs
                # because the .decode('utf-8') to convert bytes into strings
                # raises this exception when the non-unicode char is mapped.
                logging.debug('error while calling engines.. (%s)', str(e))
                self.num_unsuccessful_it += 1
                self.num_consecutive_unsuccessful_it += 1
                continue
            finally:
                logging.debug('done calling engines %s',
                              datetime.datetime.now().isoformat())

            # successful iteration
            self.num_it += 1
            self.num_consecutive_unsuccessful_it = 0
            bar.update(self.num_it)

        bar.finish()
        logging.debug('done fuzzing %s', file_path)
