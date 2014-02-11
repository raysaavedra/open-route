import os
import json
import logging
import settings
import json
import urlparse
import HTMLParser
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from route import models
from django.contrib.gis.geos import Point, LineString

def index(request, template='route/index.html'):
    context = {}
    if request.method == "GET":
        context['routes'] = models.route.objects.all()
    return render_to_response(template, context, RequestContext(request))

def admin_view(request, template='route/admin-view.html'):
    context = {}
    return render_to_response(template, context, RequestContext(request))

def manage_route(request, template='route/manage_route.html'):
    context = {}

    if request.method == "GET":
        context['routes'] = models.route.objects.all()
    elif request.method == "POST" and request.is_ajax():
        route_n = request.POST.get('route_name')
        route_d = request.POST.get('route_destination')
        points = request.POST.getlist('points[]')

        p1 = points[0].find(',')
        np1 = Point(float(points[0][0:p1]),float(points[0][p1+1:]))

        p2 = points[len(points)-1].find(',')
        np2 = Point(float(points[len(points)-1][0:p1]),float(points[len(points)-1][p2+1:]))

        route_points = []
        i = 0

        for pp in points:
            c1 = points[i].find(',')
            cp1 = (float(points[i][0:c1]),float(points[i][c1+1:]))
            route_points.append(cp1)
            i = i + 1

        rout = LineString(route_points)

        #nroute = models.route(route_name = route_n, destination = route_d)
        #nroute.start_point = np1
        #nroute.end_point = np2
        #nroute.route_points = rout
       # nroute.save()

    return render_to_response(template, context, RequestContext(request))


def add_route(request, template='route/add_route.html'):
    context = {}

    if request.method == "POST" and request.is_ajax():
        route_n = request.POST.get('route_name')
        route_d = request.POST.get('route_destination')
        points = request.POST.getlist('points[]')

        p1 = points[0].find(',')
        np1 = Point(float(points[0][0:p1]),float(points[0][p1+1:]))

        p2 = points[len(points)-1].find(',')
        np2 = Point(float(points[len(points)-1][0:p2]),float(points[len(points)-1][p2+1:]))

        route_points = []
        i = 0

        for pp in points:
            c1 = points[i].find(',')
            cp1 = (float(points[i][0:c1]),float(points[i][c1+1:]))
            route_points.append(cp1)
            i = i + 1

        rout = LineString(route_points)

        nroute = models.route(route_name = route_n, destination = route_d)
        nroute.start_point = np1
        nroute.end_point = np2
        nroute.route_points = rout
        nroute.save()

    return render_to_response(template, context, RequestContext(request))





