# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=20, verbose_name=b'username')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=50, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=50, verbose_name=b'last name', blank=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name=b'is or not admint')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Account creation date')),
                ('banned_until', models.DateTimeField(null=True, verbose_name=b'date until user is banned', blank=True)),
                ('failed_attempts_count', models.IntegerField(default=0, verbose_name=b'faild attempts count')),
                ('first_faild_attept_time', models.DateTimeField(null=True, verbose_name=b'date of the first failed attempt', blank=True)),
                ('session_id', models.CharField(unique=True, max_length=40, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
