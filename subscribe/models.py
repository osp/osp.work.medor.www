# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
from django.db.models import Max
from django.template.loader import render_to_string
from django.core.mail import send_mail

from subscribe import settings

from filer.fields.image import FilerImageField


TITLE_CHOICES = (
    (False, 'Madame'),
    (True, 'Monsieur')
)


class TransactionBase(models.Model):
    STATUS_CHOICES = (
        (0, 'en cours'),
        (1, 'confirmé'),
        (2, 'annulé')
    )

    COUNTRY_CHOICES = (
        ('AL', 'Albanie'),
        ('PT-20', 'Açores'),
        ('DE', 'Allemagne'),
        ('AD', 'Andorre'),
        ('AT', 'Autriche'),
        ('BE', 'Belgique'),
        ('BY', 'Biélorussie'),
        ('BA', 'Bosnie-Herzégovine'),
        ('BG', 'Bulgarie'),
        ('IC', 'Canaries (Îles)'),
        ('ES-CE', 'Ceuta'),
        ('CY', 'Chypre'),
        ('HR', 'Croatie'),
        ('DK', 'Danemark'),
        ('ES', 'Espagne'),
        ('EE', 'Estonie'),
        ('FO', 'Féroé (Îles)'),
        ('FI', 'Finlande'),
        ('FR', 'France (sauf DOM-TOM)'),
        ('GE', 'Géorgie'),
        ('GI', 'Gibraltar'),
        ('GB', 'Grande-Bretagne'),
        ('GR', 'Grèce'),
        ('GL', 'Groenland'),
        ('GG', 'Guernesey'),
        ('HU', 'Hongrie'),
        ('IE', 'Irlande'),
        ('IS', 'Islande'),
        ('IT', 'Italie'),
        ('JE', 'Jersey'),
        ('LV', 'Lettonie'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lituanie'),
        ('LU', 'Luxembourg (Grand-Duché de)'),
        ('MK', 'Macédoine'),
        ('PT-30', 'Madère'),
        ('MT', 'Malte'),
        ('IM', 'Man (Île de)'),
        ('Me', 'Melilla'),
        ('MD', 'Moldavie'),
        ('MC', 'Monaco'),
        ('ME', 'Monténégro'),
        ('NO', 'Norvège'),
        ('NL', 'Pays-Bas'),
        ('PL', 'Pologne'),
        ('PT', 'Portugal'),
        ('CZ', 'République tchèque'),
        ('RO', 'Roumanie'),
        ('RU', 'Russie'),
        ('SM', 'Saint-Martin'),
        ('RS', 'Serbie'),
        ('SK', 'Slovaquie'),
        ('SI', 'Slovénie'),
        ('SE', 'Suède'),
        ('CH', 'Suisse'),
        ('TR', 'Turquie'),
        ('UA', 'Ukraine'),
        ('VA', 'Vatican')
    )

    title = models.BooleanField('civilité', default=False, choices=TITLE_CHOICES)
    first_name = models.CharField('prénom', max_length=30)
    last_name = models.CharField('nom', max_length=30)
    email = models.EmailField('courriel')
    street = models.CharField('rue', max_length=30)
    number = models.CharField('numéro', max_length=50) # 27 bis
    letterbox = models.PositiveSmallIntegerField('boîte postale', null=True, blank=True)
    city = models.CharField('ville', max_length=30)
    zip_code = models.PositiveSmallIntegerField('code postal')
    country = models.CharField('pays', max_length=5, choices=COUNTRY_CHOICES, default="BE")
    creation_date = models.DateTimeField('date de création', auto_now_add=True)
    confirmation_date = models.DateTimeField('date de confirmation du paiement', null=True, blank=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    invoice_reference = models.PositiveIntegerField('référence facture', unique=True, blank=True)
    comment = models.TextField('commentaire', blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"{} {}, {}".format(self.last_name, self.first_name, self.get_title_display())

    def save(self, *args, **kwargs):
        if not self.invoice_reference:
            now = datetime.now()
            _max = self.__class__.objects.filter(creation_date__year=now.year, creation_date__month=now.month).aggregate(Max('invoice_reference'))
            _max = _max['invoice_reference__max']
            if _max:
                _max = _max + 1
                _max = _max % 10000
            else:
                _max = 1

            invoice_reference = u"{}{}{:04d}".format(now.strftime("%y%m"), self.__class__.transaction_type, _max)
            self.invoice_reference = int(invoice_reference)

        super(TransactionBase, self).save(*args, **kwargs)

    def old_simple_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "{} {} {}".format(nbr[:3], nbr[3:7], nbr[7:])

    def simple_communication(self):
        ref = self.invoice_reference
        modulo = ref % 97
        modulo = modulo if modulo != 0 else 97
        nbr = "{}{:02d}".format(ref, modulo)
        return "{} {} {}".format(nbr[:3], nbr[3:7], nbr[7:])

    def old_structured_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])

    def structured_communication(self):
        ref = self.invoice_reference
        modulo = ref % 97
        modulo = modulo if modulo != 0 else 97
        nbr = "{}{:02d}".format(ref, modulo)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])


class Subscription(TransactionBase):
    """ Describes a subscription"""
    ISSUE_CHOICES = (
        (None, '---'),
        (1, 'du 1 au 4'),
        (2, 'du 2 au 5'),
        (3, 'du 3 au 6'),
        (4, 'du 4 au 7'),
        (5, 'du 5 au 8'),
        (6, 'du 6 au 9')
    )

    transaction_type = '01'
    from_issue = models.PositiveSmallIntegerField('à partir du numéro', choices=ISSUE_CHOICES, blank=True, null=True)
    is_gift = models.BooleanField('ceci est un cadeau?', default=False)
    recipient_title = models.BooleanField('civilité du destinataire', default=False, choices=TITLE_CHOICES)
    recipient_first_name = models.CharField('prénom du destinataire', max_length=30, blank=True)
    recipient_last_name = models.CharField('nom de famille du destinataire', max_length=30, blank=True)
    recipient_email = models.CharField('courriel du destinataire', max_length=30, blank=True)

    class Meta:
        verbose_name = "abonnement"
        verbose_name_plural = "abonnements"

    __original_status = None

    def __init__(self, *args, **kwargs):
        super(Subscription, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        if not self.from_issue:
            now = datetime.now()
            if now >= datetime(2016, 9, 16):
                self.from_issue = 5
            elif now >= datetime(2016, 6, 20):
                self.from_issue = 4
            elif now >= datetime(2016, 3, 11):
                self.from_issue = 3
            else:
                self.from_issue = 2

        do_send_mail = False

        if self.status != self.__original_status and self.status == 1:
            # If the status has changed and is confirmed, mark for sending a
            # confirmation email
            do_send_mail = True

            # Also sets the confirmation date to now
            self.confirmation_date = datetime.now()


        super(Subscription, self).save(*args, **kwargs)
        self.__original_status = self.status

        # Do send the email
        if do_send_mail:
            subject = "Médor SCRL FS. Confirmation d'abonnement"
            if self.from_issue == 5:
                message = render_to_string('subscribe/subscription-confirmation-email-5-8.txt', {'obj': self})
            elif self.from_issue == 4:
                message = render_to_string('subscribe/subscription-confirmation-email-4-7.txt', {'obj': self})
            elif self.from_issue == 3:
                message = render_to_string('subscribe/subscription-confirmation-email-3-6.txt', {'obj': self})
            else:
                message = render_to_string('subscribe/subscription-confirmation-email-2-5.txt', {'obj': self})
            sender = "lesyeuxouverts@medor.coop"
            recipients = [self.email]
            send_mail(subject, message, sender, recipients, fail_silently=False)



    def amount(self):
        shipping = 20 if (self.country != "BE" and self.creation_date.date() > date(2015, 1, 20)) else 0
        return 60 + shipping


class Cooperation(TransactionBase):
    """ Describes a cooperation"""
    transaction_type = '02'

    SHARE_CHOICES = (
        (1, '1 (€ 20)'),
        (2, '2 (€ 40)'),
        (3, '3 (€ 60)'),
        (4, '4 (€ 80)'),
        (5, '5 (€ 100)'),
        (6, '6 (€ 120)'),
        (7, '7 (€ 140)'),
        (8, '8 (€ 160)'),
        (9, '9 (€ 180)'),
        (10, '10 (€ 200)'),
        (11, '11 (€ 220)'),
        (12, '12 (€ 240)'),
        (13, '13 (€ 260)'),
        (14, '14 (€ 280)'),
        (15, '15 (€ 300)'),
        (16, '16 (€ 320)'),
        (17, '17 (€ 340)'),
        (18, '18 (€ 360)'),
        (19, '19 (€ 380)'),
        (20, '20 (€ 400)'),
        (50, '50 (€ 1000)')
    )

    share_number = models.PositiveSmallIntegerField('nombre de parts', choices=SHARE_CHOICES, default="1")

    class Meta:
        verbose_name = "part coopérative"
        verbose_name_plural = "parts coopérative"

    __original_status = None

    def __init__(self, *args, **kwargs):
        super(Cooperation, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        do_send_mail = False

        if self.status != self.__original_status and self.status == 1:
            # If the status has changed and is confirmed, mark for sending a
            # confirmation email
            do_send_mail = True

            # Also sets the confirmation date to now
            self.confirmation_date = datetime.now()

        super(Cooperation, self).save(*args, **kwargs)
        self.__original_status = self.status

        # Do send the email
        if do_send_mail:
            subject = "Médor SCRL FS. Détails de votre paiement"
            message = render_to_string('subscribe/cooperation-confirmation-email.txt', {'obj': self})
            sender = "lesyeuxouverts@medor.coop"
            recipients = [self.email]
            send_mail(subject, message, sender, recipients, fail_silently=False)

    def amount(self):
        return self.share_number * 20


###############################################


class ShippingDetails(models.Model):
    COUNTRY_CHOICES = (
        ('AL', 'Albanie'),
        ('PT-20', 'Açores'),
        ('DE', 'Allemagne'),
        ('AD', 'Andorre'),
        ('AT', 'Autriche'),
        ('BE', 'Belgique'),
        ('BY', 'Biélorussie'),
        ('BA', 'Bosnie-Herzégovine'),
        ('BG', 'Bulgarie'),
        ('IC', 'Canaries (Îles)'),
        ('ES-CE', 'Ceuta'),
        ('CY', 'Chypre'),
        ('HR', 'Croatie'),
        ('DK', 'Danemark'),
        ('ES', 'Espagne'),
        ('EE', 'Estonie'),
        ('FO', 'Féroé (Îles)'),
        ('FI', 'Finlande'),
        ('FR', 'France (sauf DOM-TOM)'),
        ('GE', 'Géorgie'),
        ('GI', 'Gibraltar'),
        ('GB', 'Grande-Bretagne'),
        ('GR', 'Grèce'),
        ('GL', 'Groenland'),
        ('GG', 'Guernesey'),
        ('HU', 'Hongrie'),
        ('IE', 'Irlande'),
        ('IS', 'Islande'),
        ('IT', 'Italie'),
        ('JE', 'Jersey'),
        ('LV', 'Lettonie'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lituanie'),
        ('LU', 'Luxembourg (Grand-Duché de)'),
        ('MK', 'Macédoine'),
        ('PT-30', 'Madère'),
        ('MT', 'Malte'),
        ('IM', 'Man (Île de)'),
        ('Me', 'Melilla'),
        ('MD', 'Moldavie'),
        ('MC', 'Monaco'),
        ('ME', 'Monténégro'),
        ('NO', 'Norvège'),
        ('NL', 'Pays-Bas'),
        ('PL', 'Pologne'),
        ('PT', 'Portugal'),
        ('CZ', 'République tchèque'),
        ('RO', 'Roumanie'),
        ('RU', 'Russie'),
        ('SM', 'Saint-Martin'),
        ('RS', 'Serbie'),
        ('SK', 'Slovaquie'),
        ('SI', 'Slovénie'),
        ('SE', 'Suède'),
        ('CH', 'Suisse'),
        ('TR', 'Turquie'),
        ('UA', 'Ukraine'),
        ('VA', 'Vatican')
    )

    first_name = models.CharField("prénom", max_length=255,)
    last_name = models.CharField("nom", max_length=255)
    email = models.EmailField('courriel')

    street = models.CharField('rue', max_length=255)
    number = models.CharField('numéro', max_length=64) # 27 bis
    box = models.CharField('boîte', max_length=64, blank=True)
    postcode = models.CharField("code postal", max_length=64)
    city = models.CharField('ville', max_length=255)
    country = models.CharField('pays', max_length=5, choices=COUNTRY_CHOICES, default="BE")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Item(models.Model):
    """Represents an buyable item"""
    TRANSACTION_TYPE_CHOICES = (
        (1, 'Abonnement'),
        (2, 'À la pièce'),
    )
    is_published = models.BooleanField('est publié?', default=False)
    image = FilerImageField(null=True, blank=True)
    transaction_type = models.PositiveSmallIntegerField('type de transaction', choices=TRANSACTION_TYPE_CHOICES)
    name = models.CharField('nom', max_length=255)
    price = models.DecimalField('prix', max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    """Represents an order placed."""
    STATUS_CHOICES = (
        (0, 'encodé'),
        (1, 'payé'),
        (2, 'annulé')
    )

    # TODO: Fix the code generation
    transaction_type = '03'

    first_name = models.CharField("prénom", max_length=255)
    last_name = models.CharField("nom", max_length=255)
    organization = models.CharField("organisation", max_length=255, blank=True)
    email = models.EmailField('courriel')

    status = models.PositiveSmallIntegerField('statut du payement', choices=STATUS_CHOICES, default=0)
    shipping_details = models.ForeignKey(ShippingDetails, verbose_name='Adresse de livraison')
    creation_date = models.DateTimeField('date d\'encodage', auto_now_add=True)
    confirmation_date = models.DateTimeField('date de validation du payement',
            null=True, blank=True)
    # FIXME: change value for unique and null
    invoice_reference = models.PositiveIntegerField('référence facture',
            unique=False, blank=True, null=True)
    amount = models.DecimalField('total', max_digits=5, decimal_places=2, blank=True, null=True)
    is_gift = models.BooleanField('ceci est un cadeau', default=False)
    promo_code = models.CharField('code promo', max_length=255, blank=True)
    items = models.ManyToManyField(Item, through='ItemMembership', verbose_name="items")

    comment = models.TextField('commentaire', blank=True)
    # TODO: + editer les infos d'envois en ligne

    __original_status = None

    class Meta:
        verbose_name = "commande"
        verbose_name_plural = "commandes"

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)

        # Keeps track of the instance current status so we can check if it has
        # changed
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        # Checks if the instance is new
        pk = self.pk

        # If the instance is beeing created, sets the invoice reference so we
        # can compute the structured communication for the wire transfer;
        if not pk:
            self.set_invoice_reference()

        # If the status has changed and is confirmed:
        # 1. sets the confirmation date to now;
        # 2. sends a confirmation email.
        if self.status != self.__original_status and self.status == 1:
            self.confirmation_date = datetime.now() # 1.
            self.send_confirmation_email()  # 2.

        super(Order, self).save(*args, **kwargs)

        self.__original_status = self.status

        # If the instance is beeing created, sends an email with the order
        # details.
        if not pk:
            # FIXME: m2m relations are not yet populated at this point
            # TODO: send the email at the form level, not here!
            #  self.send_details_email()
            pass

    def send_details_email(self):
        subject = "Médor SCRL FS. Détails de votre commande"
        message = render_to_string('subscribe/order-details-email.txt', {'obj': self})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [self.email]
        send_mail(subject, message, sender, recipients, fail_silently=False)

    def send_confirmation_email(self):
        subject = "Médor SCRL FS. Confirmation de votre paiement"
        message = render_to_string('subscribe/order-confirmation-email.txt', {'obj': self})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [self.email]
        send_mail(subject, message, sender, recipients, fail_silently=False)

    def set_invoice_reference(self):
        # FIXME: changer le code type de produit en fonction du panier
        now = datetime.now()
        _max = self.__class__.objects.filter(creation_date__year=now.year,
                creation_date__month=now.month).aggregate(Max('invoice_reference'))
        _max = _max['invoice_reference__max']
        if _max:
            _max = _max + 1
            _max = _max % 10000
        else:
            _max = 1

        invoice_reference = u"{}{}{:04d}".format(now.strftime("%y%m"), self.__class__.transaction_type, _max)
        self.invoice_reference = int(invoice_reference)

    def old_simple_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "{} {} {}".format(nbr[:3], nbr[3:7], nbr[7:])

    def simple_communication(self):
        ref = self.invoice_reference
        modulo = ref % 97
        modulo = modulo if modulo != 0 else 97
        nbr = "{}{:02d}".format(ref, modulo)
        return "{} {} {}".format(nbr[:3], nbr[3:7], nbr[7:])

    def old_structured_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])

    def structured_communication(self):
        if self.invoice_reference:
            ref = self.invoice_reference
            modulo = ref % 97
            modulo = modulo if modulo != 0 else 97
            nbr = "{}{:02d}".format(ref, modulo)
            return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])
        else:
            return None

    def items_as_list(self):
        out = []
        for membership in self.itemmembership_set.all():
            out.append(u"{} x {}".format(membership.item, membership.quantity))

        return u", ".join(out)

    @property
    def price(self):
        """Returns the price without shipping costs."""
        return sum([i.price for i in self.itemmembership_set.all()])

    @property
    def grand_total(self):
        """Returns the grand total of the order, including shipping costs."""
        amount = self.price

        # In case the shipping is in Belgium, do not add extra costs
        if self.shipping_details.country == "BE":
            return amount

        # Otherwise, computes the amount with the following logic:
        else:
            # Counts the number of items of type "à la pièce" and adds the
            # shipping cost for those items
            issue_count = self.items.filter(transaction_type=2).count()
            if issue_count:
                costs = settings.PER_ITEM_EUROPE_SHIPPING_COSTS
                filtered = {k: v for k, v in costs.iteritems() if k >= issue_count}
                amount += min(filtered.items(), key=lambda x: x[0])[1]

            # Adds the shipping costs for subscriptions
            subscription_count = self.itemmembership_set.filter(item__transaction_type=1).count()
            amount += subscription_count * settings.SUBSCRIPTION_EUROPE_SHIPPING_COSTS

            return amount

    def __unicode__(self):
        return self.shipping_details.__unicode__()


class ItemMembership(models.Model):
    """ Ordered item"""

    order = models.ForeignKey(Order, verbose_name="commande")
    item = models.ForeignKey(Item, verbose_name="item")
    quantity = models.PositiveSmallIntegerField('quantité', default=1)
    is_shipped = models.BooleanField('envoyé?', default=False)

    @property
    def order_status(self):
        return self.order.get_status_display()

    @property
    def price(self):
        """Returns the price without shipping costs."""

        return self.item.price * self.quantity

    def __unicode__(self):
        return self.item.name
