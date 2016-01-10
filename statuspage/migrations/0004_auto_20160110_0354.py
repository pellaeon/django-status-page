# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuspage', '0003_auto_20151105_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='changes',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='incidents',
        ),
        migrations.RemoveField(
            model_name='service',
            name='hosts',
        ),
        migrations.RemoveField(
            model_name='service',
            name='monitors',
        ),
        migrations.AddField(
            model_name='host',
            name='service',
            field=models.ForeignKey(default=1, to='statuspage.Service'),
        ),
        migrations.AddField(
            model_name='incident',
            name='monitor',
            field=models.ForeignKey(default=1, to='statuspage.Monitor'),
        ),
        migrations.AddField(
            model_name='incidentchange',
            name='incident',
            field=models.ForeignKey(default=1, to='statuspage.Incident'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='service',
            field=models.ForeignKey(blank=True, to='statuspage.Service', null=True),
        ),
    ]
