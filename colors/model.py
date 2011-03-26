
#import colorsys
#from rdflib import ConjunctiveGraph, Namespace, URIRef, Literal

formats = {
            "rgb"    : "rgb",
            "rrggbb" : "rgb",
            "r,g,b"  : "rgb"
         }

class Color:

    def __init__(self, color, format, base="http://purl.org/color"):
        self.base = base
        self.color = color
        self.format = format
        self.rgb = self.__parse_color(color, format)
        self.__build_uris()

    def __parse_color(self, color, format):
        if (format == "rgb"):
            return (int(color[0], 16) * 16 + int(color[0], 16), 
                    int(color[1], 16) * 16 + int(color[1], 16), 
                    int(color[2], 16) * 16 + int(color[2], 16))
        elif (format == "rrggbb"):
            return (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))
        elif (format == "r,g,b"):
            splitted = color.split(",")
            return (int(splitted[0]), int(splitted[1]), int(splitted[2]))
        else:
            pass #FIXME

    def __str__(self):
        return "#%s" % self.__format_rgb()

    def __format_rgb(self):
        if (self.format == "rrggbb"):
            return self.color
        else:
            return "%X%X%X" % (self.rgb[0], self.rgb[1], self.rgb[2])
    
    def __build_uris(self):
        self.uri = "%s/%s/%s" % (self.base, formats[self.format], self.color)
        if (self.format == "rrggbb"):
            self.primary_uri = self.uri
        else:
            self.primary_uri = "%s/%s/%s" % (self.base, formats["rrggbb"], self.__format_rgb())
    
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

