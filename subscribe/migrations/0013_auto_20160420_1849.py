# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0012_auto_20151229_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='from_issue',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='\xe0 partir du num\xe9ro', choices=[(None, '---'), (1, 'du 1 au 4'), (2, 'du 2 au 5'), (3, 'du 3 au 6'), (4, 'du 4 au 7'), (5, 'du 5 au 8'), (6, 'du 6 au 9')]),
            preserve_default=True,
        ),
    ]
