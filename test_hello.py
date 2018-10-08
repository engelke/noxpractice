#!/usr/bin/python

"""
Standard 'Hello, world.' with some tests.
"""

import sys
import pytest
if sys.version_info.major == 2:
    from StringIO import StringIO
else:
    from io import StringIO


def hello(who):
    print('Hello, ' + who + '!')


def test_hello():
    save_stdout = sys.stdout
    sys.stdout = StringIO()
    hello('you')
    assert sys.stdout.getvalue() == 'Hello, you!\n'
    sys.stdout = save_stdout

