# -*- encoding: utf-8 -*-


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
    for k, v in dic.iteritems():
        k = k if isinstance(k, unicode) else str(k)
        if v is None:
            v = ""
        elif not isinstance(v, unicode):
            v = str(v)
        values.append(k + ":" + v)

    ltsv = "\t".join(values)
    if encoding is None:
        return ltsv
    else:
        return ltsv.encode(encoding)
