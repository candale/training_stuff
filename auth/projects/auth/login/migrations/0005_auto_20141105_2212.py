# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20141105_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auth_log',
            name='user',
        ),
        migrations.DeleteModel(
            name='Auth_Log',
        ),
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='block_timestamp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='blocked',
        ),
        migrations.AddField(
            model_name='user',
            name='banned_until',
            field=models.DateTimeField(default=None, verbose_name=b'date until user is banned', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='failed_attempts_count',
            field=models.IntegerField(default=0, verbose_name=b'faild attempts count'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='first_faild_attept_time',
            field=models.DateTimeField(default=None, verbose_name=b'date of the first failed attempt', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=75, verbose_name=b'email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name=b'first name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name=b'is or not admint'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name=b'last name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'username'),
            preserve_default=True,
        ),
    ]
