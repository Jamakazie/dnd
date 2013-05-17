from django.conf.urls import patterns, url

from Admin import views

urlpatterns = patterns('', 
	url(r'^$', views.admin_index, name='admin_index'),
	url(r'^Create', views.admin_create, name='admin_create'),
	url(r'^View', views.admin_view, name='admin_view'),
	url(r'^Ajax/Character', views.admin_ajax_character, name='admin_ajax_character'),
)
