# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0021_auto_20160714_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lead',
            field=ckeditor.fields.RichTextField(verbose_name='chapo', blank=True),
        ),
    ]
