import math
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from Admin.models import character as c, people as p, people_dm as pdm
from Races.models import race as r, race_desc as rd
from Admin.ajax import render_block_to_string
from Admin.character_gen import fighter, character, priest, rogue, mage
import json

# Create your views here.
@login_required
def admin_index(request):
	context = {}
	return render_to_response('admin_index.html', context, context_instance = RequestContext(request))
@login_required
def admin_create(request):
	context = {}
	return render_to_response('admin_create.html', context, context_instance=RequestContext(request))
@login_required
def admin_view(request):
	context = {}
	context['characters'] = c.objects.all()
	return render_to_response('admin_view.html', context, context_instance = RequestContext(request))
@login_required
def admin_view_people(request):
	context = {}
	context['people'] = p.objects.all()
	return render_to_response('admin_view_people.html', context, context_instance = RequestContext(request))
@login_required
def admin_ajax_character(request):
	name = request.GET['name']
	level = request.GET['level']
	race = request.GET['race']
	cclass = request.GET['class']
	char = None
	if (cclass == "Fighter"):
		char = fighter.Fighter(level, race, name)
	elif(cclass == "Rogue"):
		char = rogue.Rogue(level, race, name)
	elif(cclass == "Priest"):
		char = priest.Priest(level, race, name)
	elif(cclass == "Mage"):
		char = mage.Mage(level, race, name)
	context = {}
	request.session['generated'] = char 
	context['c'] =char 
	statMods(char.stats.__dict__, context)
	return_str = render_block_to_string('char_ajax.html', 'charinfo', context)
	return_str += render_block_to_string('char_ajax.html', 'commit', context)
	return HttpResponse(return_str)
@login_required
def ajax_person_update(request):
	pid = request.POST['pk']
	title = request.POST['title']
	race = request.POST['race']
	name = request.POST['name']
	if 'ismet' in request.POST:
		isMet = True
	else:
		isMet = False
	if 'isknown' in request.POST:
		isKnown = True
	else:
		isKnown = False
	desc = request.POST['desc']
	dm_desc = request.POST['dm_desc']
	person = p.objects.get(pk=pid)
	person.isknown = isKnown
	person.race = race
	person.ismet = isMet
	person.description = desc
	person.name = name
	person.title = title
	person.save()
	try:
		p_dm = person.people_dm_set.all()[0]
	except: 
		p_dm = person.people_dm_set.create(dm_desc=dm_desc)
	p_dm.save()
	return HttpResponse("Success")




@login_required
def ajax_person_view(request, params):
	pid = params.split('/')
	pid = params[0]
	person = p.objects.get(pk=pid)
	context = {}
	context['person'] = person
	if person.isknown:
		context['isknown'] = 'checked'
	if person.ismet:
		context['ismet'] = 'checked'
	try:
		person_dm = person.people_dm_set.all()[0]
		context['dm_desc'] = person_dm.dm_desc
	except:
		pass
	context['disabled'] = 'disabled'
	#return_str = render_block_to_string('admin_person.html', 'person', context)
	#return_str += render_block_to_string('admin_person.html', 'view', context)
	#return HttpResponse(return_str)
	return render_to_response('admin_person.html', context, context_instance = RequestContext(request))

@login_required
def commit(request):
	character = request.session['generated']
	character.charmod()
	character.commit()
	request.session['generated'] = None
	return HttpResponse("success")

@login_required
def ajax_view(request, params):
	context = {}
	param = params.split('/')
	i = param[0]
	charfromdb = c.objects.get(pk=i)
	char = character.Character('20', 'temp', 'lol')
	char.fromCharacterDB(charfromdb)
	context['c'] = char
	statMods(char.stats, context)
	return_str = render_block_to_string('char_ajax.html', 'charinfo', context)
	return_str += render_block_to_string('char_ajax.html', 'view', context)
	return HttpResponse(return_str)

@login_required
def ajax_update_race(request):
#	try:
	race = request.POST['race']
	race_desc = request.POST['race_desc']
	race_srd = request.POST['race_srd']
	race_stats = request.POST['race_stats']
	race_skills = request.POST['race_skills']
	race_misc = request.POST['race_misc']
	try:
		r_id = r.objects.filter(race_name=race)[0].race_desc_set.all()[0]
		r_id.race_desc = race_desc
		r_id.race_stats = race_stats
		r_id.race_srd = race_srd
		r_id.race_skils = race_skills
		r_id.race_misc = race_misc
	except:
		r_id = r.objects.filter(race_name=race)[0].race_desc_set.create(race_desc=race_desc, race_srd=race_srd, race_stats=race_stats, race_skills=race_skills, race_misc=race_misc)

	r_id.save()
	return HttpResponse("Success")
#	except:
#		return HttpResponse("Failure")

@login_required
def admin_person(request):
	context = {}
	return render_to_response('admin_person.html', context, context_instance = RequestContext(request))

@login_required
def admin_race(request):
	context = {}
	context['races'] = r.objects.all()
	return render_to_response('admin_race.html', context, context_instance = RequestContext(request))

@login_required
def admin_race_edit(request, params):
	context = {}
	race = params.split('/')[0]
	context['race_name'] = race
	try:
		context['race'] = r.objects.filter(race_name=race)[0].race_desc_set.all()[0]
	except:
		pass
	return render_to_response('admin_race_edit.html', context, context_instance = RequestContext(request))


def statMods(stats, context):
	context['strMod'] = toMod(stats['strength'])
	context['dexMod'] = toMod(stats['dexterity'])
	context['conMod'] = toMod(stats['constitution'])
	context['wisMod'] = toMod(stats['wisdom'])
	context['intMod'] = toMod(stats['intelligence'])
	context['chaMod'] = toMod(stats['charisma'])

@login_required
def ajax_create_sheet(request):
	context = {}
	return_str = render_block_to_string('admin_create.html', 'sheet', context)
	return HttpResponse(return_str)

@login_required
def ajax_person_nosheet(request):
	title = request.POST['title']
	name = request.POST['name']
	race = request.POST['race']
	desc = request.POST['desc']
	if 'ismet' in request.POST:
		isMet = True
	else:
		isMet = False
	if 'isknown' in request.POST:
		isKnown = True
	else:
		isKnown = False
	dm_desc = request.POST['dm_desc']
	person = p(isknown = isKnown, ismet = isMet, description = desc, race = race, name = name, title = title, skill_sheet = None)
	person.save()
	person_dm = pdm(dm_desc = dm_desc, p_id = person)
	person_dm.save()
	return HttpResponse("Success")

@login_required
def ajax_person_sheet(request):
	title = request.POST['title']
	name = request.POST['name']
	race = request.POST['race']
	desc = request.POST['desc']
	if 'ismet' in request.POST:
		isMet = True
	else:
		isMet = False
	if 'isknown' in request.POST:
		isKnown = True
	else:
		isKnown = False
	dm_desc = request.POST['dm_desc']
	character = request.session['generated'].charmod()
	character.save()
	person = p(isknown = isKnown, ismet = isMet, description = desc, race = race, name = name, title = title, skill_sheet = character)
	person.save()
	person_dm = pdm(dm_desc = dm_desc, p_id = person)
	person_dm.save()
	request.session['generated'] = None
	return HttpResponse("Success")

@login_required
def ajax_person_delete(request, params):
	p_id = params.split('/')[0]
	try:
		person = p.objects.get(pk=p_id)
		person.delete()
		return HttpResponse("Success")
	except:
		return HttpResponse("There was an error ;-;")
@login_required
def ajax_encounter(request):
	level = 10
	race = "Human"
	name = "test dude"
	char = fighter.Fighter(level, race, name)
	context = {}
	context['person'] = char
	statMods(char.stats.__dict__, context)
	render_str = render_block_to_string('ajax_enc_char.html', 'encounter', context)
	return HttpResponse(render_str)

@login_required
def admin_create_encounter(request):
	context = {}
	return render_to_response("admin_create_encounter.html", context, context_instance = RequestContext(request))
def toMod(stat):
	mod = math.floor((stat - 10) / 2)
	if( mod >= 0):
		return "+" + str(int(mod))
	else:
		return str(int(mod))
