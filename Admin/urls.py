from django.conf.urls import patterns, url

from Admin import views

urlpatterns = patterns('', 
	url(r'^$', views.admin_index, name='admin_index'),
	url(r'^Create$', views.admin_create, name='admin_create'),
	url(r'^Create/Encounter$', views.admin_create_encounter, name='admin_create_encounter'),
	url(r'^Create/Encounter/Generate$', views.ajax_encounter, name='ajax_encounter'),
	url(r'^Create/Encounter/More$', views.ajax_admin_create_encounter, name='ajax_admin_create_encounter'),
	url(r'^View/Sheet', views.admin_view, name='admin_view'),
	url(r'^View/People', views.admin_view_people, name='admin_view_people'),
	url(r'^Person', views.admin_person, name='admin_person'),
	url(r'^Race/$', views.admin_race, name='admin_race'),
	url(r'^Race/(.*)', views.admin_race_edit, name='admin_race_edit'),
	url(r'^Ajax/Commit', views.commit, name='commit'),
	url(r'^Ajax/Character', views.admin_ajax_character, name='admin_ajax_character'),
	url(r'^Ajax/View/(.*)', views.ajax_view, name='ajax_view'),
	url(r'^Ajax/Person/View/(.*)', views.ajax_person_view, name='ajax_person_view'),
	url(r'^Ajax/Person/Delete/(.*)$', views.ajax_person_delete, name='ajax_person_delete'),
	url(r'^Ajax/Person/Update/$', views.ajax_person_update, name='ajax_person_update'),
	url(r'^Ajax/Person/NoSheet', views.ajax_person_nosheet, name='ajax_person_nosheet'),
	url(r'^Ajax/Person/Sheet', views.ajax_person_sheet, name='ajax_person_sheet'),
	url(r'^Ajax/Update/Race/$', views.ajax_update_race, name='ajax_update_race'),
	url(r'^Ajax/Sheet', views.ajax_create_sheet, name='ajax_create_sheet'),
)
