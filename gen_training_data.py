# -*- coding: utf8 -*-
# Python2

import os
import glob
import codecs
import json
from mutagen.mp3 import MP3
from amis_lint import remove_punc

DATADIR = './mp3'
TXT_FMT = 'Pangcah%05d %s'
WAV_FMT = 'Pangcah%05d ffmpeg -i "%s/%s" -f wav -ac 1 -ar 16000 pipe:1 | '
SEG_FMT = 'Pangcah%05d %d %d'
UUT_FMT = 'Pangcah%05d Pangcah%05d'

txt_fp = codecs.open('./data/train/text', 'w', encoding='UTF-8')
wav_fp = codecs.open('./data/train/wav.scp', 'w', encoding='UTF-8')
seg_fp = codecs.open('./data/train/segments', 'w', encoding='UTF-8')
uut_fp = codecs.open('./data/train/uut2spk', 'w', encoding='UTF-8')

ami = codecs.open('./ami.json', 'r', encoding='UTF-8')


def mp3_len(fn):
    audio = MP3(fn)
    return audio.info.length


i = 0
for line in ami:
    lex = json.loads(line.strip())
    for ex in lex['examples']:
        if ex['sentence'] is None:
            continue
        if ex['sentence'].find(u'焦點') != -1:        # 原字典檔有誤
            i += 1
            continue
        txt = ex['sentence'].lower()
        print txt
        if ex['pronounce'] and ex['pronounce'].find('/') != -1:
            i += 1
            fn = ex['pronounce'].split('/')[-1]
            print >> txt_fp, TXT_FMT % (i, remove_punc(txt))
            print >> wav_fp, WAV_FMT % (i, '../../mp3', fn)
            print >> seg_fp, SEG_FMT % (i, 0, mp3_len('%s/%s' % (DATADIR, fn)))
            print >> uut_fp, UUT_FMT % (i, i)
    if lex['pronounce'] and lex['pronounce'].find('/') != -1:
        txt = lex['name'].lower()
        print txt
        i += 1
        fn = lex['pronounce'].split('/')[-1]
        print >> txt_fp, TXT_FMT % (i, remove_punc(txt))
        print >> wav_fp, WAV_FMT % (i, '../../mp3', fn)
        print >> seg_fp, SEG_FMT % (i, 0, mp3_len('%s/%s' % (DATADIR, fn)))
        print >> uut_fp, UUT_FMT % (i, i)

uut_fp.close()
seg_fp.close()
wav_fp.close()
txt_fp.close()
