# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='articleType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleType', verbose_name='文档类型'),
        ),
    ]
