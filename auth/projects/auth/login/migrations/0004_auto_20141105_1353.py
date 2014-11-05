# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20141105_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='andrei', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='candale', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
            preserve_default=True,
        ),
    ]
