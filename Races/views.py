from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Races.models import race, race_desc

# Create your views here.
races = race.objects.all()
context = {}
context['races'] = races
def race_index(request):
	return render_to_response('race_index.html', context, context_instance = RequestContext(request))
