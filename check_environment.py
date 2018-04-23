"""
    This file check if project is configured
"""
from subprocess import call, PIPE
from utils.constants import chakra, v8, javascriptcore, spidermonkey


ERROR_MSG = """\n########## ENVIRONMENT ERROR ##########\n Error: {}\n##########"""

def is_engines_installed():
    if not (chakra and v8 and javascriptcore and spidermonkey):
        raise Exception(
            ERROR_MSG.format(
                "Engines not found, please go to jsfuzz/js_engines folder and see the instructions"
            )
        )

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
