# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20150220_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='building',
            new_name='buildingCode',
        ),
    ]
