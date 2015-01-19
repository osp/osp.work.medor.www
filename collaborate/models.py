# -*- coding: utf-8 -*-
from django.db import models



class ArticleProposal(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="nom"
    )
    email = models.EmailField(
        max_length=75,
        verbose_name="courriel"
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="téléphone"
    )
    twitter_account = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="compte twitter"
    )
    address = models.TextField(
        verbose_name="adresse"
    )
    subject_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="intitulé du sujet (provisoire)",
        help_text="Titre le plus clair possible. Avec sous-titre éventuel"
    )
    is_urgent = models.BooleanField(
        default=False,
        verbose_name="Urgence",
        help_text="Votre sujet nécessite-t-il une publication rapide sur le web ou sur papier (pour préserver l'exclusivité par exemple) ? Si oui, il n'est pas nécessaire de remplir le formulaire entièrement (200 signes)"
    )
    abstract = models.CharField(
        max_length=750,
        blank=True,
        verbose_name="résumé (prévisionnel)",
        help_text="Rédiger comme s’il s’agissait d’un chapeau destiné à un média généraliste. (750 max)"
    )
    media = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="média",
        help_text="Quel forme de contribution envisagez-vous ? Écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres (précisez). (max 200)"
    )
    partnership = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="partenariat",
        help_text="Quelle synergie serait possible entre votre projet et un autre correspondant de Médor : écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres (précisez) (200)"
    )
    section = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="rubrique concernée (a priori)",
        help_text="Destinez-vous votre sujet à une rubrique précise ? Entretien, portrait, récit, enquête, brèves. (200)"
    )
    space = models.FloatField(
        verbose_name="format",
        help_text="Quelle serait, selon vous, l'espace nécessaire à votre contribution en nombre de pages? (une page de Médor = 16/23 ou +-2000 signes)"
    )
    sectioning = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="découpage",
        help_text="Votre sujet se décline-t-il en plusieurs entrées ? Sinon, le pourrait-il ? Où va votre préférence et pourquoi ? (500)"
    )
    innovation = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="innovation",
        help_text="En quoi votre sujet est-il innovant par rapport à l’offre médiatique francophone de Belgique ? (500)"
    )
    belgian = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Belgique",
        help_text="En quoi votre sujet est-il spécifiquement belge ? Que nous dit-il de la Belgique et comment, à travers lui, la Belgique nous parle-t-elle du monde ? (500)"
    )
    approach = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="approche",
        help_text="Sous quel angle (original, surprenant ou amusant) allez-vous aborder ce sujet ? (500)"
    )
    sources = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="sources",
        help_text="Auprès de quelle sources ou quels types de sources (principales) pensez-vous démarrer votre recherche ? (500)"
    )
    method = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="méthode",
        help_text="Comment comptez-vous obtenir vos informations et vous immerger dans votre thématique ? (500)"
    )
    difficulties = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="difficultés",
        help_text="Quelles difficultés (principales et particulières) prévoyez-vous de rencontrer dans la réalisation de votre enquête ou votre reportage ? Comment prévoyez-vous de pallier ces difficultés ? (500)"
    )
    term = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="échéance",
        help_text="Quand prévoyez-vous de remettre votre contribution (définitive) à Médor ? Quelle date vous conviendrait le mieux ? (200)"
    )
    miscellaneous = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="divers",
        help_text="Avez-vous une remarque ou une demande particulière à adresser avec votre proposition ? (500)"
    )






