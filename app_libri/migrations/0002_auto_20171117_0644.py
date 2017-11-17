# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_libri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='asin',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='autore',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='titolo',
            field=models.CharField(max_length=250),
        ),
    ]