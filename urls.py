from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf.urls.i18n import i18n_patterns

from users.views import login_to_application

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^route/', include('route.urls', namespace='route')),
)

# users app
urlpatterns += patterns('',
    url(r'^login/$', login_to_application),
)