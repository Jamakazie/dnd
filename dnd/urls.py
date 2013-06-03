from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dnd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('main.urls')),
    url(r'^Races/', include('Races.urls')),
    url(r'^History/', include('History.urls')),
    url(r'^Admin/', include('Admin.urls')),
    url(r'^People/', include('People.urls')),
    url(r'^Login/', include('Login.urls')),
)
W