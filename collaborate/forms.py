# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleProposal


class ArticleProposalForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    presentation = forms.CharField(
        max_length=300,
        label=u"Présentation",
        help_text=u"Qui êtes-vous ? Présentez-vous en quelques mots (expérience, collaborations actuelles, site personnel…) ?",
        widget=forms.Textarea()
    )
    media = forms.CharField(
        max_length=200,
        label=u"Spécialité",
        help_text=u"Quel(s) moyen(s) d’expression maîtrisez vous et souhaitez vous utiliser (écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres) ?",
        widget=forms.Textarea()
    )
    partnership = forms.CharField(
        max_length=200,
        label=u"Partenaire",
        help_text=u"Médor vous suggérera de travailler avec un partenaire. Quel type de synergie s’appliquerait bien à votre sujet : écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres ?",
        widget=forms.Textarea()
    )
    innovation = forms.CharField(
        max_length=500,
        label=u"Originalité",
        help_text=u"En quoi votre sujet est-il original ? En a-t-on déjà parlé dans les médias francophones belges ?",
        widget=forms.Textarea()
    )
    approach = forms.CharField(
        max_length=500,
        label=u"Approche",
        help_text=u"Sous quel angle (original, surprenant ou amusant) allez-vous aborder ce sujet ?",
        widget=forms.Textarea()
    )
    method = forms.CharField(
        max_length=500,
        label=u"Méthode",
        help_text=u"Quelles sont vos sources et vos hypothèses de travail ? Vos moyens pour obtenir les informations ? Les données dont vous disposez déjà ? Et en quoi cela concerne-t-il la Belgique ?",
        widget=forms.Textarea()
    )
    miscellaneous = forms.CharField(
        max_length=500,
        label=u"Divers",
        help_text=u"Avez-vous une remarque ou une demande particulière liée à votre proposition ?",
        widget=forms.Textarea()
    )

    class Meta:
        model = ArticleProposal
        fields = [
            'name',
            'email',
            'phone',
            'twitter_account',
            'address',
            'presentation',
            'subject_title',
            'abstract',
            'media',
            'partnership',
            'section',
            'innovation',
            'approach',
            'method',
            'miscellaneous',
            'is_urgent',
        ]

        widgets = {
            'address': forms.Textarea(attrs={'rows':5, 'cols': ''}),
            'subject_title': forms.Textarea(attrs={'rows':2}),
            'abstract': forms.Textarea(),
            'media': forms.Textarea(),
            'section': forms.RadioSelect(),
        }

    def clean(self):
        cleaned_data = super(ArticleProposalForm, self).clean()

        fields = ["presentation", "media", "partnership", "innovation", "approach", "method",
                "miscellaneous"]

        body = []

        for f in fields:
            data = cleaned_data.get(f, '')

            field = self.fields[f]

            body.append(u"# %s" % field.label)
            body.append(field.help_text)
            body.append(data)

        self.instance.body = u"\n\n".join(body)


class ArticleProposalSimpleForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    subject_title = forms.CharField(
        max_length=300,
        label=u"Thème de votre information",
        help_text=u"Résumez le plus clairement possible votre sujet.",
        widget=forms.Textarea()
    )

    abstract = forms.CharField(
        max_length=750,
        label=u"Résumé",
        help_text=u"Décrivez en quelques phrases l’information que vous voulez nous communiquer. Les faits, le type de preuves, l’existence de témoignages…",
        widget=forms.Textarea()
    )

    relevance = forms.CharField(
        max_length=300,
        label=u"Pertinence",
        help_text=u"Pourquoi, selon vous, il faudrait absolument en parler ?",
        widget=forms.Textarea()
    )

    independance = forms.CharField(
        max_length=300,
        label=u"Indépendance",
        help_text=u"Vous estimez-vous totalement indépendant et libre par rapport à ce sujet ? Pas de conflit d’intérêt ?",
        widget=forms.Textarea()
    )

    support = forms.CharField(
        max_length=500,
        label=u"Soutien",
        help_text=u"Quel type de soutien souhaiteriez vous avoir de l’équipe de Médor ?",
        widget=forms.Textarea()
    )


    class Meta:
        model = ArticleProposal
        fields = [
            'name',
            'email',
            'phone',
            'twitter_account',
            'address',
            'subject_title',
            'abstract',
            #'is_urgent',
        ]

        widgets = {
            'address': forms.Textarea(attrs={'rows':5, 'cols': ''}),
            'subject_title': forms.Textarea(attrs={'rows':2}),
            'abstract': forms.Textarea(),
            'media': forms.Textarea(),
            'section': forms.RadioSelect(),
        }

    def clean(self):
        cleaned_data = super(ArticleProposalSimpleForm, self).clean()

        fields = ["relevance", "independance", "support"]

        body = []

        for f in fields:
            data = cleaned_data.get(f, '')

            field = self.fields[f]

            body.append(u"# %s" % field.label)
            body.append(field.help_text)
            body.append(data)

        self.instance.body = u"\n\n".join(body)
