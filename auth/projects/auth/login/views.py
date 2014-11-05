from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from login.models import User, Auth_Log


def login(request):
	username = password = ''
	state = "Please sign in below..."
	if request.POST:
		username_form = request.POST.get('username')
		password_form = request.POST.get('password')

		try:
			user = User.objects.get(username=username_form)
		except ObjectDoesNotExist:
			state = "Invalid username or password"
		else:
			user.block_unblock()
			if not user.blocked:
				if user.check_password(password_form):
					log = Auth_Log(failed=False, log_type='IN')
					user.auth_log_set.add(log)
					return redirect("/user/%s/" % user.username)
				else:
					state = "Invalid username or password"

				log = Auth_Log(failed=True, log_type='IN')
				user.auth_log_set.add(log)	
			else:
				state = "You are blocked because you're stupid"
	
	return render_to_response('login/login.html', {'state': state}, RequestContext(request))
