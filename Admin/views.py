from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def admin_index(request):
	context = {}
	return render_to_response('admin_index.html', context, context_instance = RequestContext(request))
def admin_create(request):
	pass
def admin_view(request):
	pass