from django import forms
from .models import ArticleProposal


class ArticleProposalForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = ArticleProposal
        widgets = {
            'address': forms.Textarea(attrs={'rows':5, 'cols': ''}),
            'subject_title': forms.Textarea(attrs={'rows':2}),
            'abstract': forms.Textarea(),
            'media': forms.Textarea(),
            'partnership': forms.Textarea(),
            'section': forms.RadioSelect(),
            'space': forms.TextInput(),
            'sectioning': forms.Textarea(),
            'innovation': forms.Textarea(),
            'belgian': forms.Textarea(),
            'approach': forms.Textarea(),
            'sources': forms.Textarea(),
            'method': forms.Textarea(),
            'difficulties': forms.Textarea(),
            'term': forms.Textarea(attrs={'rows':3}),
            'miscellaneous': forms.Textarea(),
        }
