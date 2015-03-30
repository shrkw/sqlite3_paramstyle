from setuptools import setup

__VERSION__ = '0.0.1'
name = 'sqlite3paramstyle'

short_description = 'Extended paramstyle for sqlite3 module'
long_description = """\
Give a comatibility for following paramstyles to sqlite3 module.

* ANSI C printf format codes, e.g. ...WHERE name=%s
* Python extended format codes, e.g. ...WHERE name=%(name)s

Requirements
------------
* Python 2.7 or 3.4

Setup
-----
::

   $ easy_install {name}

or

::

   $ pip install {name}


Usage
-----
::

    import {name}
    conn = {name}.connect(":memory:")


History
-------
0.0.1 (2015-03-30)
~~~~~~~~~~~~~~~~~~
* first release

""".format(**locals())

classifiers = [
   "Development Status :: 4 - Beta",
   "License :: OSI Approved :: MIT License",
   "Programming Language :: Python :: 2.7",
   "Programming Language :: Python :: 3.4",
   "Topic :: Database",
]

setup(
    name=name,
    version=__VERSION__,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    packages=[name],
    keywords=["sqlite", "sqlite3"],
    author='Hiroyuki Shirakawa',
    author_email='shrkwh@gmail.com',
    url='https://github.com/shrkw/sqlite3_paramstyle',
    license='MIT License',
)
