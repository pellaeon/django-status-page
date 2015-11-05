# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fqdn', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentChange',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(choices=[('D', 'Down'), ('V', 'Investigating'), ('I', 'Identified'), ('W', 'Watching'), ('F', 'Fixed')], max_length=1, default='D')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(choices=[('D', 'Down'), ('U', 'Up'), ('P', 'Partial down'), ('M', 'Maintaining')], max_length=1, default='U')),
                ('incidents', models.ManyToManyField(null=True, to='statuspage.Incident', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='changes',
            field=models.ManyToManyField(to='statuspage.IncidentChange'),
        ),
    ]
