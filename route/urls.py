from django.conf.urls import patterns, url, include
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('route.views',
    url(r'^$', 'index', name="index"),
    url(r'^admin-view/', 'admin_view', name="admin-view"),
    url(r'^add-route/$', 'add_route', name="add-route"),
    url(r'^manage-route/$', 'manage_route', name="manage-route"),
)
