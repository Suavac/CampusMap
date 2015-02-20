# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20150218_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='id',
        ),
        migrations.AlterField(
            model_name='building',
            name='buildingCode',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
