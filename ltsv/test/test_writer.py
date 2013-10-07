# -*- encoding: utf-8 -*-

import sys
import pytest
from ltsv import writer, dump

try:
    from collections import OrderedDict
except ImportError:
    pass

if sys.version_info < (3, 0):
    UNICODE_TYPE = unicode
    BYTES_TYPE = str
else:
    UNICODE_TYPE = str
    BYTES_TYPE = bytes


def test_dump_empty_dict():
    assert '' == dump({})


def test_writer_empty_dict():
    assert b'' == writer({})


def test_writer_empty_list():
    assert b'' == writer([])


def test_dump():
    result = dump({'aaa': 'bbb', 'ccc': 'ddd', 'eee': '123'})
    result = sorted(result.split("\t"))
    expect = ['aaa:bbb', 'ccc:ddd', 'eee:123']
    assert expect == result


@pytest.mark.skipif("sys.version_info < (2, 7)")
def test_ordered_dict():
    odict = OrderedDict([('bcd', 'efg'), ('abc', 'def'), ('3', '444')])
    result = dump(odict)
    expect = "bcd:efg\tabc:def\t3:444"
    assert expect == result


def test_writer_list():
    result = writer([{'bcd': 'efg', 'abc': 'def'}, {'eee': '123'}])
    expect1 = b"abc:def\tbcd:efg\neee:123"
    expect2 = b"bcd:efg\tabc:def\neee:123"
    assert expect1 == result or expect2 == result


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
    assert isinstance(result, UNICODE_TYPE)
    assert u"あ:い\tう:え" == result or u"う:え\tあ:い" == result


def test_not_unicode():
    result = dump({'a': 'b', 'c': 'd'})
    assert isinstance(result, str)


def test_join_str_and_unicode():
    result = dump({'a': 'b', u'あ': 123})
    assert isinstance(result, UNICODE_TYPE)


def test_encoding_unicode():
    result = writer({u'あ': u'い'}, encoding='utf-8')
    assert isinstance(result, BYTES_TYPE)
    assert b"\xe3\x81\x82:\xe3\x81\x84" == result


def test_encoding_str():
    result = writer({'a': 'b'}, encoding='utf-8')
    assert isinstance(result, BYTES_TYPE)
    assert b"a:b" == result


def test_replace_special_characters():
    result = dump({"a": "b\r\nc\rd\n\re\t\\f"})
    assert isinstance(result, str)
    assert "a:b c d  e \\f" == result
