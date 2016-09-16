from django.forms.widgets import CheckboxSelectMultiple, CheckboxFieldRenderer


class CustomCheckboxFieldRenderer(CheckboxFieldRenderer):
    outer_html = u'<ul class="flex__item flex flex--outline jadore__widget" {id_attr}>{content}</ul>'
    inner_html = u'<li class="flex__item flex__cell">{choice_value}{sub_widgets}</li>'


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    renderer = CustomCheckboxFieldRenderer
