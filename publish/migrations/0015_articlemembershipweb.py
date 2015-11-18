# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0014_article_override_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleMembershipWeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('web_publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(to='publish.Article')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
    ]
