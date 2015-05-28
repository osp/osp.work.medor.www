# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_body(apps, schema_editor):
    # We can't import the ArticleProposal model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    ArticleProposal = apps.get_model("collaborate", "ArticleProposal")

    for proposal in ArticleProposal.objects.all():
        body = []

        fields = ["media", "partnership", "space", "sectioning", "innovation",
                "belgian", "approach", "sources", "method", "difficulties",
                "term", "miscellaneous"]

        for f in fields:
            field = proposal._meta.get_field(f)

            body.append(u"# %s" % field.verbose_name.decode('utf-8'))
            body.append(field.help_text.decode('utf-8'))
            body.append(getattr(proposal, f))

        proposal.body = u"\n\n".join(body)
        proposal.save()


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0007_articleproposal_body'),
    ]

    operations = [
        migrations.RunPython(populate_body),
    ]
