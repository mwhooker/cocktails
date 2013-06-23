import os.path


tib = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)))),
    'sources/other/THE IDEAL BARTENDER')


with open(tib) as f:
    print f.readline()
