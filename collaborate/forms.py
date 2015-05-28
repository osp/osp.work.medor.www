# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleProposal


class ArticleProposalForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    media = forms.CharField(
        max_length=200,
        label=u"Média",
        help_text=u"Quelle(s) contribution(s) envisagez-vous ? Écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres (précisez).",
        widget=forms.Textarea()
    )
    partnership = forms.CharField(
        max_length=200,
        label=u"Partenariat",
        help_text=u"Quelle synergie serait possible entre votre projet et un autre correspondant de Médor : écrits, photographies, dessins, peintures, infographies, vidéo, son, jeux de rôles, autres (précisez).",
        widget=forms.Textarea()
    )
    space = forms.CharField(
        max_length=200,
        label=u"Format",
        help_text=u"Une page Médor mesure 16 x 23 cm, soit environ 2000 signes. Quel serait, selon vous, l'espace nécessaire à votre contribution en nombre de pages ?",
        widget=forms.TextInput()
    )
    sectioning = forms.CharField(
        max_length=500,
        label=u"Découpage",
        help_text=u"Votre sujet se décline-t-il en plusieurs entrées ? Sinon, le pourrait-il ?",
        widget=forms.Textarea()
    )
    innovation = forms.CharField(
        max_length=500,
        label=u"Originalité",
        help_text=u"En quoi votre sujet est-il original par rapport à l’offre médiatique francophone de Belgique ?",
        widget=forms.Textarea()
    )
    belgian = forms.CharField(
        max_length=500,
        label=u"Belgique",
        help_text=u"En quoi votre sujet est-il spécifiquement belge ? Que nous dit-il de la Belgique et comment, à travers lui, la Belgique nous parle-t-elle du monde ?",
        widget=forms.Textarea()
    )
    approach = forms.CharField(
        max_length=500,
        label=u"Approche",
        help_text=u"Sous quel angle (original, surprenant ou amusant) allez-vous aborder ce sujet ?",
        widget=forms.Textarea()
    )
    sources = forms.CharField(
        max_length=500,
        label=u"Sources",
        help_text=u"Auprès de quelles sources ou quels types de sources (principales) pensez-vous démarrer votre recherche ?",
        widget=forms.Textarea()
    )
    method = forms.CharField(
        max_length=500,
        label=u"Méthode",
        help_text=u"Comment comptez-vous obtenir vos informations et vous immerger dans votre thématique ?",
        widget=forms.Textarea()
    )
    difficulties = forms.CharField(
        max_length=500,
        label=u"Difficultés",
        help_text=u"Quelles difficultés (principales et particulières) prévoyez-vous de rencontrer dans la réalisation de votre enquête ou reportage ? Comment prévoyez-vous de pallier ces difficultés ?",
        widget=forms.Textarea()
    )
    term = forms.CharField(
        max_length=200,
        label=u"Échéance",
        help_text=u"Une fois un feu vert de Médor, de combien de temps aurez-vous besoin avant nous remettre une version finale du projet ?",
        widget=forms.Textarea(attrs={'rows':3})
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
            'subject_title',
            'is_urgent',
            'abstract',
            'media',
            'partnership',
            'section',
            'space',
            'sectioning',
            'innovation',
            'belgian',
            'approach',
            'sources',
            'method',
            'difficulties',
            'term',
            'miscellaneous'
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

        fields = ["media", "partnership", "space", "sectioning", "innovation",
                "belgian", "approach", "sources", "method", "difficulties",
                "term", "miscellaneous"]

        body = []

        for f in fields:
            data = cleaned_data.get(f)

            field = self.fields[f]

            body.append(u"# %s" % field.label)
            body.append(field.help_text)
            body.append(data)

        self.instance.body = u"\n\n".join(body)
