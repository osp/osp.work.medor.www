# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_rubrics(apps, schema_editor):
    Article = apps.get_model("publish", "Article")
    Rubric = apps.get_model("publish", "Rubric")

    for article in Article.objects.all():
        kwargs = {
            'title': article.rubric_title,
            'subtitle': article.rubric_subtitle,
            'type': article.article_type,
        }
        obj, created = Rubric.objects.get_or_create(**kwargs)
        article.rubric = obj
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0018_auto_20160106_1546'),
    ]

    operations = [
        migrations.RunPython(populate_rubrics),
    ]
