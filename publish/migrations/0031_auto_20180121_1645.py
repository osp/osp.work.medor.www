# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-21 15:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0030_issue_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='biography',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
