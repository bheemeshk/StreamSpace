__author__ = 'bheem'

import rdflib
import os

os.chdir('/home/bheem/Downloads')
g = rdflib.Graph()
result = g.parse("sample.rdf")

print("graph has %s statements." % len(g))
# prints graph has 79 statements.


for s, p, o in g:
    print((s, p, o))
    break
