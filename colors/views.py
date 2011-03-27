
import logging
from model import Color
from http import Http303, get_preferred_suffix
from django.http import HttpResponse
from django.shortcuts import render_to_response
from common import if_else

def color(request, color):
    logging.info("Serving color '%s' with content negotiation" % color)
    suffix = get_preferred_suffix(request)
    url = "%s.%s" % (color, suffix)
    return Http303(url)

def color_html(request, color, format):
    logging.info("Serving %s color '%s' as HTML" % (format, color))
    ctx = { "color" : Color(color, format) }
    return render_to_response("color.html", ctx, mimetype="application/xhtml+xml")

def color_rdf(request, color, format):
    logging.info("Serving %s color #%s as RDF" % (format, color))
    #return HttpResponse(color.get_rdf_xml(), mimetype="application/rdf+xml")
    ctx = { "color" : Color(color, format) }
    return render_to_response("color.rdf", ctx, mimetype="application/rdf+xml")

def rgb_html(request, rgb):
    format = if_else(len(rgb)==3, "rgb", "rrggbb")
    return color_html(request, rgb, format)

def rgb_rdf(request, rgb):
    format = if_else(len(rgb)==3, "rgb", "rrggbb")
    return color_rdf(request, rgb, format)

def css_html(request, css):
    return color_html(request, css, "css")

def css_rdf(request, css):
    return color_rdf(request, css, "css")

