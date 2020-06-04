Instructions on how to use the differential testing infrastructure

#Requirements

Linux
Python 3.6
tox virutalenv (https://tox.readthedocs.io/en/latest/)
ECMAScript host eshost (https://github.com/bterlson/eshost-cli)
JavaScript (engines: chackra, javascriptcore, spidermonkey, v8, hermes) by jsvu

#Installation (JSEDT - jsengines_differential_testing)

1. Run the install_jsedt.sh
2. Edit the file tox.ini
   i. [tox] envlist = py36
   ii.[testenv] commands =
                python check_environment.py
                pytest -s -v -x {posargs:fuzz_drivers/nofuzz}
                pytest -s -v -x {posargs:fuzz_drivers/fuzz}
                pytest
   iii. deps = -rrequirements.txt            
3. Open a terminal window, go to project folder and run: $> tox

#Data

https://drive.google.com/open?id=1YHXatZ5KO19yHxg73FN32Xtn5ayEXw7F




