import paths
import os.path


tib = os.path.join( paths.SOURCES_PATH, 'other/THE IDEAL BARTENDER')


with open(tib) as f:
    print f.readline()
