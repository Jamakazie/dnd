from django.conf.urls import patterns, url

from Login import views

urlpatterns = patterns('', 
	url(r'^$', views.login_index, name="login_index"),
	url(r'^Auth/$', views.login_auth, name="login_auth"),
	url(r'^Logout/$', views.login_logout, name="login_logout"),
)
