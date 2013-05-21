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
