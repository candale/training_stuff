# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20141105_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='block_timestamp',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
