# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import publish.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0008_article_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rubric_subtitle',
            field=models.CharField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='rubric_title',
            field=models.CharField(default='', max_length=1024, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(default=publish.models.body_default, blank=True),
            preserve_default=True,
        ),
    ]
