import os, shlex, logging, datetime
from shutil import copyfile
from subprocess import call
from jsfuzz.utils import constants
from jsfuzz.fuzzer.radamsa_fuzzer import call_engines, validate_wrapper
from jsfuzz.fuzzer import validator

from progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed

import hashlib


OUTPUT_DEPENDENCIES_PATH = os.path.join(constants.fuzzers_dir, 'grammarinator_deps')

class Grammarinator:
    def __init__(self, grammar_path, single_grammar=True):
        if single_grammar:
            self.unlexer, self.unparser = self.process_single_grammar(grammar_path)
        else:
            self.unlexer, self.unparser = self.process_multiple_grammar(grammar_path)

    def str_to_hash(self, string):
        return hashlib.md5(string.encode()).hexdigest()

    def process_single_grammar(self, grammar):
        if not ('grammar' in grammar.lower() and '.g4' in grammar):
            raise Exception('Error: Invalid grammar')

        unlexer, unparser = None, None
        unlexer = grammar.replace('Grammar.g4', 'Unlexer.py')
        unparser = grammar.replace('Grammar.g4', 'Unparser.py')
        deps_files = os.listdir(OUTPUT_DEPENDENCIES_PATH)
        
        if (unlexer not in deps_files) or (unparser not in deps_files):
            process_cmd = """
            grammarinator-process {} --out {} --no-actions
            """.format(grammar, OUTPUT_DEPENDENCIES_PATH)
            args = shlex.split(process_cmd)
            call(args)

        return (unlexer, unparser)

    def process_multiple_grammar(self, grammars):
        """ process a grammar using grammarinator """
        if len(grammars) > 2 and not grammars:
            raise Exception('Grammar list must contains two elements')
        
        unlexer, unparser = None, None
        deps_files = os.listdir(OUTPUT_DEPENDENCIES_PATH)

        for grammar in grammars:
            if 'lexer' in grammar.lower() and '.g4' in grammar:
                lexer_path = grammar
                unlexer = lexer_path.replace('.g4', 'Unlexer.py')
            elif 'parser' in grammar.lower() and '.g4' in grammar:
                parser_path = grammar
                unparser = parser_path.replace('.g4', 'Unparser.py')
            else:
                raise Exception('Error: Invalid grammar')

        if (unlexer not in deps_files) or (unparser not in deps_files):
            process_cmd = """
            grammarinator-process {} {} --out {} --no-actions
            """.format(lexer_path, parser_path, OUTPUT_DEPENDENCIES_PATH)
            args = shlex.split(process_cmd)
            call(args)

        return (unlexer, unparser)
        
    def run_grammarinator(self, path, number_of_testcases):
        """ generate testcases using grammarinator """
        widgets = ['generating new files ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ']
        bar = ProgressBar(widgets=widgets, maxval=number_of_testcases).start()

        new_file = os.path.join(path, 'test_0')
        generate_cmd = """
        grammarinator-generate --unlexer {} \
        --unparser {} \
        --rule program \
        --encoding utf-8 \
        --out {} \
        --max-depth 20 \
        --jobs 1
        """.format(self.unlexer, self.unparser, os.path.join(path, 'test_%d'))

        args = shlex.split(generate_cmd)
        valid_files = 0
        logging.debug('starting grammarinator %s', datetime.datetime.now().isoformat())
        while valid_files < number_of_testcases:
            call(args)
            if not validator.validate(new_file):
                with open(new_file) as f:
                    filename = self.str_to_hash(f.read())
                filename = 'test_{}'.format(filename)
                if filename in os.listdir(path):
                    continue
                    
                os.rename(new_file, os.path.join(constants.seeds_dir, 'grammarinator', filename))
                valid_files += 1
                bar.update(valid_files)
        bar.finish()
        logging.debug('finished grammarinator %s', datetime.datetime.now().isoformat())