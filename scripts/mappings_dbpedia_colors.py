#!/usr/bin/python
# -*- coding: utf-8 -

from SPARQLWrapper import SPARQLWrapper, JSON

def retrieve_mappings():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX dbpo: <http://dbpedia.org/ontology/>
        PREFIX dbpp: <http://dbpedia.org/property/>
        SELECT ?color ?hex
        FROM <http://dbpedia.org>
        WHERE {
            ?color rdf:type dbpo:Colour .
            ?color dbpp:hex ?hex
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    mappings = {}

    for result in results["results"]["bindings"]:
        mappings[result["hex"]["value"]] = result["color"]["value"]

    return mappings

if __name__ == "__main__":
    mappings = retrieve_mappings()
    print mappings

