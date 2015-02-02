# -*- coding: utf-8 -*-
from django.db import models


SECTION_CHOICES = (
    (0, u'Enquête'),
    (1, u'Portrait ou récit'),
    (2, u'Interview'),
    (3, u'Portfolio photo'),
    (4, u'Autre')
)


class ArticleProposal(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=50,
        verbose_name="Nom"
    )
    email = models.EmailField(
        max_length=75,
        verbose_name="Courriel"
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Téléphone"
    )
    twitter_account = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Compte Twitter"
    )
    address = models.TextField(
        verbose_name="Adresse"
    )
    subject_title = models.CharField(
        max_length=300,
        verbose_name="Intitulé du sujet (provisoire)",
        help_text="Titre le plus clair possible. Avec sous-titre éventuel."
    )
    is_urgent = models.BooleanField(
        default=False,
        verbose_name="Urgence",
        help_text="Votre sujet nécessite-t-il une publication rapide sur le web ou sur papier (pour préserver l'exclusivité par exemple) ?"
    )
    abstract = models.CharField(
        max_length=750,
        verbose_name="Résumé (prévisionnel)",
        help_text="Rédigez comme s’il s’agissait d’un chapeau destiné à un média généraliste."
    )
    media = models.CharField(
        max_length=200,
        verbose_name="Média",
        help_text="Quelle(s) contribution(s) envisagez-vous ? Écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres (précisez)."
    )
    partnership = models.CharField(
        max_length=200,
        verbose_name="Partenariat",
        help_text="Quelle synergie serait possible entre votre projet et un autre correspondant de Médor : écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres (précisez)."
    )
    section = models.PositiveSmallIntegerField(
        choices=SECTION_CHOICES,
        default=0,
        verbose_name="Rubrique concernée (a priori)",
        help_text="Destinez-vous votre sujet à une rubrique précise ? Entretien, portrait, récit, enquête, brèves."
    )
    space = models.CharField(
        max_length=200,
        verbose_name="Format",
        help_text="Une page Médor mesure 16 x 23 cm, soit environ 2000 signes. Quelle serait, selon vous, l'espace nécessaire à votre contribution en nombre de pages ?"
    )
    sectioning = models.CharField(
        max_length=500,
        verbose_name="Découpage",
        help_text="Votre sujet se décline-t-il en plusieurs entrées ? Sinon, le pourrait-il ? Où va votre préférence et pourquoi ?"
    )
    innovation = models.CharField(
        max_length=500,
        verbose_name="Innovation",
        help_text="En quoi votre sujet est-il innovant par rapport à l’offre médiatique francophone de Belgique ?"
    )
    belgian = models.CharField(
        max_length=500,
        verbose_name="Belgique",
        help_text="En quoi votre sujet est-il spécifiquement belge ? Que nous dit-il de la Belgique et comment, à travers lui, la Belgique nous parle-t-elle du monde ?"
    )
    approach = models.CharField(
        max_length=500,
        verbose_name="Approche",
        help_text="Sous quel angle (original, surprenant ou amusant) allez-vous aborder ce sujet ?"
    )
    sources = models.CharField(
        max_length=500,
        verbose_name="Sources",
        help_text="Auprès de quelles sources ou quels types de sources (principales) pensez-vous démarrer votre recherche ?"
    )
    method = models.CharField(
        max_length=500,
        verbose_name="Méthode",
        help_text="Comment comptez-vous obtenir vos informations et vous immerger dans votre thématique ?"
    )
    difficulties = models.CharField(
        max_length=500,
        verbose_name="Difficultés",
        help_text="Quelles difficultés (principales et particulières) prévoyez-vous de rencontrer dans la réalisation de votre enquête ou reportage ? Comment prévoyez-vous de pallier ces difficultés ?"
    )
    term = models.CharField(
        max_length=200,
        verbose_name="Échéance",
        help_text="Une fois un feu vert de Médor, de combien de temps aurez-vous besoin avant nous remettre une version finale du projet ?"

    )
    miscellaneous = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Divers",
        help_text="Avez-vous une remarque ou une demande particulière liée à votre proposition ?"
    )
