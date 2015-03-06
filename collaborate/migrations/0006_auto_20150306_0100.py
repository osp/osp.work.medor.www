# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0005_auto_20150203_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleproposal',
            options={'verbose_name': "Proposition d'article", 'verbose_name_plural': "Propositions d'articles"},
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='innovation',
            field=models.CharField(help_text=b'En quoi votre sujet est-il original par rapport \xc3\xa0 l\xe2\x80\x99offre m\xc3\xa9diatique francophone de Belgique ?', max_length=500, verbose_name=b'Originalit\xc3\xa9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='sectioning',
            field=models.CharField(help_text=b'Votre sujet se d\xc3\xa9cline-t-il en plusieurs entr\xc3\xa9es ? Sinon, le pourrait-il ?', max_length=500, verbose_name=b'D\xc3\xa9coupage'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='space',
            field=models.CharField(help_text=b"Une page M\xc3\xa9dor mesure 16 x 23 cm, soit environ 2000 signes. Quel serait, selon vous, l'espace n\xc3\xa9cessaire \xc3\xa0 votre contribution en nombre de pages ?", max_length=200, verbose_name=b'Format'),
            preserve_default=True,
        ),
    ]
