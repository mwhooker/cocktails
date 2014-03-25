from __future__ import print_function

from pyparsing import Regex, oneOf, OneOrMore, Word, alphas
from collections import namedtuple
import paths
import os.path


tib = os.path.join( paths.SOURCES_PATH, 'other/THE IDEAL BARTENDER')

measures = ["jigger", "pony", "teaspoonful", "dash", "dashes", "jiggers",
            "light dash", "yolk", "wineglass", "glass"]

ingredient = Regex("[0-9 -/]+") + oneOf(measures, caseless=True) + OneOrMore(Word(alphas))

keys = (s.upper() for s in ('dedicated', 'introduction'))

Section = namedtuple('Section', ('title', 'body'))
Recipe = namedtuple('Recipe', ('pre', 'ingredients', 'post'))
Ingredient = namedtuple('Ingredient', ('portion', 'name'))
Portion = namedtuple('Portion', ('units', 'unit'))

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
                # print("starting parse")
                started = True

        if line.startswith("***END OF THE PROJECT GUTENBERG EBOOK"):
            # print("ending parse")
            break

        if pre is not None:
            yield (pre, cur, post)


def parse_ingredients(line):
    #return Ingredient(spl[0], spl[1])
    pass


import sys
i = 0
def parse_body(body):
    global i
    pre, ingredients, post = [], [], []
    b = Recipe(pre, ingredients, post)
    if i > 2:
        sys.exit()
    i+=1
    for line in body:
        if not line[0].isdigit():
            pre.append(line)
        else:
            ingredients.append(parse_ingredients(line))

    print(b)
    return b


def found_title(newtitle=None):
    """Commits previous title.

    no argument means commit title and prepare to end processing.
    """
    global title, body
    if title and len(body):
        print(title)
        if title not in ('DEDICATED', 'INTRODUCTION'):
            body = parse_body(body)
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

        found_title()

    recipes = set(map(
        str.lower,
        (section.title for section in thebook))) - set(
            ['index', 'dedicated', 'introduction'])

    index = set(map(
        str.lower,
        filter(len, thebook[-1].body.ingredients))) - set(['page'])

    if recipes != index:
        print("***failure***\n")
        print("differences: %s" % len(index.symmetric_difference(recipes)))
        print("index with no recipe found")
        print(index - recipes)
        print("recipes not found in the index")
        print(recipes - index)
        assert False, "recipes and index don't match."

    for section in thebook:
        print(section.title)
        print("*" * len(section.title))
        print("")
        print('\n'.join(section.body.pre))
        print('\n'.join(section.body.ingredients))
        print('\n'.join(section.body.post))
        print("")



"""

# grep -v "^[A-Za-z0-9 ][^A-Z]"

#end: ***END OF THE PROJECT GUTENBERG EBOOK THE IDEAL BARTENDER***
"""
