# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleProposal


class ArticleProposalForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = ArticleProposal
        fields = [
            'name',
            'email',
            'phone',
            'twitter_account',
            'address',
            'subject_title',
            'body'
        ]

        widgets = {
            'address': forms.Textarea(attrs={'rows': 5, 'cols': ''}),
        }


class ArticleProposalSimpleForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = ArticleProposal
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'subject_title',
            'body'
        ]

        widgets = {
            'address': forms.Textarea(attrs={'rows':5, 'cols': ''}),
        }
