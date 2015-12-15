# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=75)),
                ('date', models.DateField(auto_now=True)),
                ('text', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to=blog.models.upload_handler)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
    ]
