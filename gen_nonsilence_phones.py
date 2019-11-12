# -*- coding: utf8 -*-
# Python2

lexicon = open('./data/local/dict/lexicon.txt')
phones = open('./data/local/dict/nonsilence_phones.txt', 'w')

PHONES = {}

for line in lexicon:
    letters = line.strip().split(' ', 1)[1].split()
    for l in letters:
        PHONES[l] = 1

for k in PHONES:
    print >> phones, k
