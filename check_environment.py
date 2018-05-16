"""
    This file check if project is configured
"""
from subprocess import call, PIPE
from jsfuzz.utils.constants import chakra, v8, javascriptcore, spidermonkey


ERROR_MSG = """\n########## ENVIRONMENT ERROR ##########\n Error: {}\n##########"""

def download_binaries():
    try:
        call(['git', 'lfs', 'install'], stdin=PIPE, stdout=PIPE)
        call(['git', 'lfs', 'pull'], stdin=PIPE, stdout=PIPE)
        call(['git', 'lfs', 'fetch'], stdin=PIPE, stdout=PIPE)
    except OSError:
        raise Exception('The "git-lfs" is not installed. Please, check https://git-lfs.github.com to install.')

def is_engines_installed():
    try:
        call([javascriptcore, '-h'], stdin=PIPE, stdout=PIPE)
        call([chakra, '-v'], stdin=PIPE, stdout=PIPE)
        call([v8, '-v'], stdin=PIPE, stdout=PIPE)
        call([spidermonkey, '-v'], stdin=PIPE, stdout=PIPE)
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

download_binaries()
is_engines_installed()
is_radamsa_installed()
