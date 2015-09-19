# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_folder_describe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Name',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Content',
            field=DjangoUeditor.models.UEditorField(default=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe4\xbd\xa0\xe6\x83\xb3\xe8\xa6\x81\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9\xe3\x80\x82', verbose_name=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_image', blank=True),
        ),
    ]
