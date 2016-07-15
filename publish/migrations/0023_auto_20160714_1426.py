# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import re
import html5lib
from html5lib.filters import _base


def remove_control_characters(html):
    def str_to_int(s, default, base=10):
        if int(s, base) < 0x10000:
            return unichr(int(s, base))
        return default
    html = re.sub(ur"&#(\d+);?", lambda c: str_to_int(c.group(1), c.group(0)), html)
    html = re.sub(ur"&#[xX]([0-9a-fA-F]+);?", lambda c: str_to_int(c.group(1), c.group(0), base=16), html)
    html = re.sub(ur"[\x00-\x08\x0b\x0e-\x1f\x7f]", "", html)
    return html


class BodyContentFilter(_base.Filter):
    def __iter__(self):
        emit = False

        for token in _base.Filter.__iter__(self):

            if token["type"] == "StartTag" and token["name"] == "body":
                emit = True
                continue

            elif token["type"] == "EndTag" and token["name"] == "body":
                emit = False

            if emit:
                yield token


def move_chapo(apps, schema_editor):
    Article = apps.get_model("publish", "Article")

    walker = html5lib.getTreeWalker("lxml")
    s = html5lib.serializer.HTMLSerializer(quote_attr_values=True, omit_optional_tags=False)

    for article in Article.objects.all():
        print(article.title)
        tree = html5lib.parse(remove_control_characters(article.body), treebuilder="lxml", namespaceHTMLElements=False)

        chapo = tree.xpath("descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' chapeau ')]")

        if len(chapo):
            chapo[0].getparent().remove(chapo[0])
            del chapo[0].attrib["class"]
            stream2 = walker(chapo[0])
            article.lead = s.render(stream2)

        stream = walker(tree)
        stream = BodyContentFilter(stream)
        article.body = s.render(stream)

        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0022_article_lead'),
    ]

    operations = [
        migrations.RunPython(move_chapo),
    ]
