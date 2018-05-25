"""
    This file check if project is configured
"""
import os
from subprocess import call, PIPE, check_output
from jsfuzz.utils.constants import chakra, v8, javascriptcore, spidermonkey

ERROR_MSG = """\n########## ENVIRONMENT ERROR ##########\n Error: {}\n##########"""

tar_path = 'js_engines/bin.tar.gz'
bin_output = 'js_engines/bin/'

def update_engines():
    check_output(['mkdir', '-p', bin_output]) # create folder if not exists
    check_output(['tar', '-xvzf', tar_path, '-C', bin_output]) # extract binaries to js_engines/bin folder

def is_engines_installed():
    try:
        call([javascriptcore, '--help'])
        check_output([chakra, '--help'])
        check_output([v8, '--help'])
        check_output([spidermonkey, '--help'])
    except OSError:
        raise Exception(ERROR_MSG.format("Engines not found, check README.md and see the instructions"))

def is_radamsa_installed():
    try:
        call(["radamsa", "--version"], stdout=PIPE, stderr=PIPE)
    except OSError:
        raise Exception(
            ERROR_MSG.format(
                "Radamsa not found, please go to jsfuzz/README.md and see the instructions"
            )
        )

is_engines_installed()
is_radamsa_installed()
