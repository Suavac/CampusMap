# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150218_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='courseCode',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lecCode',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='roomCode',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
