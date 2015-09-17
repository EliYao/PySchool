# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='describe',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
