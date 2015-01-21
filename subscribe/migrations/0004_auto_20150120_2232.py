# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20141210_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='country',
            field=models.CharField(default=b'BE', max_length=5, verbose_name=b'pays', choices=[(b'AL', b'Albanie'), (b'PT-20', b'A\xc3\xa7ores'), (b'DE', b'Allemagne'), (b'AD', b'Andorre'), (b'AT', b'Autriche'), (b'BE', 'Belgique'), (b'BY', b'Bi\xc3\xa9lorussie'), (b'BA', b'Bosnie-Herz\xc3\xa9govine'), (b'BG', b'Bulgarie'), (b'IC', b'Canaries (\xc3\x8eles)'), (b'ES-CE', b'Ceuta'), (b'CY', b'Chypre'), (b'HR', b'Croatie'), (b'DK', b'Danemark'), (b'ES', b'Espagne'), (b'EE', b'Estonie'), (b'FO', b'F\xc3\xa9ro\xc3\xa9 (\xc3\x8eles)'), (b'FI', b'Finlande'), (b'FR', b'France (sauf DOM-TOM)'), (b'GE', b'G\xc3\xa9orgie'), (b'GI', b'Gibraltar'), (b'GB', b'Grande-Bretagne'), (b'GR', b'Gr\xc3\xa8ce'), (b'GL', b'Groenland'), (b'GG', b'Guernesey'), (b'HU', b'Hongrie'), (b'IE', b'Irlande'), (b'IS', b'Islande'), (b'IT', b'Italie'), (b'JE', b'Jersey'), (b'LV', b'Lettonie'), (b'LI', b'Liechtenstein'), (b'LT', b'Lituanie'), (b'LU', b'Luxembourg (Grand-Duch\xc3\xa9 de)'), (b'MK', b'Mac\xc3\xa9doine'), (b'PT-30', b'Mad\xc3\xa8re'), (b'MT', b'Malte'), (b'IM', b'Man (\xc3\x8ele de)'), (b'Me', b'Melilla'), (b'MD', b'Moldavie'), (b'MC', b'Monaco'), (b'ME', b'Mont\xc3\xa9n\xc3\xa9gro'), (b'NO', b'Norv\xc3\xa8ge'), (b'NL', b'Pays-Bas'), (b'PL', b'Pologne'), (b'PT', b'Portugal'), (b'CZ', b'R\xc3\xa9publique tch\xc3\xa8que'), (b'RO', b'Roumanie'), (b'RU', b'Russie'), (b'SM', b'Saint-Martin'), (b'RS', b'Serbie'), (b'SK', b'Slovaquie'), (b'SI', b'Slov\xc3\xa9nie'), (b'SE', b'Su\xc3\xa8de'), (b'CH', b'Suisse'), (b'TR', b'Turquie'), (b'UA', b'Ukraine'), (b'VA', b'Vatican')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='country',
            field=models.CharField(default=b'BE', max_length=5, verbose_name=b'pays', choices=[(b'AL', b'Albanie'), (b'PT-20', b'A\xc3\xa7ores'), (b'DE', b'Allemagne'), (b'AD', b'Andorre'), (b'AT', b'Autriche'), (b'BE', 'Belgique'), (b'BY', b'Bi\xc3\xa9lorussie'), (b'BA', b'Bosnie-Herz\xc3\xa9govine'), (b'BG', b'Bulgarie'), (b'IC', b'Canaries (\xc3\x8eles)'), (b'ES-CE', b'Ceuta'), (b'CY', b'Chypre'), (b'HR', b'Croatie'), (b'DK', b'Danemark'), (b'ES', b'Espagne'), (b'EE', b'Estonie'), (b'FO', b'F\xc3\xa9ro\xc3\xa9 (\xc3\x8eles)'), (b'FI', b'Finlande'), (b'FR', b'France (sauf DOM-TOM)'), (b'GE', b'G\xc3\xa9orgie'), (b'GI', b'Gibraltar'), (b'GB', b'Grande-Bretagne'), (b'GR', b'Gr\xc3\xa8ce'), (b'GL', b'Groenland'), (b'GG', b'Guernesey'), (b'HU', b'Hongrie'), (b'IE', b'Irlande'), (b'IS', b'Islande'), (b'IT', b'Italie'), (b'JE', b'Jersey'), (b'LV', b'Lettonie'), (b'LI', b'Liechtenstein'), (b'LT', b'Lituanie'), (b'LU', b'Luxembourg (Grand-Duch\xc3\xa9 de)'), (b'MK', b'Mac\xc3\xa9doine'), (b'PT-30', b'Mad\xc3\xa8re'), (b'MT', b'Malte'), (b'IM', b'Man (\xc3\x8ele de)'), (b'Me', b'Melilla'), (b'MD', b'Moldavie'), (b'MC', b'Monaco'), (b'ME', b'Mont\xc3\xa9n\xc3\xa9gro'), (b'NO', b'Norv\xc3\xa8ge'), (b'NL', b'Pays-Bas'), (b'PL', b'Pologne'), (b'PT', b'Portugal'), (b'CZ', b'R\xc3\xa9publique tch\xc3\xa8que'), (b'RO', b'Roumanie'), (b'RU', b'Russie'), (b'SM', b'Saint-Martin'), (b'RS', b'Serbie'), (b'SK', b'Slovaquie'), (b'SI', b'Slov\xc3\xa9nie'), (b'SE', b'Su\xc3\xa8de'), (b'CH', b'Suisse'), (b'TR', b'Turquie'), (b'UA', b'Ukraine'), (b'VA', b'Vatican')]),
            preserve_default=True,
        ),
    ]
