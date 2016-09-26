from django.forms.widgets import CheckboxSelectMultiple, CheckboxFieldRenderer, CheckboxChoiceInput
from django.utils.html import format_html


class CustomCheckboxChoiceInput(CheckboxChoiceInput):
    def render(self, name=None, value=None, attrs=None):
        if self.id_for_label:
            label_for = format_html(u' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        return format_html(
            u'{}<label{}>{}</label>', self.tag(attrs), label_for, self.choice_label
        )


class CustomCheckboxFieldRenderer(CheckboxFieldRenderer):
    choice_input_class = CustomCheckboxChoiceInput
    outer_html = u'<ul class="flex flex--outline product-list" {id_attr}>{content}</ul>'
    inner_html = u'<li class="flex__item flex__cell">{choice_value}{sub_widgets}</li>'

    def __init__(self, name, value, attrs, choices):
        self.name = name
        self.value = value
        self.attrs = attrs
        self.choices = choices


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    renderer = CustomCheckboxFieldRenderer
