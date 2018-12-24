#!/usr/bin/python3
import sys
import time
from pprint import pprint
import nltk
#from nltk.tokenize import sent_tokenize
from nltk.collocations import *


def is_simple_quote(string):
    if string[0]=='\"' and string[-1]=='\"': return True
    else: return False

def tokenize_postwork(l):
    out = []
    while len(l)>2:
        if is_simple_quote(l[0]) and not is_simple_quote(l[1]):
            out.append(' '.join(l[0:2]))
            l = l[2:]
        else:
            out.append(l[0])
            l = l[1:]
    if len(l)>0:
        out.extend(l)
    return out


def tokenize_prework(text):
    out = []
    words = text.split()
    for w in words:
        # put whitespace after ? or !
        for ec in ['?', '!']:
            if ec in w[:-1]:
                w = w.replace(ec, ec + ' ')
        # put whitespace after '.'
        if '.' in w[:-1]:
            out2 = []
            s = w[:-1].split('.')
            while len(s) > 2:
                if s[0] in ['Dr', 'Mr', 'Ms', 'Mrs']:
                    out2.appned('%s.%s' % (s[0], s[1]))
                    s = s[2:]
            if len(s) > 0:
                out2.extend(s)
            out2[-1] = out2[-1] + w[-1]
            out.append('. '.join(out2))
            # print('L36')
            # pprint(out[-1])
            continue
        # there is no middle-punctuation
        out.append(w)
        '''
        print('=== start dump')
        pprint(out)
        '''
    return ' '.join(out)


if __name__ == '__main__':
    # nltk.download('punkt')
    text = input()
    '''
    print('=== result of pretokenize_adjust')
    pprint(text)
    print('=== end of dump')
    '''
    token = nltk.word_tokenize(text)
    finder = TrigramCollocationFinder.from_words(token)
    trigrams = sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))
    print(' '.join(trigrams[0][0]))
    #pprint(trigrams)

