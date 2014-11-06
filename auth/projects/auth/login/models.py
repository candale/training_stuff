from django import forms
from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractBaseUser

import datetime


class UserManager(models.Manager):
    def authenticate(self, username, password):
        user = self.get_user(username=username)
        if user is None:
            raise ValueError("Invalid username or password")

        if user.is_banned():
            raise ValueError("You are blocked due to failed login attempts")

        if not user.check_password(password):
            user.notify_failed_login()
            raise ValueError("Invalid username or password")

        return True


    def get_user(self, username=None):
        if username is not None:
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                return None
            else:
                return user

class User(AbstractBaseUser):
    username = models.CharField('username', max_length=20, unique=True)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=50, blank=True)
    last_name  = models.CharField('last name', max_length=50, blank=True)
    is_admin = models.BooleanField('is or not admint', default=False)
    join_date = models.DateTimeField('Account creation date', auto_now_add=True)
    banned_until = models.DateTimeField('date until user is banned', blank=True, null=True)
    failed_attempts_count = models.IntegerField('faild attempts count', default=0)
    first_faild_attept_time =  models.DateTimeField('date of the first failed attempt', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    BAN_TIME = datetime.timedelta(seconds=10)
    COUNT_INTERVAL = datetime.timedelta(seconds=120)
    ATTEMPTS_COUNT = 3


    def _is_ban_active(self):
        now = timezone.now()
        return self.banned_until is not None and now < self.banned_until


    def _is_ban_info_none(self):
        return (self.first_faild_attept_time is None
                or self.failed_attempts_count is 0)

    def is_banned(self):
        if self._is_ban_active() is False:
            self.update_ban()

        return self._is_ban_active()


    def update_ban(self):
        now = timezone.now()

        # if the ban is no longer available
        if self.banned_until and self.banned_until <= now:
            self.banned_until = None
            self.first_faild_attept_time = None
            self.failed_attempts_count = 0

        if self._is_ban_info_none():
            return

        # if we need to set the ban
        if (now - User.COUNT_INTERVAL < self.first_faild_attept_time
                    and self.failed_attempts_count >= User.ATTEMPTS_COUNT):
            self.banned_until = now + User.BAN_TIME

        self.save()


    def notify_failed_login(self):
        now = timezone.now()

        if self.first_faild_attept_time is None:
            self.failed_attempts_count = 0
            self.first_faild_attept_time = now

        if now - User.COUNT_INTERVAL <= self.first_faild_attept_time:
            self.failed_attempts_count += 1
        else:
            self.first_faild_attept_time = None
            self.failed_attempts_count = 0

        self.save()


    def __str__(self):
        return self.username
