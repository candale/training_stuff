from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext

from users.models import User

def index(request):
	user = User.objects.get_loggedin_user(request.session.session_key) 
	if user is not None:
		return redirect('/user/%s/' % user.username)
	else:
		return redirect('/user/login/')


def user(request, username):
	user = User.objects.get_user(username=username)
	if user is None or user.is_logged_in() is False:
		return redirect('/user/login/')
		
	info = dict()
	info['first_name'] = user.first_name
	info['last_name'] = user.last_name
	info['username'] = user.username
	info['email'] = user.email
	return render_to_response('users/user.html', info, RequestContext(request))


def logout(request, username):
	user = User.objects.get_user(username=username)
	user.logout()
	return redirect('/user/login/')


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
	user = User.objects.get_loggedin_user(request.session.session_key) 
	if user is not None:
		return redirect('/user/%s/' % user.username)

	state = "Please sign in below"
	if request.POST:
		username_form = request.POST.get('username')
		password_form = request.POST.get('password')

		try:
			user = User.objects.authenticate(username_form, password_form)
		except ValueError as e:
			state = e.message
		else:
			user.login(request.session.session_key)
			return redirect("/user/%s/" % username_form)

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


	return render_to_response('users/register.html', {'state': state}, RequestContext(request))

