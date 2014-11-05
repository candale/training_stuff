# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('log_type', models.CharField(max_length=15, choices=[(b'OUT', b'Logout'), (b'IN', b'Login')])),
                ('failed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('is_admin', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Account creation date')),
                ('blocked', models.BooleanField(default=False)),
                ('block_timestamp', models.DateTimeField(blank=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='auth_log',
            name='user',
            field=models.ForeignKey(to='login.User', null=True),
            preserve_default=True,
        ),
    ]
