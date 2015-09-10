# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0010_auto_20150605_0222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleproposal',
            options={'ordering': ['-creation_date'], 'verbose_name': "Proposition d'article", 'verbose_name_plural': "Propositions d'articles"},
        ),
    ]
