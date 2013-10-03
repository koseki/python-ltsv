# -*- encoding: utf-8 -*-

from ltsv import writer
from collections import OrderedDict


def test_writer_empty():
    assert '' == writer({})


def test_writer_empty_list():
    assert '' == writer([])


def test_writer():
    result = writer({'aaa': 'bbb', 'ccc': 'ddd', 'eee': '123'})
    result = sorted(result.split("\t"))
    expect = ['aaa:bbb', 'ccc:ddd', 'eee:123']
    assert expect == result


def test_writer_ordered_dict():
    odict = OrderedDict([('bcd', 'efg'), ('abc', 'def'), ('3', '444')])
    result = writer(odict)
    expect = "bcd:efg\tabc:def\t3:444"
    assert expect == result


def test_writer_list():
    odict = OrderedDict([('bcd', 'efg'), ('abc', 'def')])
    result = writer([odict, {'eee': '123'}])
    expect = "bcd:efg\tabc:def\neee:123"
    assert expect == result


def test_writer_int():
    result = writer({'bbb': 111, 'aaa': 222, 3: 444})
    result = sorted(result.split("\t"))
    expect = ['3:444', 'aaa:222', 'bbb:111']
    assert expect == result


def test_writer_none():
    result = writer({'a': None, 'b': None})
    assert "a:\tb:" == result or "b:\ta:" == result