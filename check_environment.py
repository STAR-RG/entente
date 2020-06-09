"""
    This file check if project is configured
"""
from subprocess import call, PIPE, check_output
from jsfuzz.utils.constants import (
    chakra, v8, javascriptcore, spidermonkey, hermes
)

ERROR_MSG = """\n########## ENVIRONMENT ERROR ##########\n Error: {}\n##########"""


def is_engines_installed():
    try:
        call([javascriptcore, '--help'], stdout=PIPE, stderr=PIPE)
        check_output([chakra, '--help'])
        check_output([v8, '--help'])
        check_output([spidermonkey, '--help'])
        check_output([hermes, '--help'])
    except OSError:
        raise Exception(
            ERROR_MSG.format(
                "Engines not found. Check if v8, ch, jsc, sm and hermes"
                "is installed in your PATH (see install_deps.sh)"
            )
        )


def is_radamsa_installed():
    try:
        call(["radamsa", "--version"], stdout=PIPE, stderr=PIPE)
    except OSError:
        raise Exception(
            ERROR_MSG.format(
                "Radamsa not found, please go to jsfuzz/README.md or\
                    install_deps.sh and see the instructions"
            )
        )


def is_quickfuzz_installed():
    try:
        call(["QuickFuzz", "--version"], stdout=PIPE, stderr=PIPE)
    except OSError:
        raise Exception(
            ERROR_MSG.format(
                "QuickFuzz not found, please go to jsfuzz/README.md or\
                     install_deps.sh and see the instructions"
            )
        )


is_engines_installed()
is_radamsa_installed()
is_quickfuzz_installed()
