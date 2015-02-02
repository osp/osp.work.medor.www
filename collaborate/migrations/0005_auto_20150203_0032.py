# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0004_auto_20150202_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleproposal',
            name='miscellaneous',
            field=models.CharField(help_text=b'Avez-vous une remarque ou une demande particuli\xc3\xa8re li\xc3\xa9e \xc3\xa0 votre proposition ?', max_length=500, verbose_name=b'Divers', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='space',
            field=models.CharField(help_text=b"Une page M\xc3\xa9dor mesure 16 x 23 cm, soit environ 2000 signes. Quelle serait, selon vous, l'espace n\xc3\xa9cessaire \xc3\xa0 votre contribution en nombre de pages ?", max_length=200, verbose_name=b'Format'),
            preserve_default=True,
        ),
    ]
