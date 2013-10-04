# -*- encoding: utf-8 -*-

import sys


def writer(obj, lineterminator="\n", encoding="utf-8"):
    if isinstance(obj, dict):
        return dump(obj, encoding)
    elif isinstance(obj, list):
        out = []
        for line in obj:
            out.append(dump(line, encoding))
        return lineterminator.join(out)
    else:
        raise ValueError("not support")


def dump(dic, encoding=None):
    values = []
    unicode_type = unicode if sys.version < '3' else str
    for k, v in dic.items():
        k = k if isinstance(k, unicode_type) else str(k)
        if v is None:
            v = ""
        elif not isinstance(v, unicode_type):
            v = str(v)

            # Replace special character to space.
            # This is not LTSV normative but 'fail-safe' treatment.
            # User can escape values by own way before passing this method,
            # if required. For example:
            #
            #   value = value.replace("\\", "\\\\")
            #   value = value.replace("\t", "\\t")
            #   value = value.replace("\r", "\\r")
            #   value = value.replace("\n", "\\n")
            #
            v = v.replace("\t", " ")
            v = v.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")

        values.append(k + ":" + v)

    ltsv = "\t".join(values)
    if encoding is None:
        return ltsv
    else:
        return ltsv.encode(encoding)
