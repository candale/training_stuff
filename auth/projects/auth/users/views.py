from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext

from users.models import User

def index(request):
	return HttpResponse('need to redirect if user already loggined')


def user(user, username):
	return HttpResponse(username)


def change_password(request, username):
	state = "Change password"
	if request.POST:
		old_password = request.POST.get('old_password')
		new_password = request.POST.get('new_password')
		new_password_again = request.POST.get('new_password_again:')

		try:
			if (User.objects.change_password(
						username, old_password, 
						new_password, new_password_again)):
				state = "An email was sent to your address"
				return render_to_response("users/changepass.html", {'register': False, 'state': state}, RequestContext(request))
		except ValueError as e:
			state = e.message

	return render_to_response('users/changepass.html', {'register': True, 'state': state}, RequestContext(request))


def login(request):
	state = "Please sign in below"
	if request.POST:
		username_form = request.POST.get('username')
		password_form = request.POST.get('password')

		try:
			if User.objects.authenticate(username_form, password_form):
				return redirect("/user/%s/" % username_form)
		except ValueError as e:
			state = e.message

	return render_to_response('users/login.html', {'state': state}, RequestContext(request))


def register(request):
	state = 'Register'
	if request.POST:
		data = request.POST.copy()
		try:
			User.objects.create_user(data)
		except ValueError as e:
			state = e.message
		else:
			return redirect('/user/login/')

