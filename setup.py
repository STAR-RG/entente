#!/usr/bin/env python

from distutils.core import setup

setup(name='jsfuzz',
      version='1.0',
      description='Fuzzing Infrastructure for Testing JS Engines',
      author='Igor Simoes, Marcelo d\'Amorim',
      author_email='isol2@cin.ufpe.br, damorim@cin.ufpe.br',
      url='https://github.com/damorim/jsfuzz',
      packages=['jsfuzz.fuzzer','jsfuzz.utils','esprima'],
     )
