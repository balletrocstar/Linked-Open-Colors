
from common import if_else
from mappings import get_mapping_dbpedia_color, get_mapping_css_color
#import colorsys
#from rdflib import ConjunctiveGraph, Namespace, URIRef, Literal

formats = {
            "rgb"    : "rgb",
            "rrggbb" : "rgb",
            "r,g,b"  : "rgb",
            "css"    : "css"
         }

class Color:

    def __init__(self, color, format, base="http://purl.org/colors"):
        self.base = base
        self.color = color
        self.format = format
        self.rgb = self.__parse_color()
        self.hex = self.__format_hex()
        self.__build_uris()
        self.__build_mappings()

    def __parse_color(self):
        if (self.format == "rgb"):
            return (int(self.color[0], 16) * 16 + int(self.color[0], 16), 
                    int(self.color[1], 16) * 16 + int(self.color[1], 16), 
                    int(self.color[2], 16) * 16 + int(self.color[2], 16))
        elif (self.format == "rrggbb"):
            return (int(self.color[0:2], 16), int(self.color[2:4], 16), int(self.color[4:6], 16))
        elif (self.format == "r,g,b"):
            splitted = self.color.split(",")
            r = int(splitted[0])
            g = int(splitted[1])
            b = int(splitted[2])
            if (r > 255 or g > 255 or b > 255):
                raise Exception("Invalid color: " + self.color)
            else:
                return (r, g, b)
        elif (self.format == "css"):
            rgb = get_mapping_css_color(self.color)
            if (rgb == None):
                raise Exception("Invalid CSS color: " + self.color)
            else:
                return (int(rgb[0:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16))
        else:
            raise Exception("Unssuported format: " + self.format)

    def __str__(self):
        if (self.format == "rgb" or self.format == "rrggbb"):
            return "#%s" % self.color
        else:
            return self.color

    def __format_hex(self):
        if (self.format == "rrggbb"):
            return self.color.upper()
        else:
            r = if_else(self.rgb[0]<16, "0%X" % self.rgb[0], "%X" % self.rgb[0])
            g = if_else(self.rgb[1]<16, "0%X" % self.rgb[1], "%X" % self.rgb[1])
            b = if_else(self.rgb[2]<16, "0%X" % self.rgb[2], "%X" % self.rgb[2])
            return "%s%s%s" % (r, g, b)
    
    def __build_uris(self):
        self.uri = "%s/%s/%s" % (self.base, formats[self.format], self.color)
        if (self.color == self.hex):
            self.primary_uri = self.uri
        else:
            self.primary_uri = "%s/%s/%s" % (self.base, formats["rrggbb"], self.hex)

    def __build_mappings(self):
        self.mappings = {}
        self.mappings["dbpedia_color"] = get_mapping_dbpedia_color(self.hex)
    
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

