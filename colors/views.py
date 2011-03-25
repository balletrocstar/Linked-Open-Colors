
import logging
from model import Color
from http import Http303, get_preferred_suffix
from django.http import HttpResponse


def rgb(request, rgb):
    logging.info("Serving RGB color with content negotiation")
    suffix = get_preferred_suffix(request)
    url = "%s.%s" % (rgb, suffix)
    return Http303(url)

def rgb_html(request, rgb):
    logging.info("Serving RGB color as HTML")
    return HttpResponse("%s in HTML" % rgb)

def rgb_html(request, rdf):
    logging.info("Serving RGB color as RDF")
    return HttpResponse("%s in RDF" % rgb)

