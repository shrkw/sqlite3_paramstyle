# coding:utf-8

from __future__ import division, print_function, absolute_import
import sqlite3
import re


def connect(*args, **kwargs):
    return ExtendedParamstyleConnection(*args, **kwargs)


class ExtendedParamstyleConnection(sqlite3.Connection):
    def cursor(self, cursorClass=None):
        if cursorClass is None:
            return super(ExtendedParamstyleConnection, self).cursor(ExtendedParamstyleCursor)
        else:
            return super(ExtendedParamstyleConnection, self).cursor(cursorClass)

p = re.compile("%%|%s|%\((?P<key>[\w\-]+)\)s")


def convert(src):
    def f(match):
        s = match.group(0)
        if s == "%%":
            return "%"
        elif s == "%s":
            # convert from printf format to qmark style
            return "?"
        else:
            # convert from pyformat to named style
            return ":" + match.group("key")
    return p.sub(f, src)


class ExtendedParamstyleCursor(sqlite3.Cursor):
    def execute(self, sql, parameters=None):
        if parameters is None:
            return super(ExtendedParamstyleCursor, self).execute(convert(sql))
        else:
            return super(ExtendedParamstyleCursor, self).execute(convert(sql), parameters)

    def executemany(self, sql, seq_of_parameters):
        return super(ExtendedParamstyleCursor, self).executemany(convert(sql), seq_of_parameters)
