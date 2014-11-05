from django.shortcuts import render
from django.http import HttpResponse

def user(user, username):
	return HttpResponse(username)
