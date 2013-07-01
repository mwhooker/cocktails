from collections import namedtuple
import paths
import os.path


tib = os.path.join( paths.SOURCES_PATH, 'other/THE IDEAL BARTENDER')


keys = (s.upper() for s in ('dedicated', 'introduction'))

Section = namedtuple('Section', ('title', 'body'))

thebook = []

title = body = None

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
                print "starting parse"
                started = True

        if line.startswith("***END OF THE PROJECT GUTENBERG EBOOK"):
            print "ending parse"
            break

        if pre is not None:
            yield (pre, cur, post)


def found_title(newtitle):
    global title, body
    if title and len(body):
        thebook.append(Section(title, body))
        body = None
    title = newtitle

def istitle(pre, cur, post):
    if not len(cur):
        return False
    split = cur.split()
    return all([split[0].isupper(), len(split) < 8,
                not len(pre), not len(post)])



if __name__ == '__main__':
    with open(tib) as f:
        longest_line = max(len(line) for line in f)
        f.seek(0)
        for pre, cur, post in filter_book(f):
            if istitle(pre, cur, post):
                found_title(cur)
                continue

            if not body:
                body = [cur]
            else:
                body.append(cur)

    print len(thebook)
    print "\n".join(map(str, thebook))

"""

# grep -v "^[A-Za-z0-9 ][^A-Z]"

#end: ***END OF THE PROJECT GUTENBERG EBOOK THE IDEAL BARTENDER***
"""
