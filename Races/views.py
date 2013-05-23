from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Races.models import race, race_desc

# Create your views here.
races = race.objects.all()
context = {}
context['races'] = sorted(races)
def race_index(request):
	return render_to_response('race_index.html', context, context_instance = RequestContext(request))

def info(request, params):
	race_name = params.split('/')
	race_name = race_name[0]
	if len(race_name) is 0:
		race_name = "You shouldn't be here"
	context['race_name'] = race_name
	desc = race.objects.get(race_name=race_name).race_desc_set.all()
	if desc.count() > 0:
		context['information'] = desc[0]
	else:
		context['information'] = ""
	return render_to_response('race_info.html', context, context_instance = RequestContext(request))
