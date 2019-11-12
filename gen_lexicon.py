# -*- coding: utf-8 -*-
# Python2

import codecs
from amis_lint import remove_punc

lexicon = codecs.open('data/local/dict/lexicon.txt', 'w', encoding='UTF-8')
txt_fp = codecs.open('data/train/text', 'r', encoding='UTF-8')

LEX = {}

for lex in txt_fp:
    words = remove_punc(lex.split(' ', 1)[1]).strip().split()
    for w in words:
        LEX[w] = 1

for w in LEX:
    print >> lexicon, w, ' '.join(list(w.replace('ng', ':'))).replace(':', 'ng')
