# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20150220_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='buildingCode',
            field=models.CharField(max_length=7),
            preserve_default=True,
        ),
    ]
