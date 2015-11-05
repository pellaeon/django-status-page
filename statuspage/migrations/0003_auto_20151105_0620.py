# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuspage', '0002_auto_20151105_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(default='Unnamed service', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='monitors',
            field=models.ManyToManyField(blank=True, to='statuspage.Monitor'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='name',
            field=models.CharField(default='Unnamed monitor', max_length=255),
        ),
        migrations.AddField(
            model_name='service',
            name='hosts',
            field=models.ManyToManyField(blank=True, to='statuspage.Host'),
        ),
        migrations.AddField(
            model_name='service',
            name='monitors',
            field=models.ManyToManyField(blank=True, to='statuspage.Monitor'),
        ),
    ]
