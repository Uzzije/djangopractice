# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user_first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='user_last_name',
        ),
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
