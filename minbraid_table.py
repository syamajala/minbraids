import re


class MinBraid():

    def __init__(self, tag):
        self.tag = tag
        self.strands = None
        self.crossings = None
        self.alternating = None
        self.word = None
        self.rolf = None

    def __str__(self):
        return self.tag + " " + self.word

with open("minbraids.txt") as f:
    braidlst = []
    prev_type = None
    cur_type = None
    counts = {'tag': 0, 's-cr': 0, 'word': 0, 'rolf': 0, 'r': 0}

    for line in f:
        l = line.rstrip('\n')
        if re.match('^1?[0-9]:1[\-, n][0-9]+$', l):
            prev_type = 'tag'
            cur_type = 'tag'
            braidlst.append(MinBraid(l))
        elif re.match('^[0-9]+[\-, n][0-9]+$', l):
            if prev_type == 'tag' and cur_type != 's-cr':
                cur_type == 's-cr'
            if cur_type == 's-cr':
                chars = list(l)
                try:
                    strands = int(chars[0])
                    alternating = True
                    if chars[1] == 'n':
                        alternating = False
                    crossings = int(l[2:])
                    braidlst[counts['s-cr']].strands = int(strands)
                    braidlst[counts['s-cr']].crossings = int(crossings)
                    counts['s-cr'] = counts['s-cr'] + 1
                except IndexError:
                    print (counts['s-cr'], l)
                except ValueError:
                    print l
        elif re.match('^A+[A-E, a-e]*$', l):
            if prev_type != 's-cr' and cur_type != 'braid':
                prev_type = 's-cr'
                cur_type = 'braid'
            try:
                braidlst[counts['word']].word = l
                counts['word'] = counts['word'] + 1
            except IndexError:
                print (counts['word'], l)
        elif re.match('^[0-9]+$', l):
            if prev_type == 's-cr' and cur_type == 'braid':
                cur_type = 'ap'
                prev_type = 'braid'


def findtag(w):
    for i in braidlst:
        if i.word == w:
            return i.tag
