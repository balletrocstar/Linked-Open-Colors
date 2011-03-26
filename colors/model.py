
#from rdflib import ConjunctiveGraph, Namespace, URIRef, Literal

class Color:

    def __init__(self, rgb, base="http://purl.org/color/rgb"):
        self.base = base
        self.rgb = rgb
        self.graph = None
        self.uri = "%s/%s" % (self.base, self.rgb)

    def __str__(self):
        return "#%s" % self.rgb
    
    #def get_rdf(self):
    #    if (self.graph == None):
    #        self.graph = self.__get_rdf()
    #    return self.graph

    #def __get_rdf(self):
    #    graph = ConjunctiveGraph()
    #    RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    #    RDFS  = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    #    FOAF  = Namespace("http://xmlns.com/foaf/0.1/")
    #    LOCO  = Namespace("%s/loco#" % self.base)
    #    graph.bind("rdfs", RDFS)
    #    graph.bind("rdf", RDF)
    #    graph.bind("foaf", FOAF)
    #    graph.bind("loco", LOCO)
    #
    #    doc = BNode()
    #    graph.add((doc, RDF.type, FOAF["Document"]))
    #    color = URIRef(self.uri)
    #    graph.add((color, RDF.type, LOCO["Color"]))
    #    graph.add((color, RDFS.label, Literal(str(color))))
    #    graph.add((color, FOAF.page, URIRef("%s/%s.html" % (self.base, self.rgb))))
    #
    #    return graph

    #def get_rdf_xml(self):
    #    graph = self.get_rdf()
    #    return graph.serialize(format="pretty-xml")

        


