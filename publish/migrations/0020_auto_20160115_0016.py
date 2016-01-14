# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0019_auto_20160106_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_type',
        ),
        migrations.RemoveField(
            model_name='article',
            name='rubric_subtitle',
        ),
        migrations.RemoveField(
            model_name='article',
            name='rubric_title',
        ),
        migrations.AlterField(
            model_name='article',
            name='rubric',
            field=models.ForeignKey(verbose_name='rubrique', blank=True, to='publish.Rubric', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlemembershipweb',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='ordre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlemembershipweb',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='publi\xe9 en ligne'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articlemembershipweb',
            name='web_publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de publication sur le web'),
            preserve_default=True,
        ),
    ]
