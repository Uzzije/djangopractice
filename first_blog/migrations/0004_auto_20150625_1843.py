# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_blog', '0003_auto_20150619_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
        migrations.RemoveField(
            model_name='author',
            name='user_name',
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=b'', to=settings.AUTH_USER_MODEL),
        ),
    ]
