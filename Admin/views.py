import math
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from Admin.models import character as c
from Admin.ajax import render_block_to_string
from Admin.character_gen import fighter, character, priest, rogue, mage
import json

# Create your views here.
def admin_index(request):
	context = {}
	return render_to_response('admin_index.html', context, context_instance = RequestContext(request))
def admin_create(request):
	context = {}
	return render_to_response('admin_create.html', context, context_instance=RequestContext(request))
def admin_view(request):
	context = {}
	context['characters'] = c.objects.all()
	return render_to_response('admin_view.html', context, context_instance = RequestContext(request))
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
def commit(request):
	character = request.session['generated']
	character.commit()
	request.session['generated'] = None
	return HttpResponse("success")

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

def admin_person(request):
	context = {}
	return render_to_response('admin_person.html', context, context_instance = RequestContext(request))

def statMods(stats, context):
	context['strMod'] = toMod(stats['strength'])
	context['dexMod'] = toMod(stats['dexterity'])
	context['conMod'] = toMod(stats['constitution'])
	context['wisMod'] = toMod(stats['wisdom'])
	context['intMod'] = toMod(stats['intelligence'])
	context['chaMod'] = toMod(stats['charisma'])

def toMod(stat):
	mod = math.floor((stat - 10) / 2)
	if( mod >= 0):
		return "+" + str(int(mod))
	else:
		return str(int(mod))
