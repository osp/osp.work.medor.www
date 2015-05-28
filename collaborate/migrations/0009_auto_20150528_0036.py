# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0008_auto_20150527_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleproposal',
            name='approach',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='belgian',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='difficulties',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='innovation',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='media',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='method',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='miscellaneous',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='partnership',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='sectioning',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='sources',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='space',
        ),
        migrations.RemoveField(
            model_name='articleproposal',
            name='term',
        ),
    ]
