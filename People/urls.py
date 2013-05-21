from django.conf.urls import url, patterns
from People import views

urlpatterns = patterns('', 
	url(r'^$', views.people_index, name='people_index'),
	url(r'^View/', views.people_view, name='people_view'),
	url(r'^Person/(.*)', views.people_ajax_view, name='people_ajax_view'),

)
