# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    (r'^color$', lambda request: HttpResponsePermanentRedirect("/")),
    (r'^color/$', lambda request: HttpResponsePermanentRedirect("/")),
    (r'^favicon.ico', lambda request: HttpResponsePermanentRedirect("/resources/images/favicon.ico")),
    (r'^color/rgb/(?P<color>[0-9a-fA-F]{3})$', 'colors.views.color'),
    (r'^color/rgb/(?P<rgb>[0-9a-fA-F]{3}).html$', 'colors.views.rgb_html'),
    (r'^color/rgb/(?P<rgb>[0-9a-fA-F]{3}).rdf$', 'colors.views.rgb_rdf'),
    (r'^color/rgb/(?P<color>[0-9a-fA-F]{6})$', 'colors.views.color'),
    (r'^color/rgb/(?P<rgb>[0-9a-fA-F]{6}).html$', 'colors.views.rgb_html'),
    (r'^color/rgb/(?P<rgb>[0-9a-fA-F]{6}).rdf$', 'colors.views.rgb_rdf'),
    (r'^color/css/(?P<color>\w+)$', 'colors.views.color'),
    (r'^color/css/(?P<css>\w+).html$', 'colors.views.css_html'),
    (r'^color/css/(?P<css>\w+).rdf$', 'colors.views.css_rdf')
)

