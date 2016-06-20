# -*- coding: utf-8 -*-

from buy.models import RetailOutlet

import unicodecsv
from django.http import HttpResponse



def retail_outlet_as_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="retail-outlets.csv"'
    response['Access-Control-Allow-Origin'] = 'https://umap.openstreetmap.fr'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow([
        "name",
        "description",
        "latitude",
        "longitude",
    ])

    for r in RetailOutlet.objects.all():
        writer.writerow([
            r.name,
            u"%s, %s %s, %s" % (r.address, r.zip_code, r.city, r.country),
            u"%s" % r.latitude,
            u"%s" % r.longitude
        ])

    return response
