# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0009_auto_20150528_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleproposal',
            name='abstract',
            field=models.CharField(help_text=b'R\xc3\xa9digez comme s\xe2\x80\x99il s\xe2\x80\x99agissait d\xe2\x80\x99un chapeau destin\xc3\xa9 \xc3\xa0 un m\xc3\xa9dia g\xc3\xa9n\xc3\xa9raliste.', max_length=750, verbose_name=b'R\xc3\xa9sum\xc3\xa9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='section',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'Destinez-vous votre sujet \xc3\xa0 une rubrique pr\xc3\xa9cise ?', verbose_name=b'Rubrique concern\xc3\xa9e (a priori)', choices=[(0, 'Enqu\xeate'), (1, 'Portrait ou r\xe9cit'), (2, 'Interview'), (3, 'Portfolio photo'), (4, 'Autre')]),
            preserve_default=True,
        ),
    ]
