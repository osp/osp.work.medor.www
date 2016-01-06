# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0017_auto_20160106_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024, verbose_name='titre de la rubrique', blank=True)),
                ('subtitle', models.CharField(max_length=1024, verbose_name='sous-titre de la rubrique', blank=True)),
                ('type', models.CharField(max_length=1024, verbose_name="type d'article", blank=True)),
            ],
            options={
                'verbose_name': 'Rubrique',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='rubric',
            field=models.ForeignKey(blank=True, to='publish.Rubric', null=True),
            preserve_default=True,
        ),
    ]
