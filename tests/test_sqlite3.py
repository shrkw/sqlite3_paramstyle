# coding:utf-8

from __future__ import division, print_function, absolute_import
import pytest
import sqlite3_paramstyle


@pytest.fixture
def conn():
    return sqlite3_paramstyle.ExtendedParamstyleConnection(":memory:")


@pytest.fixture
def cur():
    return sqlite3_paramstyle.ExtendedParamstyleConnection(":memory:").cursor()


def test_cursor_execute_without_param(cur):
    cur.execute("select 1")
    assert cur.fetchall() == [(1,)]


def test_cursor_execute_with_qmark_param(cur):
    cur.execute("select ?", ("a",))
    assert cur.fetchall() == [("a",)]


def test_cursor_execute_with_printf_param(cur):
    cur.execute("select %s, %s", ("foo", "bar"))
    assert cur.fetchall() == [("foo", "bar")]


def test_cursor_execute_with_named_param(cur):
    cur.execute("select :who", {"who": "bc"})
    assert cur.fetchall() == [("bc",)]


def test_cursor_execute_with_pyformat_param(cur):
    cur.execute("select %(who)s, %(age)s", {"who": "bc", "age": 20})
    assert cur.fetchall() == [("bc", 20)]


def test_cursor_execute_percent(cur):
    cur.execute("select '%%', %s", ("a",))
    assert cur.fetchall() == [("%", "a",)]


def cursor_executemany(cur, symbol):
    def char_generator():
        yield ("abc",)
        yield ("bar",)
    cur.execute("create table sample (notes text)")
    cur.executemany("insert into sample values (%s)" % symbol, char_generator())
    cur.execute("select notes from sample")
    assert cur.fetchall() == [("abc",), ("bar",)]


def test_cursor_executemany_with_qmark_param(cur):
    cursor_executemany(cur, "?")


def test_cursor_executemany_with_printf_param(cur):
    cursor_executemany(cur, "%s")
