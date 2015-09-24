__author__ = 'bheem'
from SPARQLWrapper import SPARQLWrapper, JSON
import json


sparql = SPARQLWrapper("http://localhost:10035/repositories/LearnSparql")
sparql.setQuery('''
                   select ?s ?p ?o {?s ?p ?o}
                '''
                )
sparql.setReturnFormat(JSON)
results = sparql.query().convert()


for result in results["results"]["bindings"]:
    print(result["label"]["value"])