# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20150220_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='buildingCode',
            field=models.ForeignKey(to='map.Building'),
            preserve_default=True,
        ),
    ]
