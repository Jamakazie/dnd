from django.conf.urls import patterns, url

from Admin import views

urlpatterns = patterns('', 
	url('^$', views.admin_index, name='admin_index'),
	url('^Create', views.admin_create, name='admin_create'),
	url('^View', views.admin_view, name='admin_view'),
)
