# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='session_id',
            field=models.CharField(max_length=40, unique=True, null=True),
            preserve_default=True,
        ),
    ]
