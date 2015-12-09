# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def set_issue_number(apps, schema_editor):
    Subscription = apps.get_model("subscribe", "Subscription")


    # Le 6 novembre, j'ai ajouté un champ "date de confirmation". Tous les
    # abonnés qui étaient en ordre de payement ce jour là se sont vu assigner
    # une date de confirmation égale à leur date d'encodage. (1467 abonnements).

    # Tous les autres depuis une une date de confirmation non-renseignée,
    # puisque comme je suis un peu un boulet parfois je n'ai pas ajouté la
    # ligne de code qui renseigne automatiquement la date lors du changement
    # de statut (passage en confirmé).

    # Nous pouvons donc assumer que toutes les personnes avec une date de
    # confirmation *renseignée* se sont inscrites pour les numéros 1, 2, 3 et 4.

    Subscription.objects.filter(confirmation_date__isnull=False).update(from_issue=1)

    # Par contraste, toutes les autres sont inscrites par défaut pour les
    # numéros 2, 3, 4 et 5, sauf si elles sont présentes dans la feuille de
    # calcul "Tardifs" (je corrige à la main) et si elles en ont fait la
    # demande mais ne sont pas encore traitées.

    Subscription.objects.filter(confirmation_date__isnull=True).exclude(status=2).update(from_issue=2)


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0010_subscription_from_issue'),
    ]

    operations = [
        migrations.RunPython(set_issue_number),
    ]
