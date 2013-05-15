from django.conf.urls import patterns, url

from Races import views

urlpatterns = patterns('', 
	url(r'^$', views.race_index, name='race_index'),
	url(r'^Info/(.*)', views.info, name='info'),
)
