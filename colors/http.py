# -*- coding: utf-8 -*-

# actually this code is from djubby, but it's the same problem, so same solution ;-)

import mimeparse
from django.http import HttpResponseRedirect
from sets import Set

formats = {
            "rdf"   : { "default":"application/rdf+xml", "xml":"application/rdf+xml", "n3":"text/n3" },
            "html"  : { "default":"text/html", "html":"text/html", "xhtml":"application/xhtml+xml" }
          }

def get_supported_formats():
    sf = Set()
    for f in formats.itervalues():
        for m in f.itervalues():
            sf.add(m)
    return list(sf)

def get_preferred_format(request):
    try:
        accept = request.META["HTTP_ACCEPT"]
    except KeyError:
        accept = formats["rdf"]["default"]
    return mimeparse.best_match(get_supported_formats(), accept)

def get_preferred_suffix(request):
    return get_suffix(get_preferred_format(request))

def get_suffix(mimetype):
    for suffix, f in formats.items():
        mimes = f.values()
        if mimetype in mimes:
            return suffix
    return "html"

class Http303(HttpResponseRedirect):
    status_code = 303

