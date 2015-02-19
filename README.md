Introduction
============

A test suite for the Haskell library language-python (a parser for Python 2 and 3).

License
-------

language-python-test is released as open source software under the terms of the 3 clause BSD License. See the file LICENCE.txt in the [source code repository of language-python-test](https://github.com/bjpop/language-python-test).

This package also contains files from the CPython test suite. Those files are found in the
sub-directories test/CPython_test_suite_v2 and test/CPython_test_suite_v3. The license for those files is
contained in those directories. 

Installation
------------

language-python-test can be installed with cabal:

    cabal install language-python-test

You may want to consider installing it in a sandbox. This will avoid
polluting your cabal package database.

    mkdir language_python_test
    cd language_python_test
    cabal sandbox init
    cabal install language-python-test
    # perhaps copy the executables from language_python_test/.cabal-sandbox/bin to ~/.cabal/bin/
    # and run cabal sandbox delete to remove the sandbox files

Usage
-----

The package builds the following executable programs:

* language-python-parse-pretty
* language-python-roundtrip
* language-python-tokens

The first program parses a Python file as input and pretty prints it back again.

The second program performs a round-trip of parse, pretty print, parse and pretty print.

The third program performs lexical analysis on the input Python file and pretty prints the resulting token stream.

The test suite (which tests the behaviour of language-python) uses the shelltest tool. To run the tests you need to have shelltest installed:

    cabal install shelltestrunner

The tests are found in the sub-directory called tests.

You can run the tests like so:

    shelltest --color --execdir test/ -- -j1

We provide a Makefile for convenience which does the same thing. You can run it like so:

    make test
