# -*- encoding: utf-8 -*-

from ltsv import writer, dump
from collections import OrderedDict


def test_dump_empty_dict():
    assert '' == dump({})


def test_writer_empty_dict():
    assert '' == writer({})


def test_writer_empty_list():
    assert '' == writer([])


def test_dump():
    result = dump({'aaa': 'bbb', 'ccc': 'ddd', 'eee': '123'})
    result = sorted(result.split("\t"))
    expect = ['aaa:bbb', 'ccc:ddd', 'eee:123']
    assert expect == result


def test_ordered_dict():
    odict = OrderedDict([('bcd', 'efg'), ('abc', 'def'), ('3', '444')])
    result = dump(odict)
    expect = "bcd:efg\tabc:def\t3:444"
    assert expect == result


def test_writer_list():
    odict = OrderedDict([('bcd', 'efg'), ('abc', 'def')])
    result = writer([odict, {'eee': '123'}])
    expect = "bcd:efg\tabc:def\neee:123"
    assert expect == result


def test_int_key_and_value():
    result = dump({'bbb': 111, 'aaa': 222, 3: 444})
    result = sorted(result.split("\t"))
    expect = ['3:444', 'aaa:222', 'bbb:111']
    assert expect == result


def test_none_value():
    result = dump({'a': None, 'b': None})
    assert "a:\tb:" == result or "b:\ta:" == result


def test_unicode_key_and_value():
    result = dump({u'あ': u'い', u'う': u'え'})
    assert isinstance(result, unicode)
    assert u"あ:い\tう:え" == result or u"う:え\tあ:い" == result


def test_string_to_unicode():
    result = dump({'a': 'b', 'c': 'd'})
    assert isinstance(result, unicode)


def test_encoding():
    result = writer({u'あ': u'い'}, encoding='utf-8')
    assert isinstance(result, str)
    assert "\xe3\x81\x82:\xe3\x81\x84" == result
