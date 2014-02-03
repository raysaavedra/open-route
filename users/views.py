from django.shortcuts import render_to_response
from django.template import RequestContext

def login_to_application(request, template='users/login.html'):
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))