# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('buildingName', models.CharField(max_length=75, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseCode', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('courseName', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('depName', models.CharField(max_length=70, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lecCode', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('lecFirst_Name', models.CharField(max_length=50)),
                ('lecLast_Name', models.CharField(max_length=50)),
                ('lecEmail', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('modCode', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('modName', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomCode', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('roomName', models.CharField(max_length=30)),
                ('lat', models.FloatField(max_length=9)),
                ('lon', models.FloatField(max_length=9)),
                ('building', models.ForeignKey(to='map.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=1)),
                ('semester', models.CharField(max_length=1)),
                ('day', models.CharField(max_length=7)),
                ('time', models.CharField(max_length=7)),
                ('courseCode', models.ForeignKey(to='map.Course')),
                ('lecCode', models.ForeignKey(to='map.Lecturer')),
                ('modCode', models.ForeignKey(to='map.Module')),
                ('roomCode', models.ForeignKey(to='map.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together=set([('year', 'semester', 'courseCode', 'modCode', 'day', 'time')]),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(to='map.Department'),
            preserve_default=True,
        ),
    ]
