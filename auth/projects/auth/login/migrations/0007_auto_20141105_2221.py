# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20141105_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_faild_attept_time',
            field=models.DateTimeField(null=True, verbose_name=b'date of the first failed attempt', blank=True),
            preserve_default=True,
        ),
    ]
