from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from Admin.models import character
from Admin.ajax import render_block_to_string
from Admin.character_gen import fighter
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
	context['characters'] = character.objects.all()
	return render_to_response('admin_view.html', context, context_instance = RequestContext(request))
def admin_ajax_character(request):
	name = request.GET['name']
	level = request.GET['level']
	cclass = request.GET['class']
	response = name + level + cclass
	fig = fighter.Fighter(level, 'Orc', cclass, name)
	context = {}
	request.session['generated'] = fig
	context['c'] = fig
	return_str = render_block_to_string('char_ajax.html', 'charinfo', context)
	return HttpResponse(return_str)
def commit(request):
	character = request.session['generated']
	character.commit()
	return HttpResponse("success")
