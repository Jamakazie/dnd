from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_index(request):
	context = {}
	return render_to_response('login.html', context, context_instance = RequestContext(request))

def login_auth(request):
	user = request.POST['username']
	password = request.POST['password']

	authuser = authenticate(username = user, password=password)
	if authuser is not None:
		if authuser.is_active:
			login(request, authuser)
			return HttpResponse("Success")
		else:
			return HttpResponse("Failure")
	else:
		return HttpResponse("Failure")
def login_logout(request):
	logout(request)
	return HttpResponseRedirect("/")
