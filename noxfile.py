"""
Trying out nox with simple examples.
"""

import nox

@nox.session(python=['2.7', '3.5', '3.6'])
def tests(session):
    session.install('pytest')
    session.run('pytest')

@nox.session(python=['2.7', '3.5'])
def lint(session):
    session.install('flake8')
    session.run('flake8', 'google')

