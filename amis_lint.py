# -*- coding: utf8 -*-
# Python2
# Some lint functions

import re

def remove_punc(s):
    if s is None:
        return None
    s = s.strip()
    # Weird exceptions
    s = s \
            .replace(u'ē', 'e') \
            .replace(u'’', "'")
    r = re.sub(r'[^a-z0-9\' ^]', '', s)
    r = re.sub(r' +', ' ', r)
    # ts = traditional_remove_punc(s)
    # if r != ts:
    #     print ts, '=>', r
    return r


def traditional_remove_punc(s):
    r = s \
            .replace(',', ' ') \
            .replace(':', ' ') \
            .replace('.', ' ') \
            .replace('!', ' ') \
            .replace('?', ' ') \
            .replace('  ', ' ') \
            .strip()
    return r
