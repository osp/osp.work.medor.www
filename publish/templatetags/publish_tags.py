from django import template

import HTMLParser
from publish.utils import typogrify as typogrify_util


register = template.Library()


@register.filter(name='times')
def times(number):
    return range(1, number + 1)


@register.filter(name='decode_entities')
def decode_entities(text):
    html_parser = HTMLParser.HTMLParser()
    return html_parser.unescape(text)


@register.filter(name='typogrify')
def typogrify(html):
    return typogrify_util(html)
