from django.conf.urls import patterns, url

from History import views

urlpatterns = patterns('',
	url(r'^$', views.history_index, name='history_index'),
	url(r'^Terror$', views.theterror, name='theterror'),
	url(r'^Nyrium$', views.nyrium, name='nyrium'),
	url(r'^Ores$', views.ores, name='ores'),

)
