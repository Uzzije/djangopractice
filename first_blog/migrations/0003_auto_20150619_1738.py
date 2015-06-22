# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_blog', '0002_auto_20150619_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allentry',
            name='author',
        ),
        migrations.RemoveField(
            model_name='allentry',
            name='blog',
        ),
        migrations.DeleteModel(
            name='AllEntry',
        ),
    ]
