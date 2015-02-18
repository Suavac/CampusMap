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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('buildingCode', models.CharField(max_length=7)),
                ('buildingName', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('courseCode', models.CharField(max_length=7)),
                ('courseName', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('lecCode', models.CharField(max_length=7)),
                ('lecFirst_Name', models.CharField(max_length=100)),
                ('lecLast_Name', models.CharField(max_length=100)),
                ('lecEmail', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('modCode', models.CharField(max_length=7)),
                ('modName', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('roomCode', models.CharField(max_length=7)),
                ('roomName', models.CharField(max_length=7)),
                ('lat', models.CharField(max_length=7)),
                ('lon', models.CharField(max_length=7)),
                ('building', models.ForeignKey(to='map.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
            unique_together=set([('courseCode', 'modCode', 'day', 'time')]),
        ),
    ]
