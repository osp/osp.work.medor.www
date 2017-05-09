# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unicodecsv

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from buy.models import RetailOutlet


def retail_outlet_as_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Access-Control-Allow-Origin'] = 'https://umap.openstreetmap.fr'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow([
        "name",
        "description",
        "latitude",
        "longitude",
    ])

    for r in RetailOutlet.objects.filter(is_published=True):
        writer.writerow([
            r.name,
            "%s, %s %s, %s" % (r.address, r.zip_code, r.city, r.country),
            "%s" % r.latitude,
            "%s" % r.longitude
        ])

    return response
