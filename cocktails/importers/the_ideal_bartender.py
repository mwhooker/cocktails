from collections import namedtuple
import paths
import os.path
from itertools import imap, ifilter


tib = os.path.join( paths.SOURCES_PATH, 'other/THE IDEAL BARTENDER')


keys = (s.upper() for s in ('dedicated', 'introduction'))

Section = namedtuple('Section', ('title', 'body'))

thebook = []

title = None
body = []

def filter_book(f):
    started = False
    pre = cur = post = None
    for line in f:
        line = line.strip()
        pre, cur, post = cur, post, line

        if not started:
            if line != 'DEDICATED':
                continue
            else:
                # print "starting parse"
                started = True

        if line.startswith("***END OF THE PROJECT GUTENBERG EBOOK"):
            # print "ending parse"
            break

        if pre is not None:
            yield (pre, cur, post)


def found_title(newtitle):
    global title, body
    if title and len(body):
        thebook.append(Section(title, body))
        body = []
    title = newtitle

def istitle(pre, cur, post):
    if not len(cur):
        return False
    checks = ([cur.split()[0].isupper(),
               #length before open paren
               len(cur.split('(')[0].split()) < 8,
               not len(pre), len(post.split()) <= 1])

    return all(checks)



if __name__ == '__main__':
    with open(tib) as f:
        longest_line = max(len(line) for line in f)
        f.seek(0)
        for pre, cur, post in filter_book(f):
            if istitle(pre, cur, post):
                found_title(cur)
                continue

            if not body and len(cur):
                body = [cur]
            elif len(cur):
                body.append(cur)

        found_title(None)

    recipes = set(imap(
        str.lower,
        (section.title for section in thebook))) - set(
            ['index', 'dedicated', 'introduction'])

    index = set(imap(
        str.lower,
        ifilter(len, thebook[-1].body))) - set(['page'])

    if recipes != index:
        print "***failure***\n"
        print "differences: %s" % len(index.symmetric_difference(recipes))
        print "index with no recipe found"
        print index - recipes
        print "recipes not found in the index"
        print recipes - index
        assert False, "recipes and index don't match."

    for section in thebook:
        print section.title
        print "*" * len(section.title)
        print ""
        print '\n'.join(section.body)
        print ""



"""

# grep -v "^[A-Za-z0-9 ][^A-Z]"

#end: ***END OF THE PROJECT GUTENBERG EBOOK THE IDEAL BARTENDER***
"""
