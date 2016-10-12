# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0011_auto_20150825_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleproposal',
            name='comment',
            field=models.TextField(help_text='On lui a dit quoi?', verbose_name='Commentaire', blank=True),
        ),
        migrations.AddField(
            model_name='articleproposal',
            name='is_answered',
            field=models.BooleanField(default=False, verbose_name='R\xe9pondu?'),
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='abstract',
            field=models.CharField(help_text=b'R\xc3\xa9digez comme s\xe2\x80\x99il s\xe2\x80\x99agissait d\xe2\x80\x99un chapeau destin\xc3\xa9 \xc3\xa0 un m\xc3\xa9dia g\xc3\xa9n\xc3\xa9raliste.', max_length=750, verbose_name=b'R\xc3\xa9sum\xc3\xa9', blank=True),
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='body',
            field=models.TextField(help_text=b'Pr\xc3\xa9sentez-vous et pr\xc3\xa9sentez-nous votre sujet\xc2\xa0: de quoi s\xe2\x80\x99agit-il, o\xc3\xb9 en \xc3\xaates-vous dans vos recherches, quelles sont vos pistes et hypoth\xc3\xa8ses, en quoi ce sujet est-il in\xc3\xa9dit, sous quelle forme l\xe2\x80\x99imaginez-vous, etc.\xc2\xa0?', verbose_name=b'Contenu', blank=True),
        ),
        migrations.AlterField(
            model_name='articleproposal',
            name='subject_title',
            field=models.CharField(help_text=b'Donnez un titre \xc3\xa0 votre proposition', max_length=300, verbose_name=b'Titre'),
        ),
    ]
