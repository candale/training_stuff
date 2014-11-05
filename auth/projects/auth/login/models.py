from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import AbstractBaseUser
import datetime

# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    join_date = models.DateTimeField('Account creation date', auto_now_add=True)
    blocked = models.BooleanField(default=False)
    block_timestamp = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


    def block_unblock(self):
        now = timezone.now()
        # check if we are blocked and if we need to release the user
        if self.blocked == True:
            block_time = datetime.timedelta(minutes=2)
            if self.block_timestamp and now - self.block_timestamp >= block_time:
                self.blocked = False
                self.save()
                return False

        # check if we need to block the user
        delta = now - datetime.timedelta(seconds=30)
        # get a reference date from which to count the number of failed login attempts
        if self.block_timestamp != None:
            # get the greater date from the computed delta and the last date the user was blocked
            reference_date = delta if delta > self.block_timestamp else self.block_timestamp
        else:
            reference_date = delta

        result = self.auth_log_set.filter(timestamp__gt=reference_date, failed=True, log_type='IN')
        # if 3 or more failed attempts were made in the last
        if len(result) >= 3:
            self.blocked = True
            self.block_timestamp = timezone.now()
            self.save()
            return True

        return False


    def __str__(self):
        return self.username

class Auth_Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    LOG_TYPE = {('IN', 'Login'),
                ('OUT', 'Logout'),}
    log_type = models.CharField(max_length=15, choices=LOG_TYPE)
    failed = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True)
