from django.conf.urls import patterns, url, include
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('route.views',
    url(r'^$', 'index', name="route-index"),
    url(r'^add-route/$', 'add_route', name="add-route"),
)
