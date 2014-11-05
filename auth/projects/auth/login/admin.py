from django.contrib import admin
from login.models import User, Auth_Log

# Register your models here.
admin.site.register(User)
admin.site.register(Auth_Log)
