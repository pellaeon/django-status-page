# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuspage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitor',
            name='incidents',
            field=models.ManyToManyField(to='statuspage.Incident', blank=True),
        ),
    ]
