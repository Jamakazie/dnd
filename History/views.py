from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def history_index(request):
	context = {}

	return render_to_response('history_index.html', context, context_instance = RequestContext(request))

def theterror(request):
	context = {}
	return render_to_response('history_terror.html', context, context_instance = RequestContext(request))
		
def ores(request):
	context = {}
	return render_to_response('history_ores.html', context, context_instance = RequestContext(request))

def nyrium(request):
	context = {}
	return render_to_response('history_nyrium.html', context, context_instance = RequestContext(request))
