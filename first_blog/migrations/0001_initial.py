# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_first_name', models.CharField(max_length=200)),
                ('user_last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_created', models.DateField()),
                ('author', models.ForeignKey(to='first_blog.Author')),
            ],
        ),
        migrations.AddField(
            model_name='allentry',
            name='author',
            field=models.ForeignKey(to='first_blog.Author'),
        ),
        migrations.AddField(
            model_name='allentry',
            name='blog',
            field=models.ManyToManyField(to='first_blog.Blog'),
        ),
    ]
