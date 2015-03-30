# sqlite3paramstyle

*Extended paramstyle for sqlite3 module*

Give a comatibility for following paramstyles to sqlite3 module.

* ANSI C printf format codes, e.g. ...WHERE name=%s
* Python extended format codes, e.g. ...WHERE name=%(name)s

https://www.python.org/dev/peps/pep-0249/#paramstyle

Tested on 2.7.8 and 3.4.1


# Usage

    import sqlite3paramstyle
    conn = sqlite3paramstyle.connect(":memory:")

# Requirements

* py.test
* tox

See `requirements.txt`.

# Test

    tox



