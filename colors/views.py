
import logging
from model import Color
from http import Http303, get_preferred_suffix
from django.http import HttpResponse


def rgb(request, rgb):
    logging.info("Serving RGB color #%s with content negotiation" % rgb)
    suffix = get_preferred_suffix(request)
    url = "%s.%s" % (rgb, suffix)
    return Http303(url)

def rgb_html(request, rgb):
    logging.info("Serving RGB color #%s as HTML" % rgb)
    return HttpResponse("%s in HTML" % rgb)

def rgb_rdf(request, rgb):
    logging.info("Serving RGB color #%s as RDF" % rgb)
    return HttpResponse("%s in RDF" % rgb)

