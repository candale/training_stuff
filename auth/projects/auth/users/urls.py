from django.conf.urls import patterns, url, include

from users import views

urlpatterns = patterns('', 
		url(r'^$', views.index, name='index'),
		url(r'^login/', views.login, name='login'),
	    url(r'^(?P<username>\w+)/$', views.user, name='user'),
		url(r'^(?P<username>\w+)/changepass/', views.change_password, name='changepass'),
)
