# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
        migrations.AlterField(
            model_name='module',
            name='modCode',
            field=models.CharField(serialize=False, primary_key=True, max_length=7),
            preserve_default=True,
        ),
    ]
