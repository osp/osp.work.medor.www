# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'nom')),
                ('email', models.EmailField(max_length=75, verbose_name=b'courriel')),
                ('phone', models.CharField(max_length=50, verbose_name=b't\xc3\xa9l\xc3\xa9phone', blank=True)),
                ('twitter_account', models.CharField(max_length=100, verbose_name=b'compte twitter', blank=True)),
                ('address', models.TextField(verbose_name=b'adresse')),
                ('subject_title', models.CharField(help_text=b'Titre le plus clair possible. Avec sous-titre \xc3\xa9ventuel.', max_length=300, verbose_name=b'intitul\xc3\xa9 du sujet (provisoire)', blank=True)),
                ('is_urgent', models.BooleanField(default=False, help_text=b"Votre sujet n\xc3\xa9cessite-t-il une publication rapide sur le web ou sur papier (pour pr\xc3\xa9server l'exclusivit\xc3\xa9 par exemple) ?", verbose_name=b'Urgence')),
                ('abstract', models.CharField(help_text=b'R\xc3\xa9digez comme s\xe2\x80\x99il s\xe2\x80\x99agissait d\xe2\x80\x99un chapeau destin\xc3\xa9 \xc3\xa0 un m\xc3\xa9dia g\xc3\xa9n\xc3\xa9raliste \xe2\x80\x94 750 signes maximum.', max_length=750, verbose_name=b'r\xc3\xa9sum\xc3\xa9 (pr\xc3\xa9visionnel)', blank=True)),
                ('media', models.CharField(help_text=b'Quelle(s) contribution(s) envisagez-vous? \xc3\x89crits, photographies, dessins, peintures, infographies, vid\xc3\xa9o, son, jeux de r\xc3\xb4les, autres (pr\xc3\xa9cisez) \xe2\x80\x94 200 signes maximum.', max_length=200, verbose_name=b'm\xc3\xa9dia', blank=True)),
                ('partnership', models.CharField(help_text=b'Quelle synergie serait possible entre votre projet et un autre correspondant de M\xc3\xa9dor : \xc3\xa9crits, photographies, dessins, peintures, infographies, vid\xc3\xa9o, son, jeux de r\xc3\xb4les, autres (pr\xc3\xa9cisez) \xe2\x80\x94 200 signes maximum.', max_length=200, verbose_name=b'partenariat', blank=True)),
                ('section', models.CharField(help_text=b'Destinez-vous votre sujet \xc3\xa0 une rubrique pr\xc3\xa9cise ? Entretien, portrait, r\xc3\xa9cit, enqu\xc3\xaate, br\xc3\xa8ves \xe2\x80\x94 200 signes maximum.', max_length=200, verbose_name=b'rubrique concern\xc3\xa9e (a priori)', blank=True)),
                ('space', models.FloatField(help_text=b"Une page M\xc3\xa9dor mesure 16x23 cm, soit environ 2000 signes. Quelle serait, selon vous, l'espace n\xc3\xa9cessaire \xc3\xa0 votre contribution en nombre de pages?", verbose_name=b'format')),
                ('sectioning', models.CharField(help_text=b'Votre sujet se d\xc3\xa9cline-t-il en plusieurs entr\xc3\xa9es ? Sinon, le pourrait-il ? O\xc3\xb9 va votre pr\xc3\xa9f\xc3\xa9rence et pourquoi ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'd\xc3\xa9coupage', blank=True)),
                ('innovation', models.CharField(help_text=b'En quoi votre sujet est-il innovant par rapport \xc3\xa0 l\xe2\x80\x99offre m\xc3\xa9diatique francophone de Belgique ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'innovation', blank=True)),
                ('belgian', models.CharField(help_text=b'En quoi votre sujet est-il sp\xc3\xa9cifiquement belge ? Que nous dit-il de la Belgique et comment, \xc3\xa0 travers lui, la Belgique nous parle-t-elle du monde ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'Belgique', blank=True)),
                ('approach', models.CharField(help_text=b'Sous quel angle (original, surprenant ou amusant) allez-vous aborder ce sujet ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'approche', blank=True)),
                ('sources', models.CharField(help_text=b'Aupr\xc3\xa8s de quelles sources ou quels types de sources (principales) pensez-vous d\xc3\xa9marrer votre recherche ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'sources', blank=True)),
                ('method', models.CharField(help_text=b'Comment comptez-vous obtenir vos informations et vous immerger dans votre th\xc3\xa9matique ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'm\xc3\xa9thode', blank=True)),
                ('difficulties', models.CharField(help_text=b'Quelles difficult\xc3\xa9s (principales et particuli\xc3\xa8res) pr\xc3\xa9voyez-vous de rencontrer dans la r\xc3\xa9alisation de votre enqu\xc3\xaate ou reportage ? Comment pr\xc3\xa9voyez-vous de pallier ces difficult\xc3\xa9s ? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'difficult\xc3\xa9s', blank=True)),
                ('term', models.CharField(help_text=b'Quand pr\xc3\xa9voyez-vous de remettre votre contribution (d\xc3\xa9finitive) \xc3\xa0 M\xc3\xa9dor ?', max_length=200, verbose_name=b'\xc3\xa9ch\xc3\xa9ance', blank=True)),
                ('miscellaneous', models.CharField(help_text=b'Avez-vous une remarque ou une demande particuli\xc3\xa8re li\xc3\xa9e \xc3\xa0 votre proposition? \xe2\x80\x94 500 signes maximum.', max_length=500, verbose_name=b'divers', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
