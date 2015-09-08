# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_course_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
