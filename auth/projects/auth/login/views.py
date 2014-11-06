from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from login.models import User


def login(request):
	username = password = ''
	state = "Please sign in below..."
	if request.POST:
		username_form = request.POST.get('username')
		password_form = request.POST.get('password')

		try:
			if User.objects.authenticate(username_form, password_form) is True:
				return redirect("/user/%s/" % username_form)
		except ValueError as e:
			state = e.message

	return render_to_response('login/login.html', {'state': state}, RequestContext(request))
