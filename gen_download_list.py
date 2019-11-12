# -*- coding: utf8 -*-
# Python2
# Generate the list of MP3 to download

import json
import codecs

ami = codecs.open('ami.json', encoding='UTF-8')
lst = codecs.open('download_list.txt', 'w', encoding='UTF-8')

for line in ami:
    lex = json.loads(line.strip())
    for ex in lex['examples']:
        if ex['pronounce'] and ex['pronounce'].find('/') != -1:
            print >> lst, ex['pronounce']
    if lex['pronounce'] and lex['pronounce'].find('/') != -1:
        print >> lst, lex['pronounce']

print 'Run wget -c -i download_list.txt'
