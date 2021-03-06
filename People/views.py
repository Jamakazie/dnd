from Admin.ajax import render_block_to_string
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from Admin.models import people as p
from django.template import RequestContext

# Create your views here.
def people_index(request):
	context = {}
	return render_to_response('people_index.html', context, RequestContext(request))
	
def people_view(request):
	context = {}
	context['people'] = p.objects.filter(isknown=True)
	return render_to_response('people_view.html', context, RequestContext(request))
def people_ajax_view(request, params):
	context = {}
	pid = params.split('/')
	pid = pid[0]
	person = p.objects.get(pk=pid)
	context['person'] = person
	return_str = render_block_to_string('people_ajax_view.html', 'person', context)
	return_str += render_block_to_string('people_ajax_view.html', 'buttons', context)
	return HttpResponse(return_str)
