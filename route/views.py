import os
import json
import logging
import settings
import json
import urlparse
import HTMLParser
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import (
    render,
    render_to_response,
)
from django.template import RequestContext


def index(request, template='route/index.html'):
    context = {}
    return render_to_response(template, context, RequestContext(request))