# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20141105_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='banned_until',
            field=models.DateTimeField(null=True, verbose_name=b'date until user is banned', blank=True),
            preserve_default=True,
        ),
    ]
